#coding:utf-8
#---------------------------------------------------------
import sys
import xlwt
reload(sys)
sys.setdefaultencoding( "utf-8" )

file_excel = xlwt.Workbook(encoding='utf-8')
table = file_excel.add_sheet('website')
table.write(0,0,'test测试')
file_excel.save('test.xls')