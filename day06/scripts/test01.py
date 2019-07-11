import allure
import pytest


class Test01():

    @allure.step(title="正在执行登录操作！")
    def test001(self):
        print("test001被执行")

    @allure.step(title="正在执行退出操作！")
    def test002(self):
        print("test002被执行")

    # 紧要级别
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test003(self):
        # 添加描述
        allure.attach("描述：","正在打印test003被执行")
        print("test003被执行")

    # 崩溃级别
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test004(self):
        # 添加描述
        allure.attach("描述：","")
        # 模拟失败，目的：查看图标优先级颜色
        assert 0
        print("test004被执行")

    def test005(self):
        # 失败截图，将图片写入报告
        with open("./image/fail.png","rb")as f:
            # 参数：（描述：，文件流，图片类型）
            allure.attach("失败原因：",f.read(),allure.attach_type.PNG)