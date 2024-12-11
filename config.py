class Config:
    LOG_DIR: str = "./logs/"  # 日志
    MAIN_DIR: str = "./"  # 主目录
    DBS_LOG_DIR: str = "./db_log/"  # 数据库日志
    DBS_DIR: str = "./db/"  # 数据库目录
    QRCODE_DIR: str = "./qrcode/"  # 数据库目录

    DATABASE_TYPE: str = "mysql"  # mysql or sqlite

    # 数据库配置
    DATABASE_DEFAULT: str = "S1"

    DATABASE: dict = {

        "S1": {
            'HOST': "127.0.0.1",
            'USERNAME': "root",
            'PASSWD': "123456",
            'DATABASE': "s1",
            'PORT': 2500,
            'CHARSET': "utf8mb4"
        },

        "V9": {
            'HOST': "127.0.0.1",
            'USERNAME': "root",
            'PASSWD': "123456",
            'DATABASE': "v9",
            'PORT': 2500,
            'CHARSET': "utf8mb4"
        },

        "NEWS1": {
            'HOST': "127.0.0.1",
            'USERNAME': "root",
            'PASSWD': "123456",
            'DATABASE': "ddf_s1",
            'PORT': 3306,
            'CHARSET': "utf8mb4"
        },
    }

