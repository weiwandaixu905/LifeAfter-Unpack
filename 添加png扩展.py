# 导入os模块，用于操作文件和文件夹
import os

# 定义一个函数，用于检查文件的前16个字节中是否有89 50 4E 47这四个十六进制数
def check_file_type(file):
    # 以二进制模式打开文件
    with open(file, "rb") as f:
        # 读取文件的前16个字节
        data = f.read(16)
        # 将字节转换为十六进制字符串
        hex_data = data.hex()
        # 检查是否包含89 50 4E 47
        if "89504e47" in hex_data:
            # 如果包含，返回True
            return True
        else:
            # 如果不包含，返回False
            return False

# 定义一个函数，用于检查文件是否已经是.png后缀
def check_file_extension(file):
    # 获取文件的后缀名
    ext = os.path.splitext(file)[1]
    # 检查是否是.png
    if ext == ".png":
        # 如果是，返回True
        return True
    else:
        # 如果不是，返回False
        return False

# 定义一个文件夹的路径，这里假设是当前目录下的test文件夹
folder_path = input("请输入文件夹路径：")

# 遍历文件夹中的所有文件
for file in os.listdir(folder_path):
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, file)
    # 检查文件是否已经是.png后缀
    if check_file_extension(file_path):
        # 如果是，跳过该文件，不做任何操作
        continue
    # 如果不是，再检查文件是否符合条件
    elif check_file_type(file_path):
        # 如果符合条件，给文件添加.png后缀
        new_file_path = file_path + ".png"
        # 重命名文件
        os.rename(file_path, new_file_path)
        # 打印一条信息，显示文件已经被修改
        print(f"文件{file}已经被修改为{new_file_path}")
