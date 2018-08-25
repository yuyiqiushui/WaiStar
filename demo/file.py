# fpath_blue = 'E:\小程序\echart_line\client\images\home_blue.png'
# fpath = 'E:\小程序\echart_line\client\images\light1.bmp'
# fpath = 'E:\小程序\echart_line\client\images\my.png'
#
# with open(fpath_blue, 'rb') as f:
#     s = f.read()
#     print(s)
# with open(fpath, 'rb') as f:
#     s = f.read()
#     print(f.tell())
# import io as IO
#
# F=IO.StringIO()
# F.write("hello")
# print(F.getvalue())


# import os as OS
# print(OS.name)
# print(OS.environ)
# print(OS.path.abspath("."))
# print(OS.path.join("E:\python\demo","test"))
# print(OS.path.splitext('E:\python\demo\title.py'))
# for x in OS.listdir('.'):
#     if OS.path.isfile(x) and OS.path.splitext(x)[1]==".txt":
#         print(x)
# print(help(OS))

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
