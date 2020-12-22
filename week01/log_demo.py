import logging
import time
import os,sys

from pathlib import Path,PurePath

def add_log():
    # 获取当前文件所在目录
    current_path=PurePath(__file__).parent
    # 拼接日志创建目标目录 并 转换为目录类型
    log_date=time.strftime('%Y%m%d',time.localtime())
    target_path=Path(Path(current_path)/'var/log/python-{}/'.format(log_date))
    # 判断目录是否存在，不存在则创建对应的文件夹
    if not target_path.exists():
        target_path.mkdir(parents=True)
    log_file_name= target_path / 'wk1.log'
    log_file_path= Path(log_file_name)
    # 判断日志文件是否存在，不存在则创建对应日志文件
    if not log_file_path.exists():
        log_file_path.touch()
    
   
    logging.basicConfig(
        filename=log_file_name,
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format = '%(asctime)s %(name)s [line:%(lineno)d] %(levelname)s %(message)s'
    )
    
    call_time=time.strftime('%Y-%m-%d %X',time.localtime())
    msg=sys._getframe().f_code.co_name
    logging.info('函数{}调用时间为{}'.format(msg,call_time))
    logging.debug('函数{}调用时间为{}'.format(msg,call_time))
    logging.warning('函数{}调用时间为{}'.format(msg,call_time))
    logging.error('函数{}调用时间为{}'.format(msg,call_time))
    logging.critical('函数{}调用时间为{}'.format(msg,call_time))



 
if __name__ == '__main__':
      add_log()
    # print(logfile)
    # logging.debug("调试消息")
    # logging.info("普通消息")
    # logging.warning("警告消息")
    # logging.error("错误消息")
    # logging.critical("严重错误消息")


# /var/log/python-{}/xxxx.log