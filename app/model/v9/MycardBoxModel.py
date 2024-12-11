import logging
from app.model.V9DataBaseModel import V9DataBaseModel as DatabaseModel


class MycardBoxModel(DatabaseModel):
    table = "mycardbox"

    def getList(self, owner):
        sql = "select * from {} where owner='{}'".format(
            self.table,
            owner
        )
        logging.info(sql)
        return self.fetchAll(sql)

    def getOne(self, cardid, owner):
        sql = "select * from {} where cardid ='{}' and owner='{}'".format(
            self.table,
            cardid,
            owner
        )
        logging.info(sql)
        return self.fetchOne(sql)

    def delMycardbox(self, id):
        sql = "DELETE FROM {} WHERE id = {};\n".format(
            self.table,
            id
        )
        return sql
