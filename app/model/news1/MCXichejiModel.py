import logging
from app.model.NewS1DataBaseModel import NewS1DataBaseModel as DatabaseModel


class MCXichejiModel(DatabaseModel):
    table = "mc_xicheji"

    def getList(self):
        sql = "select * from {} ".format(
            self.table
        )
        logging.info(sql)
        return self.fetchAll(sql)

    def getOne(self, bianhao):
        sql = "select * from {} where bianhao ='{}'".format(
            self.table,
            bianhao
        )
        logging.info(sql)
        return self.fetchOne(sql)
