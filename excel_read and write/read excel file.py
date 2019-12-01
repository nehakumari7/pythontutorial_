import xlrd

wb=xlrd.open_workbook(r"Schooldatabase.xlsx")
sheet=wb.sheet_by_name("Student Data")
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(1,5))
print(sheet.row_values(2,0,1))
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        print(sheet.cell_value(i,j),end=" ")
    print()

#print() is just to give new line