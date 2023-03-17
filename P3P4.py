import hashlib
from tkinter import *
from tkinter import filedialog

# 创建一个Tkinter窗口
root = Tk()
root.title ('P3P P4G校验和修正') #程序标题
root.resizable(0,0)           #程序不可缩放
root.attributes("-topmost",0) #程序置顶
kuan = 400                       #程序宽度
gao = 270                         #程序高度

#获取分辨率的宽度赋值给fkuan
fkuan=root.winfo_screenwidth()

#获取分辨率的高度赋值给fgao
fgao=root.winfo_screenheight()

#设定程序打开时的位置在屏幕正中间
weizhi='%dx%d+%d+%d' %(kuan,gao,(fkuan-kuan)/2,(fgao-gao)/2)
#主程序输出位置
root.geometry(weizhi)

# 定义选择文件按钮的回调函数
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # 将选择的文件路径显示在标签中
        file_path_entry.delete(0, END)
        file_path_entry.insert(0, file_path)
        result_entry.delete(0, END)

# 定义加密文件按钮的回调函数
def encrypt_file():
    # 获取要加密的文件路径
    file_path = file_path_entry.get()
    if file_path:
        # 打开文件并读取数据
        with open(file_path, 'rb') as file:
            #读取整个文件
            file_data = file.read()

        # 使用hashlib模块中的md5函数对文件数据进行加密
        hash_md5 = hashlib.md5(file_data)

        # 获取加密后的摘要值并输出
        encrypted = hash_md5.hexdigest()
        result_entry.delete(0, END)
        result_entry.insert(0, encrypted)

# 这个回调函数获取要写入的list文件
def Hash_file():
    # 获取要写入MD5的文件路径
    list_path_hash = filedialog.askopenfilename()
    if list_path_hash:
        # 将选择的文件路径显示在标签中
        list_path_entry.delete(0, END)
        list_path_entry.insert(0, list_path_hash)

def Hash_write():
    hash_path = list_path_entry.get()
    if hash_path:
        with open (hash_path,'r+b') as hash:
            md5 = result_entry.get()
            hash.seek(0x18)
            hash.write(bytes.fromhex(md5))
            result_label = Label(root, text="CheckSum修正成功")
            result_label.pack()




# 创建选择文件按钮和标签
browse_button = Button(root, text="选择bin文件", command=browse_file)
browse_button.pack()
file_path_entry = Entry(root, width=50)
file_path_entry.pack()

# 创建加密文件按钮
encrypt_button = Button(root, text="获取CheckSum", command=encrypt_file)
encrypt_button.pack()
result_entry = Entry(root, width=50)
result_entry.pack()

# 创建选择list文件按钮和标签
browse_button = Button(root, text="选择slot文件", command=Hash_file)
browse_button.pack()
list_path_entry = Entry(root, width=50)
list_path_entry.pack()

#写入按钮
Hash_write_button = Button (root, text="写入MD5到slot文件", command=Hash_write)
Hash_write_button.pack()
hash_entry = Label (root, width=50)
hash_entry.pack()

# 启动Tkinter窗口
root.mainloop()