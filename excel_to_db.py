import openpyxl
import sqlite3

wb = openpyxl.reader.excel.load_workbook(filename="C:/Users/mipti/Desktop/table.xlsx")
wb.active = 0
sheet = wb.active
print(sheet['D1'].value)

db = sqlite3.connect('server.db', check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS results (
    q1 INTEGER,
    q2 INTEGER,
    q3 INTEGER,
    q4 INTEGER,
    q5 INTEGER,
    q6 INTEGER,
    q7 INTEGER,
    q8 INTEGER,
    q9 INTEGER,
    q10 INTEGER,
    res TEXT
)""")


# добавляем всё из экселя в бд
def add_lines():
    for i in range(1, 3457):
        q1 = int(sheet['A' + str(i)].value)
        q2 = int(sheet['B' + str(i)].value)
        q3 = int(sheet['C' + str(i)].value)
        q4 = int(sheet['D' + str(i)].value)
        q5 = int(sheet['E' + str(i)].value)
        q6 = int(sheet['F' + str(i)].value)
        q7 = int(sheet['G' + str(i)].value)
        q8 = int(sheet['H' + str(i)].value)
        q9 = int(sheet['I' + str(i)].value)
        q10 = int(sheet['J' + str(i)].value)
        res = str(sheet['K' + str(i)].value)
        sql.execute(f"INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, res))
        db.commit()
