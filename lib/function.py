import hashlib
import random
import string
import time
from datetime import datetime


def datetime_to_unix(dt):
    """
    将datetime对象转换为UNIX时间戳（秒）
    :param dt: datetime对象
    :return: UNIX时间戳（整数）
    """
    return int(dt.timestamp())


def unix_to_datetime(unix_time):
    """
    将UNIX时间戳（秒）转换为datetime对象
    :param unix_time: UNIX时间戳（整数或浮点数）
    :return: datetime对象
    """
    return datetime.fromtimestamp(unix_time)


def date_to_unix(d):
    """
    将date对象转换为UNIX时间戳（秒）
    :param d: date对象
    :return: UNIX时间戳（整数）
    """
    # 将date对象转换为datetime对象，时间设为当天的00:00:00
    dt = datetime(d.year, d.month, d.day)
    # 转换为UNIX时间戳
    return int(dt.timestamp())


def unix_to_date(unix_time):
    """
    将UNIX时间戳（秒）转换为date对象
    :param unix_time: UNIX时间戳（整数或浮点数）
    :return: date对象
    """
    # 将UNIX时间戳转换为datetime对象
    dt = datetime.fromtimestamp(unix_time)
    # 提取date部分
    return dt.date()


def get_unix_now():
    """
    获得当前时间戳
    :return:
    """
    current_time = datetime.now()
    return int(current_time.timestamp())


def get_date_now():
    """
    获得当前时间
    :return:
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d")
    return str(formatted_time)


def get_datetime_now():
    """
    获得当前时间
    :return:
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return str(formatted_time)


def only_date_id(function):
    random_number = random.randint(1000, 9999)  # 随机数
    str_time = int(time.time())  # 当前时间戳
    rand_string = rand_string_generator(random.randint(0, 9))  # 生成随机字符串
    # 使用 md5 哈希函数来生成最终的字符串
    hashed_string = hashlib.md5(f"{random_number}{str_time}{function}{rand_string}".encode('utf-8')).hexdigest()
    return hashed_string


def rand_string_generator(length):
    # 定义包含所有字母大小写的字符集合
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
