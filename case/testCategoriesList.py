from testFile.readExcel import ReadExcel
import paramunittest
import unittest
from common.configHttp import Run_Main
import json
from common.log import logger
from common.configapiMock import Mock_Test

# 读取excel中的测试case   readExcel.py封装的函数，需要传递入参数：excel_name,sheet_name，[1:]的意思是从下标为1往后开始。
readexcel = ReadExcel().getexcel("API_test.xlsx", "base_data")[1:]


@paramunittest.parametrized(*readexcel)  # 参数化
class testCategoriesList(unittest.TestCase):

    def setParameters(self, module, ID, casename, url, method, data, headers, body, status_code, message, result, mock):  # 测试case的属性
        self.module = module
        self.ID = ID
        self.casename = casename
        self.url = url
        self.method = method
        self.data = data
        self.headers = headers
        self.body = body
        self.status_code = status_code
        self.message = message
        self.result = result
        self.mock = mock



    def setUp(self) -> None:
        logger.info(self.casename + "......测试开始......")

    def tearDown(self) -> None:
        logger.info(self.casename + "......测试结束......")

    def description(self):
        self.casename

    def testcategorieslist(self):
        # 如果case需要mock，就掉用configapiMock中封装好的函数
        if self.caseismock():
            resp = Mock_Test().mocktest(mock_method=Run_Main().run_main, method=self.method, url=self.url)
            self.check_result(resp)

        # 否则，就正常发送请求，判断返回值
        else:
            resp = Run_Main().run_main(self.url, self.method)  # configHttp.py中的函数，需要传url和method等参数
            self.check_result(resp)

    def caseismock(self):
        # 判断该case是否需要mock
        if Mock_Test().ismock("mock_testCategoriesList"):  # 判断config.ini中是否存在配置好的mock数据
            if self.mock == "Y":  # 判断从excel中获取到的数据是否需要mock
                logger.info(self.casename + "mock该case")
                return True
            else:
                logger.info(self.casename + "该case不需要mock")
                return False
        else:
            logger.info(self.casename + "不存在mock数据")

    def check_result(self, response):
        info = json.loads(response)  # 格式化返回值
        # 判断返回值中的status是否等于预期中的值
        self.assertEqual(info["status"], int(self.status_code))
        logger.info("status=%s" % int(self.status_code) + "(期望值|实际值)%s" % info["status"])


if __name__ == '__main__':
    unittest.main(verbosity=2)