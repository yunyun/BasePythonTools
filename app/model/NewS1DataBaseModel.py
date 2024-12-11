import logging

from lib.MysqlDatabase import MysqlDatabase as Database


class NewS1DataBaseModel(Database):
    """
    基类，用于初始化数据库连接，数据库名称固定为"DB1"。
    """
    db_name = "NEWS1"
