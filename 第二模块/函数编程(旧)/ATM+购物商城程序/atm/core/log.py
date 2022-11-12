# 日志记录模块
import logging,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
user_Water = BASE_DIR + r"/log/water_record"

'''日志模块'''
def get_logger():
    #有循环的时候 要放到循环外面
    fh = logging.FileHandler(user_Water)  # 创建一个文件流,需要给一个文件参数

    logger = logging.getLogger()  # 获得一个logger对象

    #sh = logging.StreamHandler()  # 创建一个屏幕流，
    logger.setLevel(logging.DEBUG)  # 设定最低等级debug
    # 写入文件的中的格式
    fm = logging.Formatter("%(asctime)s --- %(message)s")
    logger.addHandler(fh)   # 把文件流添加进来，流向文件
    #logger.addHandler(sh)  # 把屏幕流添加进来，流向屏幕

    fh.setFormatter(fm)  # 在文件流添加写入格式
    #sh.setFormatter(fm)  # 在屏幕流添加写入格式

    return logger

