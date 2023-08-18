from mock import Mock
from testFile.readConfig import ReadConfig


class Mock_Test():

    def ismock(self, api_name):
        # 判断该接口的mock数据
        global data
        data = ReadConfig().get_mockdata(api_name=api_name, name="data")

        if data:
            return True
        else:
            return False

    def mocktest(self, mock_method, method, url, header=None, request_data=None):
        # 返回mock的结果
        mock_method = Mock(return_value=data)
        res = mock_method(url=url, method=method, request_data=request_data, header=header)
        return res


if __name__ == '__main__':
    Mock_Test()