from app.controller.DuiHuan.DuiHuanController import DuiHuanController
from app.controller.MoNi.GongJiController import GongJiController


class MainController:

    def Main(self):

        # 兑换卷功能
        # duihuanCon = DuiHuanController()
        # duihuanCon.Main()

        # 攻击模拟
        gongjiCon = GongJiController()
        gongjiCon.Main()

        pass