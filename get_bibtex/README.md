# Get Bibtex from Google Scholar

本工具用于批量从 Google Scholar 或 dblp 获取参考文献的 Bibtex，支持自动化检索和格式化，极大提升文献管理效率。项目包含 Python 脚本和浏览器插件两种方式，适用于不同场景。

> 特别感谢 https://github.com/IoTS-P/Get-Bibtex-from-Google-Scholar 项目的 bibtex 提取工具，为本项目提供了重要参考和技术支持。

## 项目结构与模块说明

- `process_words_to_bibtex.py`：主脚本，负责读取关键词、自动检索 Google Scholar/dblp 并提取 Bibtex，支持代理设置。
- `global_settings.py`：全局配置文件，包含检索方式、Cookie、代理等参数设置，可灵活扩展支持更多检索网站。
- `imgs/`：存放获取 Cookie 的操作截图等辅助图片。
- `main.js`：浏览器插件脚本，实现选中文本后自动在 dblp 检索并复制 Bibtex 到剪切板。
- `done.txt`：记录已检索过的关键词，避免重复处理。
- `words.txt`：待检索的关键词列表，每行一个。
- `result_bibtex.txt`：批量检索得到的 Bibtex 结果。
- `result_cite.txt`：批量检索得到的 LaTeX 引用格式（如 \cite{xxx}）。

## 1. Python 批量获取 Bibtex

支持从 Google Scholar 或 dblp 批量检索关键词，自动获取第一个搜索结果的 Bibtex。

### 使用方法

1. 在 `words.txt` 中添加待检索关键词，每行一个。
2. （可选）访问 [Google Scholar](https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q=1&btnG=) 获取 Cookie，将 Cookie 填入 `global_settings.py` 的 `headers['Cookie']`。
3. 运行 `process_words_to_bibtex.py`。
4. 检查 `result_bibtex.txt` 和 `result_cite.txt` 获取结果。
5. 如需代理访问，可在 `process_words_to_bibtex.py` 启用 `set_proxy` 并配置代理。

> Google Scholar 检索可能遇到人机验证，需在浏览器手动通过验证并更新 Cookie。

### 配置说明

- 支持自定义检索网站，可在 `global_settings.py` 添加更多 `searchUrlBases`。
- 可切换检索方式（Google Scholar/dblp），修改 `searchWay`。
- 支持代理访问，设置 `proxy_related` 并配置 `set_proxy`。

### 示例流程

- 输入：`words.txt` 添加关键词，`done.txt` 记录已处理。
- 输出：`result_bibtex.txt` 生成 Bibtex，`result_cite.txt` 生成 LaTeX 引用。

## 2. 浏览器插件获取 Bibtex

通过油猴插件，选中文本后自动在 dblp 检索并复制第一个 Bibtex 到剪切板。

### 使用方法

1. 安装油猴插件（参考 [安装视频](https://www.bilibili.com/video/BV1AN4y1Y7mo)）。
2. 通过 Greasy Fork 安装脚本：[选择文本并自动获取BibTex到剪切板](https://greasyfork.org/zh-CN/scripts/522825-%E9%80%89%E6%8B%A9%E6%96%87%E6%9C%AC%E5%B9%B6%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96bibtex%E5%88%B0%E5%89%AA%E5%88%87%E6%9D%BF)。
3. 选中文本后，页面左下角出现按钮，点击即可自动检索并复制 Bibtex。

## 可扩展功能

- [x] 浏览器插件支持选中关键词右键获取 Bibtex。
- [ ] words_from_pdf：从 PDF 文献中提取参考文献列表作为关键词。
- [ ] words_from_doc：从 Word 文档中提取参考文献列表作为关键词。
- [ ] cite_to_bibtex：将文本中的索引号自动转为 LaTeX Bibtex 引用（如 `[6]` 变为 `\cite{xxx}`）。

## 致谢

本项目参考并部分复用了 [Get-Bibtex-from-Google-Scholar](https://github.com/IoTS-P/Get-Bibtex-from-Google-Scholar) 的相关代码和思路，感谢原作者的开源贡献。

---
如有建议或问题，欢迎反馈与交流。
