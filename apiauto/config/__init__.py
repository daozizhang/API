import xlrd
import openpyxl
# import os
#
#
# def get_cwd():
#     path = os.path.join(os.path.dirname(__file__), '/testdata/roms.xlsx')
#     return path
# print(get_cwd())

# workbook = xlrd.open_workbook(get_cwd())
# sheet = workbook.sheet_names()
# sh = workbook.sheets()
# name = workbook.sheet_by_name('猎聘入网')
# rows = workbook.sheet_by_name('猎聘入网').row_values(rowx=0)
# cols = xlrd.open_workbook(get_cwd()).sheet_by_name('猎聘入网').col_values(colx=1)
# print(rows, cols, end='\n')
# value = xlrd.open_workbook(get_cwd()).sheet_by_name('猎聘入网').cell_value(0, 1)
# value1 = xlrd.open_workbook(get_cwd()).sheet_by_name('猎聘入网').cell(0, 1).value
# print(value, value1)
# ls = []
# for i in cols:
#
#     if i == 'test_3_openApi_enterprise_register':
#         num = cols.index(i)
#         ls.append(num)
# for i in ls:
#     print(xlrd.open_workbook(get_cwd()).sheet_by_name('猎聘入网').cell_value(i, 1))

