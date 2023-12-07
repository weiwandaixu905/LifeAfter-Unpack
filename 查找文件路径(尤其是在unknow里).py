import os
import re
import concurrent.futures

# 修改后的正则表达式，用于匹配文件路径
regex = r"[a-zA-Z0-9_\\\/]+\\[a-zA-Z0-9_]+\.(nxs|fx|png|gim|mesh|mtg|ags|tga|ktx|fev|mp4|gis)"

def process_file(file_path):
    matches_found = set()  # 使用集合来存储匹配结果，自动去除重复项
    try:
        with open(file_path, "rb") as f:
            content = f.read()
            try:
                decoded_content = content.decode('ISO-8859-1')
                matches = re.finditer(regex, decoded_content, re.IGNORECASE)
                for match in matches:
                    matches_found.add(match.group())
            except UnicodeDecodeError:
                matches_found.add("Unable to decode file content")
    except Exception as e:
        matches_found.add(f"Error processing file {file_path}: {e}")

    return file_path, matches_found

def process_files_in_folder(folder_path, output_file):
    all_matches = set()  # 用于存储所有文件的匹配结果，去除重复
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(process_file, os.path.join(root, file)): file for root, dirs, files in os.walk(folder_path) for file in files}
        for future in concurrent.futures.as_completed(future_to_file):
            file_path, matches = future.result()
            all_matches.update(matches)  # 更新集合，自动去除重复项

    with open(output_file, 'w', encoding='utf-8') as out_f:  # 注意这里是'w'模式，因为我们要写入所有去重后的结果
        for match in all_matches:
            out_f.write(match + '\n')

# 调用处理文件夹中文件的函数，并传入文件夹路径和输出文件路径
folder_path = input("请输入文件夹路径：")  # 替换为你的文件夹路径，确保使用原始字符串
output_path = r'matches_output.txt'  # 定义输出文件的路径，确保使用原始字符串
process_files_in_folder(folder_path, output_path)
