
import xlwt

wb=xlwt.Workbook()
sheet=wb.add_sheet("Neha")
style=xlwt.easyxf("font: bold 1, color red;")
sheet.write(0,0,"Ansh",style)
sheet.write(1,1,"vivek")

wb.save("example")
