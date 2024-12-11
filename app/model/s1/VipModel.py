import logging
from app.model.S1DataBaseModel import S1DataBaseModel as DatabaseModel


class VipModel(DatabaseModel):
    table = "vip"

    def getList(self, owner):
        sql = "select * from {} where owner='{}'".format(
            self.table,
            owner
        )
        logging.info(sql)
        return self.fetchAll(sql)

    def getOne(self, phone, owner):
        sql = "select * from {} where phone ='{}' and owner='{}'".format(
            self.table,
            phone,
            owner
        )
        logging.info(sql)
        return self.fetchOne(sql)

    def delVip(self, id):
        sql = "DELETE FROM {} WHERE id = {};\n".format(
            self.table,
            id
        )
        return sql
