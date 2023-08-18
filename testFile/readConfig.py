import os
from getPath import GetPath  # 导入文件夹下的GetPath类
import configparser

# path = GetPath().getPath()  #对象调用getPath方法，获取当前文件夹的绝对路径
config_path = os.path.join(GetPath().getPath(), "testFile/config.ini")  # 拼接配置文件config.ini的绝对路径
config_object = configparser.ConfigParser()  # 实例化python的读取配置文件的对象
config_object.read(config_path, encoding="utf-8")  # 读取配置文件对象按照config.ini路径读取文件中内容


class ReadConfig():

    def get_http(self, name):
        value = config_object.get("HTTP", name)
        return value

    def get_db(self, dbname, name):
        value = config_object.get(dbname, name)
        return value

    def get_mockdata(self, api_name, name):
        value = config_object.get(api_name, name)
        return value

    def get_secs(self):
        secs_list = config_object.sections()
        return secs_list


if __name__ == '__main__':
    ReadConfig()