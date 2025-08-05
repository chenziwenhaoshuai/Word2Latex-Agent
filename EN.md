# Word2Latex Agent

## Project Overview

Word2Latex Agent is an intelligent tool powered by Large Language Models (LLMs) designed to automatically convert Word documents into standard LaTeX formats for specific journals and conferences. Through Agent technology, it supports automatic processing and formatting of sections, images, tables, references, and other content, significantly improving the efficiency of paper format conversion.

This project adopts a modular design, integrating document parsing, content conversion, reference processing, and other functions, supporting LaTeX templates for mainstream journals and conferences.

## Key Features

- **Intelligent Document Parsing**: Automatically extract sections, text, images, tables, and other content from Word documents
- **Automatic Format Conversion**: Convert Markdown content to journal-compliant LaTeX format using AI
- **Image and Table Processing**: Automatically extract and insert images with appropriate layout formatting
- **Reference Management**: Intelligently identify references and automatically generate BibTeX files
- **Template Adaptation**: Support multiple journal/conference LaTeX templates (e.g., Elsevier)
- **Batch Processing**: Support section separation and batch format conversion

## Project Structure and Module Functions

```
word2Latex_agent/
├── main.py                    # Main program entry, controls overall conversion process
├── agent.py                   # Core AI Agent module for content understanding and format conversion
├── process_doc.py             # Document processing module for DOCX to Markdown conversion
├── ref2bib.py                 # Reference processing module, calls bibtex extraction tools
├── 123.py                     # Auxiliary test script
├── README.md                  # Project documentation (Chinese)
├── README_EN.md               # Project documentation (English)
├── temp/                      # Temporary files directory
│   ├── main.tex              # Generated main LaTeX file
│   ├── *.tex                 # Section LaTeX files
│   ├── bibtex.bib            # Reference BibTeX file
│   └── ...                   # Other temporary files
├── elsarticle/               # Elsevier journal LaTeX templates
│   ├── elsarticle-template-*.tex  # Template files for different styles
│   ├── *.bst                 # Reference style files
│   └── doc/                  # Template documentation and examples
├── get_bibtex/               # BibTeX extraction tool module
│   ├── process_words_to_bibtex.py  # Get BibTeX from Google Scholar/DBLP
│   ├── global_settings.py    # Global configuration file
│   ├── main.js               # Browser extension script
│   └── README.md             # Detailed usage instructions
└── media/                    # Image resources directory
    └── *.png                 # Images extracted from Word documents
```

### Detailed Module Descriptions

#### 1. main.py - Main Control Module
- **Function**: Coordinates the entire conversion process with step-by-step execution support
- **Main Steps**:
  - Step 1: DOCX → Markdown conversion with media extraction
  - Step 2: Section analysis, template reading, main file generation, reference processing
  - Step 3: Section-by-section content extraction
  - Step 4: Section content LaTeX format conversion
  - Step 5: Result file organization

#### 2. agent.py - AI Intelligent Conversion Module
- **Function**: Content understanding and format conversion based on Large Language Models
- **Core Functions**:
  - `paper_split_agent()`: Intelligent section separation
  - `get_total_sections_agent()`: Section structure analysis
  - `convert_markdown_to_latex_agent()`: Markdown to LaTeX conversion
  - `make_main_latex()`: Main LaTeX file generation
  - `process_bib_agent()`: Intelligent reference processing

#### 3. process_doc.py - Document Processing Module
- **Function**: Calls Pandoc to convert DOCX to Markdown
- **Features**:
  - Automatically extract images from documents to specified directory
  - Maintain document structure and format information
  - Support conversion of complex content like formulas and tables

#### 4. ref2bib.py - Reference Processing Module
- **Function**: Integrates get_bibtex tools for automated reference processing
- **Process**: Extract references from Markdown → Call search tools → Generate BibTeX files

#### 5. get_bibtex/ - BibTeX Extraction Tool
- **Source**: Based on [Get-Bibtex-from-Google-Scholar](https://github.com/IoTS-P/Get-Bibtex-from-Google-Scholar) project
- **Function**: Automatically obtain BibTeX format references from academic databases like Google Scholar and DBLP
- **Support Methods**: Python script batch processing + browser extension real-time acquisition

## Installation and Environment Setup

### System Requirements
- Python 3.7+
- Windows/Linux/macOS
- Internet connection (for AI services and reference retrieval)

### Dependencies Installation

1. **Install Pandoc**:
   ```bash
   # Windows: Download and install pandoc-3.7.0.2-windows-x86_64.msi
   # Linux: sudo apt-get install pandoc
   # macOS: brew install pandoc
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install python-docx openai requests beautifulsoup4
   ```

3. **Configure API Keys**:
   - Configure your AI service API Key in `agent.py`
   - Configure Google Scholar Cookie in `get_bibtex/global_settings.py` (optional)

## Usage Instructions

### Basic Usage Workflow

1. **Prepare Document**: Place the Word document to be converted in the project root directory

2. **Modify Configuration**: Set document path and template file in `main.py`:
   ```python
   docx_file = r'your_document.docx'
   latex_template_file = "elsarticle/elsarticle-template-num-names.tex"
   ```

3. **Run Conversion**:
   ```bash
   python main.py
   ```

4. **Get Results**: Obtain from `temp/` directory:
   - `main.tex`: Main LaTeX file
   - `{section_name}.tex`: Section LaTeX files
   - `bibtex.bib`: Reference BibTeX file
   - `media/`: Extracted image files

5. **Compile LaTeX**: Use target journal LaTeX template for compilation

### Advanced Configuration

- **Step-by-step Execution**: Control which steps to execute in the `steps_to_run` dictionary in `main.py`
- **Template Switching**: Modify `latex_template_file` variable to select different journal templates
- **AI Model Configuration**: Choose different language models in `agent.py`



## Acknowledgments

The reference processing functionality of this project is based on the excellent open source project:
- **[Get-Bibtex-from-Google-Scholar](https://github.com/IoTS-P/Get-Bibtex-from-Google-Scholar)**: Provides powerful automatic BibTeX acquisition tools, supporting batch retrieval of references from academic databases like Google Scholar and DBLP, greatly improving literature management efficiency.

Thanks to the open source community's contributions, making academic tool development more convenient and efficient.


