import os
def getfile():
    """处理目录下符合条件的文件，返回文件名"""
    g = os.walk(r"C:\Users\荣\PycharmProjects\homework")
    files = []
    for path,d,filelist in g:
        for filename in filelist:
            if filename.endswith('.c'):
                files.append(filename)
    return files
