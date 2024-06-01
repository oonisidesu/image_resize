import os
from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)
        print(f"Image saved to {output_path}")

def resize_images_in_folder(input_folder, output_folder, size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, size)

# 入力フォルダのパス
input_folder = "/input"  # ここに実際の入力フォルダのパスを指定
# 出力フォルダのパス
output_folder = "/output"  # ここに実際の出力フォルダのパスを指定
# 目標のサイズ (幅, 高さ)
size = (60, 90)

# フォルダ内のすべての画像をリサイズ
resize_images_in_folder(input_folder, output_folder, size)