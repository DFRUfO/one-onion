import tkinter as tk
from  tkinter  import *
import sys
def Result(datas,filename):
    """统计结果窗口"""
    root = tk.Tk()
    root.title("选择文件")
    root.geometry("420x320")

    file_name = tk.Label(root, text='文件名： %s'%filename, justify=tk.RIGHT, width=80)
    line = tk.Label(root, text='行数：  %s'%datas['line'], justify=tk.RIGHT, width=80)
    word = tk.Label(root, text='单词数：  %s'%datas['word'], justify=tk.RIGHT, width=80)
    character = tk.Label(root, text='字符数：  %s' % datas['character'], justify=tk.RIGHT, width=80)
    empty_line = tk.Label(root, text='空行数：  %s' % datas['empty_line'], justify=tk.RIGHT, width=80)
    note_line = tk.Label(root, text='注释行：  %s' % datas['note_line'], justify=tk.RIGHT, width=80)
    code_line = tk.Label(root, text='代码行：  %s' % datas['code_line'], justify=tk.RIGHT, width=80)

    file_name.place(x=50,y=10,width=280,height=30)
    line.place(x=135, y=40, width=100, height=20)
    word.place(x=135, y=85, width=100, height=20)
    character.place(x=135, y=130, width=100, height=20)
    empty_line.place(x=135, y=175, width=100, height=20)
    note_line.place(x=135, y=220, width=100, height=20)
    code_line.place(x=135, y=265, width=100, height=20)

    root.mainloop()
    sys.exit()
