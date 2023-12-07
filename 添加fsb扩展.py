import os

# 获取文件夹路径
folder_path = input("请输入文件夹路径：")

# 遍历文件夹中的每个文件
for file in os.listdir(folder_path):
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, file)
    # 打开文件并读取前三个字节
    with open(file_path, "rb") as f:
        header = f.read(3)
    # 判断文件是否以dds标签开头
    if header == b"FSB":
        # 获取文件的原始后缀
        file_ext = os.path.splitext(file)[1]
        # 如果文件后缀不是dds，就重命名文件
        if file_ext != ".fsb":
            # 生成新的文件名，添加fsb后缀
            new_file = file + ".fsb"
            # 生成新的文件路径
            new_file_path = os.path.join(folder_path, new_file)
            # 重命名文件
            os.rename(file_path, new_file_path)
            # 打印重命名结果
            print(f"已将{file}重命名为{new_file}")
