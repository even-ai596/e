import os
import re

def edit_md_files(folder_path):
    try:
        # 获取文件夹中的所有 .md 文件
        md_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.md')]

        if not md_files:
            print("错误：文件夹中没有 .md 文件。")
            return

        print(f"找到以下 .md 文件：{md_files}")

        # 遍历每个 .md 文件并进行编辑
        for md_file in md_files:
            md_path = os.path.join(folder_path, md_file)

            try:
                # 读取文件内容
                with open(md_path, 'r', encoding='utf-8') as file:
                    content = file.readlines()

                # 编辑内容
                edited_content = []
                for line in content:
                    # 匹配 "一、二、三..." 开头的行并添加一级标题
                    if re.match(r'^[一二三四五六七八九十]+、', line.strip()):
                        edited_content.append(f"# {line}")
                    # 匹配 "1、2、3..." 开头的行并添加二级标题
                    elif re.match(r'^\d+、', line.strip()):
                        edited_content.append(f"## {line}")
                    else:
                        edited_content.append(line)
                                                    
                # 将修改后的内容写回文件
                with open(md_path, 'w', encoding='utf-8') as file:
                    file.writelines(edited_content)

                print(f"已编辑文件：{md_file}")

            except Exception as e:
                print(f"处理文件 {md_file} 时出错：{e}")

    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法
if __name__ == "__main__":
    folder_path = r"智研"  # 替换为包含 .md 文件的文件夹路径
    edit_md_files(folder_path)