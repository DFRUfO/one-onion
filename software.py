import sys
import output as op
from window import Window
def main():
    """主程序"""
    file = sys.argv[2]  #从命令行中获取参数文件名
    command  = sys.argv[1]
    file_name = file
    if command == '-x':
        Window()
    op.Output(command,file_name)
main()




