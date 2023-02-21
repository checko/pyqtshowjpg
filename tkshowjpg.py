import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# 创建窗口
root = tk.Tk()
root.title("Show JPG File")

# 创建画布
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# 定义图片变量和路径变量
image = None
image_path = None

# 定义打开文件的函数
def open_file():
    global image, image_path
    # 选择文件并获取路径
    image_path = filedialog.askopenfilename(filetypes=[("JPG files", "*.jpg")])
    # 如果路径不为空，打开图片并显示在画布上
    if image_path:
        # 打开图片并转换为 PhotoImage 对象
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        # 在画布上创建图片对象，并保存引用以防被垃圾回收器删除
        canvas.image = photo 
        canvas.create_image(0, 0, anchor="nw", image=photo)
        
# 定义缩放窗口的函数        
def resize_window(event):
    global image, image_path
    # 如果图片和路径不为空，重新打开图片并调整大小为窗口大小，并显示在画布上
    if image and image_path:
        # 获取窗口宽度和高度，并转换为整数类型
        width = int(root.winfo_width())
        height = int(root.winfo_height())
        # 打开图片并调整大小为窗口大小，并转换为 PhotoImage 对象 
        resized_image = Image.open(image_path).resize((width, height))
        resized_photo = ImageTk.PhotoImage(resized_image)
        # 在画布上创建图片对象，并保存引用以防被垃圾回收器删除 
        canvas.resized_image = resized_photo 
        canvas.create_image(0, 0, anchor="nw", image=resized_photo)

# 创建按钮，绑定打开文件的函数        
button = tk.Button(root, text="Open JPG File", command=open_file)
button.pack()

# 绑定窗口配置事件，触发缩放窗口的函数 
root.bind("<Configure>", resize_window)

# 启动主循环    
root.mainloop()