import tkinter as tk
import sys
from response import Response
def Window():
    """打开窗口，选择文件"""
    root = tk.Tk()
    root.title("选择文件")
    root.geometry("300x100")
    button = tk.Button(root, text='浏览文件', relief=tk.RAISED,command=Response)
    button.place(x=100, y=20, width=100, height=50)
    root.mainloop()
    sys.exit()
