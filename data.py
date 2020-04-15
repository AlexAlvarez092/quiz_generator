import xlrd

# dictionary
d = {}

# open the workbook
wb = xlrd.open_workbook('foo.xls')


sh = wb.sheet_by_index(0)

for i in range(10):
    cell_value_class = sh.cell(i, 0).value
    cell_value_id = sh.cell(i, 1).value
    d[cell_value_class] = cell_value_id

for k, v in d.items():
    print(k, v)
