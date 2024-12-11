import os
import platform
import random
import sys
import time

from config import Config
import logging


def beginLogsStart():
    if not os.path.exists(Config.LOG_DIR):
        os.makedirs(Config.LOG_DIR)

    log_dir = f'{Config.LOG_DIR}back_' + time.strftime("%Y-%m-%d", time.localtime()) + '.log'

    logging.basicConfig(  # 针对 basicConfig 进行配置(basicConfig 其实就是对 logging 模块进行动态的调整，之后可以直接使用)
        # encoding='utf-8',
        level=logging.INFO,  # INFO 等级以下的日志不会被记录
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 日志输出格式
        filename=log_dir,  # 日志存放路径(存放在当前相对路径)
        filemode='a',  # 输入模式；如果当前我们文件已经存在，可以使用 'a' 模式替代 'w' 模式
        # 与文件写入的模式相似，'w' 模式为没有文件时创建文件；'a' 模式为追加内容写入日志文件
    )


def selfWrite(file, content):
    if not os.path.exists(Config.DBS_LOG_DIR):
        os.makedirs(Config.DBS_LOG_DIR)

    log_dir = f'{Config.DBS_LOG_DIR}back_write_' + file

    try:
        with open(log_dir, 'a', encoding='utf-8') as file:
            file.write(content)
        return True
    except IOError:
        return False


def WriteFile(file, content):
    if not os.path.exists(Config.DBS_LOG_DIR):
        os.makedirs(Config.DBS_LOG_DIR)

    log_dir = f'{Config.DBS_LOG_DIR}back_write_' + file

    try:
        with open(log_dir, 'a', encoding='utf-8') as file:
            file.write(content)
        return log_dir
    except IOError:
        return None


def getNO(digit=8):
    code = random.randint(10 ** (digit - 1), 10 ** digit - 1)
    return code


def getOSVersion():
    os_type = platform.system()
    machine = platform.machine()
    bit = "64" if "64" in machine else "32"
    if "arm" in machine.lower():
        cpu = "arm"
    elif machine.endswith("64") or sys.maxsize > 2 ** 32:
        cpu = "x86_64"
    else:
        cpu = "x86"
    system_info = {
        'system': os_type,
        'cpu': cpu,
        'bit': bit
    }
    return system_info
