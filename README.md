# Study
学习


# 批量图片处理器

此脚本用于处理指定文件夹中的图片，执行以下操作：
1. 将图片名称转换为大写。
2. 将每张图片复制两次，分别命名为缩略图和艺术图。
3. 裁剪图片的右侧部分并保存为海报。
4. 处理完成后删除原始图片。

## 功能

- 批量处理指定文件夹中的所有支持的图片（.jpg, .jpeg, .png）。
- 将图片名称转换为大写。
- 为每张图片创建两个副本，带有特定的后缀。
- 裁剪图片的右侧部分到指定尺寸，并保存为海报。
- 处理完成后删除原始图片。

## 环境要求

- Python 3.x
- Pillow 库

## 安装

1. 确保系统已安装 Python 3.x。
2. 安装 Pillow 库（如果尚未安装）：

```bash
pip install pillow
```

## 使用方法
  1、将脚本 batch_image_processor.py 放置在系统上的一个方便位置。
  2、更新脚本中的 folder_path 变量，指向包含要处理图片的文件夹。例如：

```python
folder_path = r"C:\Users\Lenovo\Desktop\新建文件夹"
```
  3、运行脚本：

```
python batch_image_processor.py
```

## 示例
如果文件夹中包含名为 dnjr-125.jpg 的图片，脚本将：

1、将图片重命名为 DNJR-125.jpg。
2、创建两个副本：DNJR-125-thumb.jpg 和 DNJR-125-fanart.jpg。
3、裁剪图片的右侧部分，并保存为 DNJR-125-poster.jpg。
4、删除原始的 dnjr-125.jpg。

## 注意事项
裁剪尺寸固定为 379x538 像素。
脚本假设所有图片的宽度至少为 379 像素，高度至少为 538 像素。

