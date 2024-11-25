import os
"""
删除trigger_text及后续内容
"""
def remove_copyright_text(folder_path):
    # 要删除的触发文本
    trigger_text = "以上数据及信息可参考智研咨询"

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):  # 仅处理 .md 文件
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 如果包含触发文本，从触发点删除后续内容
            if trigger_text in content:
                content = content.split(trigger_text)[0]  # 保留触发文本前的内容
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"触发文本及后续内容已从文件 {filename} 中删除。")
            else:
                print(f"文件 {filename} 不包含触发文本。")

# 使用示例：将 'path/to/your/md/folder' 替换为您的文件夹路径
folder_path = "智研咨询_光伏组件"
remove_copyright_text(folder_path)
