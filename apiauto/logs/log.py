import colorlog

import logging
import time

from logs.get_cwd import *


def get_log(log_name):
    log_colors_config={
        'DEBUG': 'black',  # cyan white
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
    #创建一个logger
    logger=logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    #设置时间格式
    #tm=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # tm=datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    rq=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    #print(rq)
    #设置log存放路径
    path=get_cwd()
    all_log_path=os.path.join(path,'All_logs/')
    err_log_path=os.path.join(path,'Error_logs/')
    #设置日志文件名
    all_log_name=all_log_path+rq+'.log'
    err_log_name=err_log_path+rq+'.log'


    #创建handler，写入所有日志
    fh=logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    print(fh)

    eh=logging.FileHandler(err_log_name)
    eh.setLevel(logging.WARNING)

    #创建handler，输出到控制台
    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    #定义日志输出格式:时间-日志名称-日志级别-日志行数-日志内容
    all_log_format=logging.Formatter(
        fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        datefmt='%Y-%m-%d  %H:%M:%S'
    )
    err_log_format=colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        datefmt='%Y-%m-%d  %H:%M:%S',
        log_colors=log_colors_config
    )
    # all_log_format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(lineno)s-%(message)s')
    # err_log_format=logging.Formatter('%(asctime)s|%(name)s||%(levelname)s|||%(lineno)s->%(message)s')

    #将格式添加到handler
    fh.setFormatter(all_log_format)
    eh.setFormatter(all_log_format)
    ch.setFormatter(err_log_format)

    # 给logger添加handler
    # 重复日志问题：
    # 1、防止多次addHandler；
    # 2、loggername 保证每次添加的时候不一样；
    # 3、显示完log之后调用removeHandler
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(eh)
        logger.addHandler(ch)

    fh.close()
    eh.close()
    ch.close()
    return logger

log=get_log('webuiAuto')

if __name__ == '__main__':

    log1=get_log('webuiAuto')
    log1.debug('这是debug消息')
    log1.info('这是error消息')

