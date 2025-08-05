import subprocess
import os

def docx_to_md_with_media(docx_path, media_dir='.'):
    """
    调用pandoc将docx文档转换为md文件，并提取图片到指定目录
    """
    md_path = os.path.splitext(docx_path)[0] + '.md'
    cmd = [
        'pandoc',
        '-s',
        docx_path,
        f'--extract-media={media_dir}',
        '-o',
        md_path
    ]
    subprocess.run(cmd, check=True)
    return md_path

if __name__ == '__main__':
    docx_path = r'G:\project\word2Latex_agent\TBFormer-V8.docx'
    md_path = r'G:\project\word2Latex_agent\TBFormer-V8.md'
    fig_dir = r'G:\project\word2Latex_agent'
    print('开始处理文档...')
    try:
        docx_to_md_with_media(docx_path, md_path, fig_dir)
        print('处理完成，md和图片已保存。')
    except Exception as e:
        print(f'处理失败: {e}')
