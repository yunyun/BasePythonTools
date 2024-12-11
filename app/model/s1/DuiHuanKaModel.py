import logging
from app.model.S1DataBaseModel import S1DataBaseModel as DatabaseModel


class DuiHuanKaModel(DatabaseModel):
    table = "duihuanka"

    def getList(self, moId):
        sql = "select * from {} where md_owner='{}'".format(
            self.table,
            moId
        )
        logging.info(sql)
        return self.fetchAll(sql)

    def getInfo(self, card_id):
        sql = "select * from {} where cardid='{}'".format(
            self.table,
            card_id
        )
        logging.info(sql)
        return self.fetchOne(sql)

    def add(self, data):
        return self.insert(data)

    def del_dhk(self, id):
        sql = "DELETE FROM {} WHERE id = {};\n".format(
            self.table,
            id
        )
        return sql
