import os
import shutil
from PIL import Image

# 图片文件夹路径
folder_path = r"C:\Users\Lenovo\Desktop\新建文件夹"

# 支持的图片扩展名
supported_extensions = ['.jpg', '.jpeg', '.png']

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否为支持的图片格式
    if os.path.splitext(filename)[1].lower() in supported_extensions:
        original_image_path = os.path.join(folder_path, filename)
        original_name = os.path.splitext(filename)[0].upper()  # 将原始名称转换为大写

        # 定义新文件的路径
        thumb_image_path = os.path.join(folder_path, f"{original_name}-thumb.jpg")
        fanart_image_path = os.path.join(folder_path, f"{original_name}-fanart.jpg")
        poster_image_path = os.path.join(folder_path, f"{original_name}-poster.jpg")

        # 复制图片并重命名
        shutil.copyfile(original_image_path, thumb_image_path)
        shutil.copyfile(original_image_path, fanart_image_path)

        # 打开原始图片进行裁剪
        with Image.open(original_image_path) as img:
            # 图片原始尺寸
            width, height = img.size
            
            # 计算需要保留的区域 (裁剪右边部分)
            left = width - 379
            top = 0
            right = width
            bottom = 538
            
            # 裁剪图片
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img.save(poster_image_path)

        # 删除原始图片
        os.remove(original_image_path)

        print(f"处理完成并删除原始图片：{filename}")
        print(f"生成的文件：{thumb_image_path}, {fanart_image_path}, {poster_image_path}")

print("所有图片处理完成。")
