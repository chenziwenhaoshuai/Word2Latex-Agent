from zai import ZhipuAiClient
import json
from openai import OpenAI



client = ZhipuAiClient(api_key="")  # 请填写您自己的APIKey
gpt_client = OpenAI(base_url="",api_key="")  # 请填写您自己的APIKey

def llm(system_prompt, user_prompt):
    """
    通用的LLM调用函数
    :param text: 输入文本
    :param system_prompt: 系统提示词
    :param user_prompt: 用户提示词
    :return: LLM的响应内容
    """
    response = gpt_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content


def paper_split_agent(section, text):
    system_prompt = f"请在以下段落中提取出完整的{section}章节的全部完整内容，包括公式，图，表等，并将结果返回给我，不需要额外的回复，直接返回结果，下面是全文内容"
    prompt = f"{text}"
    response = llm(prompt, system_prompt)
    return response

def get_total_sections_agent(text):
    system_prompt = """请根据以下文本内容，提取出所有的章节标题，并将结果以json的形式返回给我，注意，章节不包括摘要和参考文献列表，只包括正文内容，不包括子章节，章节名称不要带编号，不需要额外的回复，直接返回结果具体格式为{"sections": ["Introduction", "Methods"...]}，其中sections为章节标题的列表，下面是全文内容"""
    prompt = f"{text}"
    r = llm(prompt, system_prompt)
    r = r.replace("```json", "").replace("```", "")
    r = json.loads(r)
    return r["sections"]

def clear_latex_template_agent(text):
    system_prompt = "请根据以下latex模板，去除章节里的内容，保留图片、表格的格式示例，保留正文之前的内容，并将清洗后的标准干净latex模板返回给我，不需要额外的回复，直接返回结果，下面是全文内容"
    prompt = f"{text}"
    response = llm(prompt, system_prompt)
    return response

def convert_markdown_to_latex_agent(template, section_content):
    system_prompt = template+r"""阅读前面的latex模板，请将以下markdown格式的论文内容转换为latex论文里的一章，保持原始的语言，以\section开始，如果遇到图片直接在图片位置进行插入，并设置好文件路径，如果图片很大，就用双栏排版，如果不大就用单栏排版，记得填写图片的caption，表格的要求与图片一致。遇到引用参考文献时，只需要使用\cite{1}等直接标号就可以，直接将转换的结果返回给我，不需要额外的回复，下面是markdown内容"""
    prompt = f"{section_content}"
    response = llm(system_prompt, prompt)
    return response

def make_main_latex(template, section_content):
    system_prompt = template+r"""阅读上面的latex模板，请将以下markdown内容中的作者，标题，单位等内容转换为latex代码，保持原始的语言，随后在正文的\begin{document}中使用\input{Introduction}等形式插入其他章节，章节子文件我已经准备好，你只需要按照章节进行插入即可，参考文献不需要转换，只需要在文件中插入对bib的引用即可，我希望你返回给我的文件可以直接运行编译，直接将转换的结果返回给我，不需要额外的回复，下面是markdown内容"""
    prompt = f"{section_content}"
    response = llm(system_prompt, prompt)
    # 替换```latex和```为一个空字符串
    response = response.replace("```latex", "").replace("```", "")
    return response

def process_bib_agent(section_content):
    """
    处理参考文献的函数
    :param section_content: 参考文献内容
    :return: 处理后的参考文献内容
    """
    system_prompt = """请根据以下文本内容，提取出所有的参考文献的论文题目，并且按照顺序，将结果以json的形式返回给我，，不需要额外的回复，直接返回结果格式样例为{"num_of_ref": 3, "title": ["Attention is all you need", "Segment anything"...]}，其中title为参考文献标题的列表，下面是全文内容"""
    prompt = f"{section_content}"
    response = llm(system_prompt, prompt)
    response = response.replace("```json", "").replace("```", "")
    response = json.loads(response)
    return response
