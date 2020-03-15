import tkinter as tk
from tkinter import filedialog
import output as out
import sys
from result import Result
def Response():
    '''打开选择文件夹对话框'''
    root = tk.Tk()
    root.withdraw()

    Filepath = filedialog.askopenfilename() #获得选择好的文件
    # print('Folderpath:',Folderpath)
    print('Filepath:',Filepath)
    data_list = out.count(Filepath)
    print(data_list)
    Result(data_list,Filepath)
    sys.exit()

