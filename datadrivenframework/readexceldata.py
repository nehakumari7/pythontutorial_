import xlrd

def getdata():
    wb=xlrd.open_workbook("credential.xlsx")
    sheet=wb.sheet_by_name("Credentail")
    data=[]
    for i in range(1,sheet.nrows):
        data.append((sheet.cell_value(i,0),(sheet.cell_value(i,1))))

    return data