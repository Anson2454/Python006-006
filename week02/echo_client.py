#!/usr/bin/env python
import socket
from  datetime import datetime
from pathlib import *

HOST = 'localhost'
PORT = 10000

def echo_client(file):

    ''' Echo Server Client '''
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # 接收用户输入数据并发送服务端
        data = input('input > ')

        # 设定退出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        s.sendall(data.encode())

        # 接收服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            try:
                with open(page,'w',encoding='utf-8') as f:
                    f.write(str(data))
            except FileNotFoundError as e:
                print(f'文件无法打开：{e}')
            except IOError as e:
                print(f'文件读写出错: {e}')
            except Exception as e:
                print(e)

    s.close()


if __name__ == '__main__':
    p=Path(__file__)  #获取当前文件绝对路径
    pyfile_path=p.resolve().parent #获取父目录
    # print(pyfile_path)
    # 定义需要保存的目标文件夹，不存在则新建
    result_path= pyfile_path.joinpath('ehco_files') 
    # print(result_path)
    if not result_path.is_dir():
        Path.mkdir(result_path)
    page =result_path.joinpath(f'{datetime.now().strftime("%Y%m%d%H%M%S")}.txt') # 最终存放的文件绝对路径
    echo_client(page)