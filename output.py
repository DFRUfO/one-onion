import re
from get_file import getfile
def Output(command,file_name):
    """选择命令，输出数据"""
    datas = count(file_name)
    if command == '-c':
        export(file_name,"字符数",datas['character'])
    elif command == '-w':
        export(file_name, "单词数", datas['word'])
    elif command == '-l':
        export(file_name, "行数", datas['line'])
        # print('文件名：%s,行数: %d' % (file_name, datas['line']))
    elif command == '-s':  #处理目录下符合条件的文件
        print("\nC:\\Users\\荣\\PycharmProjects\\homework目录下的文件统计：\n")
        recursion()
    elif command == '-a':
        print('\n文件%s下的统计：' % file_name)
        print(datas)
    else:
        print("请输入正确指令")

def export(filename,name,data):
    print('文件名：%s, %s: %d' % (filename,name,data))

def count(file_name):
    """统计文件中的数据"""
    data = {}
    data['line'] = 0
    data['word'] = 0
    data['character'] = 0
    data['empty_line'] = 0 #空行
    data['note_line'] = 0  #注释行
    data['code_line'] = 0 #代码行
    try:
        with open(file_name, 'r', encoding='utf-8')as fi:
            for lines in fi:
                if lines.strip() == '':
                    data['empty_line'] += 1
                    continue
                if '//' in lines:
                    data['note_line'] += 1

                replace = re.subn(r"[#<>,;()""&{}+]"," ",lines) #用空格代替替他符号
                words = replace[0].split()
                data['line'] += 1
                for word in words:
                    if re.match(r".*[A-Za-z].*",word):
                        data['word'] += 1
                if data['word'] > 1:
                    data['code_line'] += 1
                data['character'] += len(lines) - 1
    except Exception as err:
        print(err)
    finally:
        fi.close()
    return data

def recursion():
    """处理目录下符合条件的文件"""
    file_list = getfile()
    for filename in file_list:
        datalist = count(filename)
        print("文件名：%s" % filename)
        print(datalist)