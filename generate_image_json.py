import os
import json

def generate_image_json(root_dir, output_file):
    images = []
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif')

    for dirpath, dirnames, filenames in os.walk(root_dir):
        i = 0
        for filename in filenames:
            i += 1
            if filename.lower().endswith(supported_formats):
                # 获取相对路径
                relative_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
                # 使用父文件夹名称作为类别
                category = os.path.basename(os.path.dirname(relative_path))
                
                category, price = category.split("_")
                
                image_info = {
                    "src": "images/" + relative_path.replace('\\', '/'),  # 确保路径使用正斜杠
                    "category": category,
                    "price": price if i == 1 else ""
                }
                images.append(image_info)

    # 将数据写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(images, f, ensure_ascii=False, indent=2)

    print(f"已生成 {output_file}，包含 {len(images)} 张图片的信息。")

# 使用示例
root_directory = "images"  # 替换为您的图片根目录
output_json_file = "images.json"  # 输出的JSON文件名

generate_image_json(root_directory, output_json_file)