import logging

import config
import pymysql


class MysqlDatabase():

    def __init__(self):
        self.db = None
        self.cursor = None
        self.connect()

    def connect(self):
        """建立数据库连接"""

        db_config = None
        if self.db_name is not None:
            db_config = config.Config.DATABASE[self.db_name]
        else:
            db_config = config.Config.DATABASE[config.Config.DATABASE_DEFAULT]

        host = db_config['HOST']
        username = db_config['USERNAME']
        password = db_config['PASSWD']
        database = db_config['DATABASE']
        port = db_config['PORT']
        charset = db_config["CHARSET"]  # charset

        try:
            self.db = pymysql.connect(host=host, user=username, password=password, database=database, port=port, charset=charset)
            self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            logging.info(f"成功连接到数据库")
        except pymysql.err.OperationalError as e:
            logging.error(f"连接数据库失败: {e}")
            self.db = None
            self.cursor = None

    def reconnect(self):
        """重新建立数据库连接"""

        logging.info("尝试重新连接数据库...")
        self.connect()  # 调用连接方法重新建立连接
        if self.db:
            logging.info("重新连接成功")
            return True
        else:
            logging.info("重新连接失败")
            return False

    def close(self):
        """关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()

    def fetchAll(self, sql):
        if self.db.open:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
        else:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
        return self.cursor.fetchall()

    def execute(self, sql):
        if self.db.open:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
        else:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()

    def fetchOne(self, sql):
        if self.db.open:
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()
        else:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            self.db.commit()
            self.db.close()

        return self.cursor.fetchone()

    def executemany(self, sql, params):
        if self.db.open:
            self.cursor.executemany(sql, params)
            insertId = self.db.insert_id()
            self.db.commit()
            self.db.close()
        else:
            self.db.ping(reconnect=True)
            self.cursor.executemany(sql, params)
            insertId = self.db.insert_id()
            self.db.commit()
            self.db.close()
        return insertId

    def executeId(self, sql):
        if self.db.open:
            self.cursor.execute(sql)
            insertId = self.db.insert_id()
            self.db.commit()
            # self.db.close()
        else:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql)
            insertId = self.db.insert_id()
            self.db.commit()
            # self.db.close()
        return insertId

    def executeAll(self, sql, params):
        if self.db.open:
            self.cursor.execute(sql, params)
            insertId = self.db.insert_id()
            self.db.commit()
            self.db.close()
        else:
            self.db.ping(reconnect=True)
            self.cursor.execute(sql, params)
            insertId = self.db.insert_id()
            self.db.commit()
            self.db.close()
        return insertId

    def insert(self, data):

        # 构造插入语句
        # insert_statement = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(data.keys()),
        #                                                             ", ".join(["'%s'"] * len(data)))

        insert_statement = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(
            ["`{}`".format(key) for key in data.keys()]),
                                                                    ", ".join(["'%s'"] * len(data)))

        # 使用参数绑定的方式执行SQL语句
        sql = insert_statement % tuple(data.values())

        logging.info(sql)
        return self.executeId(sql)

    def update(self, data, condition_key):
        # 构造更新语句的SET部分
        set_clause = ", ".join(
            ["{} = %s".format("`{}`".format(key)) for key in data.keys() if key != condition_key])

        # 构造更新语句的WHERE部分
        where_clause = "`{}` = %s".format(condition_key)

        # 构造完整的更新语句
        update_statement = "UPDATE {} SET {} WHERE {}".format(self.table, set_clause, where_clause)

        logging.info(update_statement)
        # 使用参数绑定的方式执行SQL语句
        params = tuple(data[key] for key in data.keys() if key != condition_key) + (data[condition_key],)
        # print(params)
        return self.executeAll(update_statement, params)

    def multi_insert(self, data_list):
        # 假设data_list是一个列表，其中每个元素都是一个字典，代表一行要插入的数据
        # 并且所有字典的键都是相同的（即列名）
        if not data_list or not isinstance(data_list[0], dict):
            raise TypeError("data_list must be a list of dictionaries")

            # 构造插入语句的列部分
        # columns = ", ".join(["`{}`".format(key) for key in data_list[0].keys()])

        # 构造插入语句（不需要显式的placeholders字符串，因为executemany会处理）
        insert_statement = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(
            ["`{}`".format(key) for key in data_list[0].keys()]),
                                                                    ", ".join(["%s"] * len(data_list[0])))
        # insert_statement = "INSERT INTO {} ({}) VALUES %s".format(self.table, columns)

        # 使用参数绑定的方式（通过executemany）执行SQL语句
        params = [tuple(data.values()) for data in data_list]

        return self.executemany(insert_statement, params)

    def multi_update(self, data_list, condition_key):
        # 假设data_list是一个列表，其中每个元素都是一个字典，代表一行要更新的数据
        # condition_key是用于匹配要更新行的键（通常是主键或唯一索引）
        if self.db.open is None:
            self.db.ping(reconnect=True)

        # 逐条执行更新语句
        for data in data_list:
            # 构造更新语句的SET部分
            set_clause = ", ".join(
                ["{} = %s".format("`{}`".format(key)) for key in data.keys() if key != condition_key])

            # 构造更新语句的WHERE部分
            where_clause = "`{}` = %s".format(condition_key)

            # 构造完整的更新语句
            update_statement = "UPDATE {} SET {} WHERE {}".format(self.table, set_clause, where_clause)

            logging.info(update_statement)
            # 使用参数绑定的方式执行SQL语句
            params = tuple(data[key] for key in data.keys() if key != condition_key) + (data[condition_key],)
            # print(params)
            self.cursor.execute(update_statement, params)

        # 提交事务
        self.db.commit()
        self.db.close()
        return True

        # 如果需要，可以返回受影响的行数（但通常不需要）
        # 可以通过self.cursor.rowcount获取受影响的行数（但请注意，并非所有数据库驱动都支持这个属性）
