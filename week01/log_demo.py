import logging
import time
import os,sys
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)

def add_log(filename):
    log_date=time.strftime('%Y-%m-%d',time.localtime())
    log_path=filename
    logfile=os.path.join(log_path,'{}/test.log')
    logging.basicConfig(
        filename=logfile,
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format = '%(asctime)s %(name)s [line:%(lineno)d] %(levelname)s %(message)s'
    )
    
    call_time=time.strftime('%Y-%m-%d %X',time.localtime())
    msg=sys._getframe().f_code.co_name
    print('函数{}调用时间为{}'.format(msg,call_time))

add_log()

# if __name__ == '__main__':
#     # print(logfile)
#     logging.debug("调试消息")
#     logging.info("普通消息")
#     logging.warning("警告消息")
#     logging.error("错误消息")
#     logging.critical("严重错误消息")


# /var/log/python-{}/xxxx.log