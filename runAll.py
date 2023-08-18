from getPath import GetPath
import os
from common.log import logger
import unittest
from common import HTMLTestRunnerCN
from testFile.readConfig import ReadConfig
from common.configEmail import SendEmail

path = GetPath().getPath()  # /Users/dongyue/Documents/framework
# 定义报告文件夹路径
report_path = os.path.join(path, r"result\report")
readconfig = ReadConfig()


class AllTest():
    def __init__(self):  # 定义初始化数据
        global result_path
        # 定义文件路径，以及文件名
        result_path = os.path.join(report_path, "report.html")
        logger.info("result_path：%s" % result_path)
        # 定义要执行的case文件的路径
        self.case_list_path = os.path.join(path,
                                           r"testFile\caselist.txt")  # /Users/dongyue/Documents/framework/testFile/caselist.txt
        logger.info("case_list_path：%s" % self.case_list_path)
        # 定义需要测试case的py文件路径
        self.case_file = os.path.join(path, "case")  # /Users/dongyue/Documents/framework/case
        logger.info("case_file：%s" % self.case_file)
        # 定义要执行的case的py文件集合
        self.caselist = []

    def set_caselist(self):
        # 读取caselist.txt文件，写入caselist列表
        file = open(self.case_list_path)
        str = file.readlines()
        for i in str:
            if i != "" and not i.startswith("#"):
                self.caselist.append(
                    i.split('/')[1].replace("\n", "") + ".py")  # 按照/进行切割字符串取后面带py文件的，然后将\n替换为空，最后添加到caselist中
        logger.info("newcaselist：%s" % self.caselist)
        return self.caselist
        file.close()

    def set_case_suit(self):
        # self.set_caselist()  #获取上述caselist列表
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.set_caselist():
            discover = unittest.defaultTestLoader.discover(self.case_file, pattern=case, top_level_dir=None)  ##批量加载用例
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)

        else:
            logger.debug("测试套件集合为空")
            return None

        return test_suite

    def send_email(self):
        subject = readconfig.get_email("subject")
        mail_host = readconfig.get_email("mail_host")
        mail_user = readconfig.get_email("mail_user")
        mail_pass = readconfig.get_email("mail_pass")
        sender = readconfig.get_email("sender")
        receivers_str = readconfig.get_email("receivers")
        for i in range(len(eval(receivers_str))):
            # print(eval(receivers_str)[i])
            data = open(r'C:\Users\lj\Desktop\接口自动化\API_long1\result\report\report.html', 'rb').read()
            c = SendEmail(subject, mail_host, mail_user, mail_pass, sender, eval(receivers_str)[i], data)
            c.sendemail()

    def run(self):
        # 执行测试集，并且生成报告
        fp = None  # 初始化fp变量
        try:
            suite = self.set_case_suit()
            if suite:
                fp = open(result_path, 'wb')
                runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='自动化测试报告',
                                                         description='接口自动化测试python + unittest')
                runner.run(suite)
                if readconfig.get_email("on_off") == "on":
                    self.send_email()
                else:
                    logger.debug("邮件开关没有打开")
            else:
                logger.debug("测试套件集合为空")
        except Exception as ex:
            logger.debug(ex)
        finally:
            logger.info("*********TEST END*********")
            if fp is not None:
                fp.close()  # 在关闭文件之前检查fp是否已被赋值


if __name__ == '__main__':
    AllTest().run()