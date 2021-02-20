import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="C:/Users/mipti/Desktop/table.xlsx")
wb.active = 0
sheet = wb.active
print(sheet['A1'].value)
msg = 'Ингибиторы 5 альфа редуктазы; ТУИП'
for i in range(1, 5185):
    if(sheet['A' + str(i)].value == 1 and
        sheet['B' + str(i)].value == 0 and
        sheet['C' + str(i)].value == 0 and
        sheet['D' + str(i)].value == 1 and
        sheet['E' + str(i)].value == 0 and
        sheet['F' + str(i)].value == 1 and
        sheet['G' + str(i)].value == 1 and
        sheet['H' + str(i)].value == 1 and
        sheet['I' + str(i)].value == 1 and
        sheet['J'+str(i)].value == 1):
        if sheet['K' + str(i)].value == None:
            sheet['K' + str(i)].value = msg
        else:
            sheet['K' + str(i)].value = sheet['K' + str(i)].value + ' + ' + msg
wb.save("table.xlsx")
