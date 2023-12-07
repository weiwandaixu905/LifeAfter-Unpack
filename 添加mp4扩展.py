import os

# 定义一个函数，用于检查文件的前16个字节中是否有abcd
def check_ftypisom(file):
    # 打开文件，读取前16个字节
    with open(file, "rb") as f:
        data = f.read(16)
    # 如果前16个字节中有abcd，返回True，否则返回False
    if b"ftypisom" in data:
        return True
    else:
        return False

# 定义一个函数，用于检查文件是否已经是.abcd后缀

def check_suffix(file):
    # 获取文件的扩展名
    ext = os.path.splitext(file)[1]
    # 如果扩展名是.mp4，返回True，否则返回False
    if ext == ".mp4":
        return True
    else:
        return False

# 定义一个文件夹的路径，这里假设是当前目录下的test文件夹
# 获取文件夹路径
folder_path = input("请输入文件夹路径：")

# 遍历文件夹中的所有文件
for file in os.listdir(folder_path):
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, file)
    # 如果文件是一个普通文件，而不是一个目录
    if os.path.isfile(file_path):
      if not check_suffix(file_path):
            # 如果不是，再调用check_abcd函数，检查文件是否符合条件
        # 调用check_abcd函数，检查文件是否符合条件
        if check_ftypisom(file_path):
            # 如果符合条件，给文件添加abcd后缀
            new_file_path = file_path + ".mp4"
            # 重命名文件
            os.rename(file_path, new_file_path)
            # 打印一条信息，显示文件已经被修改
            print(f"{file_path} 已经被修改 {new_file_path}")
