import logging
import os

import qrcode

from app.model.s1.DuiHuanKaModel import DuiHuanKaModel
from config import Config
from lib.base import getNO, WriteFile
from lib.function import get_datetime_now


class DuiHuanController():

    def AddData(self):
        num = 10010
        moId = 1
        suihuanModel = DuiHuanKaModel()

        for i in range(1, num):
            add_data = {
                "owner": "18769775372",
                "usewdname": "",
                "cardname": "免费洗车活动",
                "cardid": getNO(11),
                "starttime": "2024-12-5",
                "overtime": "2024-12-31",
                "cardtype": "储值卡",
                "jine": "20",
                "cishu": "0",
                "youxiaoqi": "60",
                "vipname": "",
                "lingqutime": get_datetime_now(),
                "wangdian": "",
                "bianhao": "",
                "is_new": 0,
                "type_id": 0,
                "md_owner": moId,
                "is_md_or_owner": 1,
            }

            print(add_data["cardid"])
            type = suihuanModel.getInfo(add_data["cardid"])
            if type is not None:
                print("跳过：" + add_data["cardid"])
                logging.info("跳过：" + add_data["cardid"])
                break

            id = suihuanModel.add(add_data)
            db_str = suihuanModel.del_dhk(id)
            WriteFile("db.sql",db_str)

            pass
        pass

    def QrCode(self):
        moId = 1
        suihuanModel = DuiHuanKaModel()
        dh_rt = suihuanModel.getList(moId)



        if not os.path.exists(Config.QRCODE_DIR):
            os.makedirs(Config.QRCODE_DIR)

        for info in dh_rt:
            qr = qrcode.QRCode(
                version=1,  # 控制二维码的大小，范围是1到40，1是最小的
                error_correction=qrcode.constants.ERROR_CORRECT_L,  # 控制二维码的纠错级别
                box_size=10,  # 每个小格子的像素数
                border=4,  # 边框的宽度（小格子的数量）
            )

            qr.add_data(info["cardid"])
            qr.make(fit=True)
            # 创建图像对象
            img = qr.make_image(fill='black', back_color='white')

            # 保存图像到文件

            img.save(Config.QRCODE_DIR + "qrcode_{}.png".format(info["cardid"]))
            qr.clear()

            print(info["cardid"])
        pass

    def Main(self):
        # self.AddData()
        self.QrCode()
        pass