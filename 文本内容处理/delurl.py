import os
import re
"""
删除图片引用image_pattern
"""
def remove_image_references(folder_path):
    # 匹配类似 `![](images/filename.jpg)` 的文本
    image_pattern = r'!\[\]\(images/.*?\)'

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):  # 仅处理 .md 文件
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 使用正则表达式删除匹配的文本
            updated_content = re.sub(image_pattern, '', content)

            # 如果有改动则写回文件
            if content != updated_content:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                print(f"已从文件 {filename} 中删除图片引用。")
            else:
                print(f"文件 {filename} 不包含图片引用。")

# 使用示例：将 'path/to/your/md/folder' 替换为您的文件夹路径
folder_path = "乐晴"
remove_image_references(folder_path)
