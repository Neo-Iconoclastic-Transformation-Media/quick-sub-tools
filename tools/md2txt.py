import re

def process_markdown_file(input_file, output_file):
    """
    参数:
    input_file (str): Markdown 文件的路径
    output_file (str): 输出 .txt 文件的路径
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 删除所有标题
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
    
    # 删除所有换行符
    content = content.replace('\n', '')
    
    # 替换中文逗号和句号为换行符
    content = re.sub(r'[，。]', '\n', content)

    # 在感叹号、问号、省略号之后添加换行符
    specPuct = r'[！？…]'
    content = re.sub(specPuct, r'\g<0>\n',content)
    
    # 替换顿号为空格
    content = content.replace('、', ' ')
    
    # 输出到 .txt 文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    input_file = input("请输入 Markdown 文件的路径: ")
    output_file = input("请输入输出 .txt 文件的路径: ")
    
    # 检查输出文件路径是否以 .txt 结尾
    if not output_file.endswith('.txt'):
        output_file += '.txt'
    
    process_markdown_file(input_file, output_file)
    print(f"文件 '{output_file}' 已生成。")
