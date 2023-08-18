import os
from getPath import GetPath
from xlrd import open_workbook

# 项目的绝对路径
path = GetPath().getPath()


class ReadExcel():
    def getexcel(self, excel_name, sheet_name):
        case_set = []
        excelpath = os.path.join(path, "excel", excel_name)  # 拼接excel的路径
        excel = open_workbook(excelpath)  # excel对象
        sheet = excel.sheet_by_name(sheet_name)  # 获取该excel的sheet
        rows = sheet.nrows  # 获取该sheet的行数

        for i in range(rows):
            if sheet.row_values(i)[0] != 'case_name':
                case_set.append(sheet.row_values(i))
        return case_set

        print(case_set)

