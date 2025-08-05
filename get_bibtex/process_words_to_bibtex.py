# -------------- Basic Settings --------------
from get_bibtex.global_settings import *
import os
import requests
from lxml import etree

def set_proxy(proxy_url, proxy_port):
    os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
    os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'

# 设置代理
if proxy_related['enable']:
    set_proxy(proxy_related['proxy_url'], proxy_related['proxy_port'])

def get_data(q, source="google_scholar"):
    if source not in searchUrlBases:
        print(f"Source {source} is not supported.")
        return None
    source_settings = searchUrlBases[source]["bibtex_route"][0]
    url = source_settings["url"]
    search_url = url.replace("@@", q.strip())
    need_cookie = source_settings["need_cookie"]
    headers['Referer'] = search_url.split('?')[0]
    if need_cookie and headers['Cookie'] == "":
        print("No Cookie for %s! Please visit this page %s to get your cookie. Now will remove this source from searchWay." % (source, url.replace("@@", "1")))
        return None
    res = requests.get(search_url, headers=headers)
    content = res.text
    html = etree.HTML(content)
    dom_xpath = source_settings["dom"]
    elements = html.xpath(dom_xpath)
    if elements == []:
        print(f"{q} not found in {source} or you need captcha!")
        return None
    bibtex_link = elements[0].attrib['href']
    if "keyword_regex" in source_settings:
        for old, new in source_settings["keyword_regex"].items():
            bibtex_link = bibtex_link.replace(old, new)
    res = requests.get(bibtex_link, headers=headers)
    return res.text

def process_words_to_bibtex(words_path, result_bibtex_path='./result_bibtex.txt', result_cite_path='./result_cite.txt', done_path='./get_bibtex/done.txt'):
    to_delete = []
    # remove done
    # if done_path exists, remove done from words_path
    with open(done_path, 'w', encoding='utf-8') as fd:
        fd.write('')
    with open(result_cite_path, 'w', encoding='utf-8') as fc:
        fc.write('')
    with open(done_path, 'r', encoding='utf-8') as fd:
        with open(words_path, 'r', encoding='utf-8') as f:
            done_list = fd.readlines()
            q_list = f.readlines()
            after = list(set(q_list)-set(done_list))
            after.sort(key = q_list.index)
            q_list = after
    with open(words_path, 'w', encoding='utf-8') as f:
        f.writelines(q_list)
    index = 1  # 初始化编号，移到外层循环之前
    # find
    for q in q_list:
        if q == '\n' or not q.strip():
            continue
        with open(done_path, 'a', encoding='utf-8') as fd:
            with open(result_bibtex_path, 'a', encoding='utf-8') as fw:
                with open(result_cite_path, 'a', encoding='utf-8') as fc:
                    for search_way in searchWay:
                        result = get_data(q, search_way)
                        if result is not None:
                            # 动态替换 BibTeX 的第一行中的 cite_key 为 index，并保留逗号
                            first_line_end = result.find('\n')
                            if first_line_end != -1:
                                first_line = result[:first_line_end]
                                updated_first_line = first_line.split('{')[0] + f"{{{index},"
                                result = updated_first_line + result[first_line_end:]
                            fw.write(result+'\n')
                            fc.write(f"{index}\t{q.split(']')[0].strip()}\t\\cite{{{index}}}\n")
                            index += 1  # 编号递增
                            fd.write(q)
                    if to_delete != []:
                        for source in to_delete:
                            searchWay.remove(source)
                        to_delete = []

if __name__ == "__main__":
    process_words_to_bibtex('./words.txt')
