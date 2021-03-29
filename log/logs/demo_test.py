import logging
import os
import datetime

class LoggerTest:
    def __init__(self):
        '''
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  #设置日志级别

        current_path = os.path.dirname(os.path.realpath(__file__))
        # 指定文件输出路径，注意logs是个文件夹，一定要加上/，不然会导致输出路径错误，把log变成文件名的一部分了
        log_path = current_path 
        # 指定输出的日志文件名
        dt = datetime.strftime(datetime.now(), "%Y-%m-%d_%H")
        # 日志的文件名
        logname = log_path + str(dt)+ '.log.'
        # 创建一个handler，用于写入日志文件, 'a'表示追加
        file_handler = logging.FileHandler(logname, 'a')
        # 为logger添加的日志处理器
        self.logger.addHandler(file_handler)

        formatter = logging.Formatter('%(asctime)s => %(name)s * %(levelname)s : %(message)s')
        # 设置日志内容的格式
        file_handler.setFormatter(formatter)
        '''
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  #设置日志级别
        base_dir = os.path.abspath(os.path.abspath(__file__))
        file_dir = os.path.join(base_dir, "logs")
        filename = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        print(filename)
        # 日志的文件名
        logname = log_path + str(dt)+ '.log.'
        # 创建一个handler，用于写入日志文件, 'a'表示追加
        file_handler = logging.FileHandler(file_dir+logname, 'a', encoding='utf-8')
        # 为logger添加的日志处理器
        self.logger.addHandler(file_handler)

    def fun(self):
        self.logger.error("这个一条错误日志")
        self.logger.info("这是一条info日志")
        self.logger.debug("这是一条debug日志")
        self.logger.warning("这是一条warning日志")

if '__main__' == __name__:
    testLogger = LoggerTest()
    testLogger.fun()