import os
"""
删除指定内容copyright_text
"""
def remove_copyright_text(folder_path):
    # 要删除的具体版权信息
    copyright_text = "文章转载、引用说明：\n智研咨询推崇信息资源共享，欢迎各大媒体和行研机构转载引用。但请遵守如下规则：\n1.可全文转载，但不得恶意镜像。转载需注明来源智研咨询。\n2.转载文章内容时不得进行删减或修改。图表和数据可以引用，但不能去除水印和数据来源。\n如有违反以上规则，我们将保留追究法律责任的权力。\n版权提示：\n智研咨询倡导尊重与保护知识产权，对有明确来源的内容注明出处。如发现本站文章存在版权、稿酬或其它问题，烦请联系我们，我们将及时与您沟通处理。联系方式：gaojianchyxx.com、010-60343812。\nCopyright2008-2024北京智研科信咨询有限公司Allrightsreserved.京ICP备13007370号-1京公网安备11011102001993号\n增值电信业务经营许可证：京B2-20224504"
    # copyright_text = "资料来源：公司年报、智研咨询整理"
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):  # 仅处理 .md 文件
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 删除版权信息
            if copyright_text in content:
                content = content.replace(copyright_text, '')
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"版权信息已从文件 {filename} 中删除。")
            else:
                print(f"文件 {filename} 不包含指定版权信息。")

# 使用示例：将 'path/to/your/md/folder' 替换为您的文件夹路径
folder_path = "智研咨询_光伏组件"
remove_copyright_text(folder_path)
