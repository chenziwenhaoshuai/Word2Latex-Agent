import os
from process_doc import *
from agent import *
from ref2bib import *
import shutil

if __name__ == '__main__':
    docx_file = r'./TBFormer-V8.docx'
    latex_template_file = "./elsarticle/elsarticle-template-num-names.tex"
    latex_temp_path = "./temp"
    # makedir
    os.makedirs(latex_temp_path, exist_ok=True)

    # 添加步骤选择条件测试
    steps_to_run = {
        "step1": 1,  # 转换DOCX到Markdown
        "step2_1": 1,  # 获取Markdown文件的总章节
        "step2_2": 1,  # 读取LaTeX模板
        "step2_3": 1,  # 制作LaTeX主文件
        "step2_4": 1,  # 处理参考文献
        "step3": 1,  # 提取每个章节
        "step4": 1,  # 转换章节内容到LaTeX
    }

    # Step 1: Convert DOCX to Markdown with media extraction
    if steps_to_run["step1"]:
        print("Converting DOCX to Markdown with media extraction...")
        md_file = docx_to_md_with_media(docx_file)
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

    # Step 2.1: get total section of markdown file
    if steps_to_run["step2_1"]:
        print("Getting total sections of Markdown file...")
        total_sections = get_total_sections_agent(md_content)
        print("Total Sections:", total_sections)

    # Step 2.2: Read latex template
    if steps_to_run["step2_2"]:
        print("Reading LaTeX template...")
        with open(latex_template_file, 'r', encoding='utf-8') as f:
            latex_template = f.read()
            Clear_latex_template = clear_latex_template_agent(latex_template)

    # Step 2.3: Make latex head
    if steps_to_run["step2_3"]:
        print("Making main LaTeX template...")
        Latex_header = make_main_latex(latex_template, md_content)
        with open(latex_temp_path + '/main.tex', 'w', encoding='utf-8') as f:
            f.write(Latex_header)

    # Step 2.4: Process bib
    if steps_to_run["step2_4"]:
        print("Processing bibliography...")
        bib_content = process_bib_agent(md_content)
        with open(latex_temp_path + '/word.txt', 'w', encoding='utf-8') as f:
            for item in bib_content['title']:
                f.write(item + '\n')
        ref2bib(latex_temp_path + '/word.txt',latex_temp_path + '/bibtex.bib',latex_temp_path + '/ref.txt', latex_temp_path + '/done.txt')


    # Step 3: Extract each section
    if steps_to_run["step3"]:
        for section in total_sections:
            print(f"Extracting section: {section}")
            section_content = paper_split_agent(section, md_content)
            print(f"Section {section} content extracted successfully.")

            # Step 4: convert section content to LaTeX
            if steps_to_run["step4"]:
                print("Converting section content to LaTeX...")
                latex_content = convert_markdown_to_latex_agent(latex_template, section_content)
                # replace```latex and ``` with empty string
                latex_content = latex_content.replace('```latex', '').replace('```', '').strip()
                with open(latex_temp_path+'/'+section+'.tex', 'w', encoding='utf-8') as f:
                    f.write(latex_content)

    # Step 5: copy .bib and .tex files to result directory, do not copy .txt files
    if steps_to_run["step_5"]:
        result_dir = './result'
        os.makedirs(result_dir, exist_ok=True)
        for file_name in os.listdir(latex_temp_path):
            if file_name.endswith('.tex') or file_name.endswith('.bib'):
                src_file = os.path.join(latex_temp_path, file_name)
                dst_file = os.path.join(result_dir, file_name)
                shutil.copy(src_file, dst_file)
        print("All files copied to result directory.")

