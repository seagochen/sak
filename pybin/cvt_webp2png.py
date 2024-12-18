import os
import sys
from PIL import Image

def webp_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.webp'):
            webp_file = os.path.join(folder_path, filename)
            png_file = os.path.splitext(webp_file)[0] + '.png'
            try:
                with Image.open(webp_file) as img:
                    img.save(png_file, 'PNG')
                print(f"已转换：{png_file}")
            except Exception as e:
                print(f"转换文件 {webp_file} 时出错：{e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python webp_to_png.py <文件夹路径>")
        sys.exit(1)
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"文件夹 {folder_path} 不存在。")
        sys.exit(1)
    webp_to_png(folder_path)

