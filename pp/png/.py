from PIL import Image
import os

def images_to_pdf(folder_path, output_pdf):
    """
    将指定文件夹中的所有PNG图片转换为一个PDF文件。

    :param folder_path: 包含PNG图片的文件夹路径
    :param output_pdf: 输出的PDF文件名
    """
    # 获取文件夹中所有的PNG文件
    images = [img for img in os.listdir(folder_path) if img.endswith('.png')]
    
    # 按文件名排序图片，如果需要按特定顺序组合，请调整此部分代码
    images.sort()

    # 创建一个列表来保存Image对象
    image_list = []

    # 遍历每个PNG文件
    for image_name in images:
        # 打开图片
        img_path = os.path.join(folder_path, image_name)
        with Image.open(img_path) as img:
            # 转换为RGB模式，因为PDF不支持RGBA或P模式
            img = img.convert('RGB')
            # 添加到列表
            image_list.append(img)

    # 如果列表中有图片，则保存为PDF
    if image_list:
        # 第一张图片作为PDF的第一页，其余的作为后续页
        first_image = image_list.pop(0)
        first_image.save(output_pdf, save_all=True, append_images=image_list)
        print(f"PDF文件已创建：{output_pdf}")
    else:
        print("没有找到任何PNG图片")

# 使用示例
folder_path = 'pp/png'  # 替换为你的文件夹路径
output_pdf = 'pp/dpf/output.pdf'  # 输出的PDF文件名
images_to_pdf(folder_path, output_pdf)