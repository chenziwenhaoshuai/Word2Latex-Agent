# Word2Latex Agent

## 项目简介

Word2Latex Agent 是一个基于大语言模型的智能化工具，旨在将 Word 文档内容自动转换为指定期刊或会议的标准 LaTeX 格式。通过 Agent 技术，支持章节、图片、表格、参考文献等内容的自动处理和格式化，极大提升论文格式转换效率。

本项目采用模块化设计，集成了文档解析、内容转换、参考文献处理等功能，支持主流期刊会议的 LaTeX 模板。

## 主要功能

- **智能文档解析**：自动从 Word 文档提取章节、正文、图片、表格等内容
- **格式自动转换**：基于 AI 将 Markdown 内容转换为符合期刊要求的 LaTeX 格式
- **图片表格处理**：自动提取并插入图片，设置合适的排版格式
- **参考文献管理**：智能识别参考文献并自动生成 BibTeX 文件
- **模板适配**：支持多种期刊/会议 LaTeX 模板（如 Elsevier）
- **批量处理**：支持章节分离和批量格式转换

## 项目结构与模块功能

```
word2Latex_agent/
├── main.py                    # 主程序入口，控制整体转换流程
├── agent.py                   # 核心 AI Agent 模块，负责内容理解和格式转换
├── process_doc.py             # 文档处理模块，实现 DOCX 到 Markdown 的转换
├── ref2bib.py                 # 参考文献处理模块，调用 bibtex 提取工具
├── 123.py                     # 辅助测试脚本
├── README.md                  # 项目说明文档
├── temp/                      # 临时文件目录
│   ├── main.tex              # 生成的主 LaTeX 文件
│   ├── *.tex                 # 各章节的 LaTeX 文件
│   ├── bibtex.bib            # 参考文献 BibTeX 文件
│   └── ...                   # 其他临时文件
├── elsarticle/               # Elsevier 期刊 LaTeX 模板
│   ├── elsarticle-template-*.tex  # 不同样式的模板文件
│   ├── *.bst                 # 参考文献样式文件
│   └── doc/                  # 模板文档和示例
├── get_bibtex/               # BibTeX 提取工具模块
│   ├── process_words_to_bibtex.py  # 从 Google Scholar/DBLP 获取 BibTeX
│   ├── global_settings.py    # 全局配置文件
│   ├── main.js               # 浏览器插件脚本
│   └── README.md             # 详细使用说明
└── media/                    # 图片资源目录
    └── *.png                 # 从 Word 文档提取的图片
```

### 核心模块详细说明

#### 1. main.py - 主控制模块
- **功能**：协调整个转换流程，支持分步骤执行
- **主要步骤**：
  - Step 1: DOCX → Markdown 转换并提取媒体文件
  - Step 2: 章节分析、模板读取、主文件生成、参考文献处理
  - Step 3: 逐章节内容提取
  - Step 4: 章节内容 LaTeX 格式转换
  - Step 5: 结果文件整理

#### 2. agent.py - AI 智能转换模块
- **功能**：基于大语言模型的内容理解和格式转换
- **核心函数**：
  - `paper_split_agent()`: 智能章节分离
  - `get_total_sections_agent()`: 章节结构分析
  - `convert_markdown_to_latex_agent()`: Markdown 到 LaTeX 转换
  - `make_main_latex()`: 主 LaTeX 文件生成
  - `process_bib_agent()`: 参考文献智能处理

#### 3. process_doc.py - 文档处理模块
- **功能**：调用 Pandoc 实现 DOCX 到 Markdown 的转换
- **特性**：
  - 自动提取文档中的图片到指定目录
  - 保持文档结构和格式信息
  - 支持公式、表格等复杂内容的转换

#### 4. ref2bib.py - 参考文献处理模块
- **功能**：整合 get_bibtex 工具，实现参考文献的自动化处理
- **流程**：从 Markdown 提取参考文献 → 调用检索工具 → 生成 BibTeX 文件

#### 5. get_bibtex/ - BibTeX 提取工具
- **来源**：基于 [Get-Bibtex-from-Google-Scholar](https://github.com/IoTS-P/Get-Bibtex-from-Google-Scholar) 项目
- **功能**：从 Google Scholar、DBLP 等学术数据库自动获取参考文献的 BibTeX 格式
- **支持方式**：Python 脚本批量处理 + 浏览器插件实时获取

## 安装与环境配置

### 系统要求
- Python 3.7+
- Windows/Linux/macOS
- 网络连接（用于 AI 服务和参考文献检索）

### 依赖安装

1. **安装 Pandoc**：
   ```bash
   # Windows: 下载并安装 pandoc-3.7.0.2-windows-x86_64.msi
   # Linux: sudo apt-get install pandoc
   # macOS: brew install pandoc
   ```

2. **安装 Python 依赖**：
   ```bash
   pip install python-docx openai requests beautifulsoup4
   ```

3. **配置 API 密钥**：
   - 在 `agent.py` 中配置你的 AI 服务 API Key
   - 在 `get_bibtex/global_settings.py` 中配置 Google Scholar Cookie（可选）

## 使用方法

### 基本使用流程

1. **准备文档**：将待转换的 Word 文档放入项目根目录

2. **修改配置**：在 `main.py` 中设置文档路径和模板文件：
   ```python
   docx_file = r'your_document.docx'
   latex_template_file = "elsarticle/elsarticle-template-num-names.tex"
   ```

3. **运行转换**：
   ```bash
   python main.py
   ```

4. **获取结果**：在 `temp/` 目录下获取：
   - `main.tex`：主 LaTeX 文件
   - `{章节名}.tex`：各章节 LaTeX 文件
   - `bibtex.bib`：参考文献 BibTeX 文件
   - `media/`：提取的图片文件

5. **编译 LaTeX**：使用目标期刊的 LaTeX 模板进行编译

### 高级配置

- **分步执行**：在 `main.py` 中的 `steps_to_run` 字典中控制执行哪些步骤
- **模板切换**：修改 `latex_template_file` 变量选择不同的期刊模板
- **AI 模型配置**：在 `agent.py` 中选择不同的语言模型


## 致谢

本项目的参考文献处理功能基于优秀的开源项目：
- **[Get-Bibtex-from-Google-Scholar](https://github.com/IoTS-P/Get-Bibtex-from-Google-Scholar)**：提供了强大的 BibTeX 自动获取工具，支持从 Google Scholar、DBLP 等学术数据库批量获取参考文献，极大提升了文献管理效率。


