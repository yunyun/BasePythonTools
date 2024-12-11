import logging
import os
import threading

import qrcode

from app.model.news1.MCXichejiModel import MCXichejiModel
from app.model.s1.DuiHuanKaModel import DuiHuanKaModel
from config import Config
from lib.base import getNO, WriteFile
from lib.function import get_datetime_now
from lib.socket import client_thread_main


class GongJiController():

    def GetAllList(self):
        mcModel = MCXichejiModel()
        mc_list = mcModel.getList()
        client_threads = []

        for item in mc_list:
            bianhao = item["bianhao"]
            client_thread_id = f"{bianhao}"
            send_str = f",xt|{bianhao}|0.0|1|1"
            client_thread = threading.Thread(target=client_thread_main, args=(client_thread_id,send_str))
            client_threads.append(client_thread)
            client_thread.start()
            print(bianhao)

        # 等待所有客户端线程完成
        for client_thread in client_threads:
            client_thread.join()

        pass

    def Main(self):
        self.GetAllList()
        pass