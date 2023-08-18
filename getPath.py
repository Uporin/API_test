import os


# 此方法获取项目绝对路径
class GetPath():
    def getPath(self):
        # 获取当前所在文件夹的绝对路径
        path_directory = os.path.split(os.path.realpath(__file__))[0]
        return path_directory


if __name__ == '__main__':
    getpath = GetPath()
