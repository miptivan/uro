import sqlite3
import config
import random
import openpyxl


'''wb = openpyxl.reader.excel.load_workbook(filename="C:/Users/mipti/Desktop/table.xlsx")
wb.active = 0
sheet = wb.active'''


db = sqlite3.connect('server.db', check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    current_state TEXT,
    q1 INTEGER,
    q2 INTEGER,
    q3 INTEGER,
    q4 INTEGER,
    q5 INTEGER,
    q6 INTEGER,
    q7 INTEGER,
    q8 INTEGER,
    q9 INTEGER,
    q10 INTEGER 
)""")


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    sql.execute(f"SELECT username FROM users WHERE username = '{user_id}'")
    sqlite_insert_query = f"""UPDATE users SET
                              current_state = '{value}'
                              WHERE username = '{user_id}'"""
    sql.execute(sqlite_insert_query)
    db.commit()


def create_user(user_id):
    sql.execute(f"SELECT username FROM users WHERE username = '{user_id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, None, None, None, None, None, None, None, None, None, None, None))  # Создать строчку юзера
    else:
        #  sql.execute(f"""UPDATE users SET username = '{user_id}' WHERE username = '{user_id}'""")
        print('Такой профиль уже есть')
    db.commit()


def get_current_state(user_id):
    sql.execute(f"SELECT current_state FROM users WHERE username = '{user_id}'")
    a = sql.fetchone()[0]
    print(a)
    return a


def set_question(user_id, value, column):
    sqlite_insert_query = f"""UPDATE users SET
                                  '{column}' = '{value}'
                                  WHERE username = '{user_id}'"""
    sql.execute(sqlite_insert_query)
    db.commit()


def search(user_id):
    sql.execute(f"SELECT q1 FROM users WHERE username = '{user_id}'")
    q1 = sql.fetchone()[0]
    sql.execute(f"SELECT q2 FROM users WHERE username = '{user_id}'")
    q2 = sql.fetchone()[0]
    sql.execute(f"SELECT q3 FROM users WHERE username = '{user_id}'")
    q3 = sql.fetchone()[0]
    sql.execute(f"SELECT q4 FROM users WHERE username = '{user_id}'")
    q4 = sql.fetchone()[0]
    sql.execute(f"SELECT q5 FROM users WHERE username = '{user_id}'")
    q5 = sql.fetchone()[0]
    sql.execute(f"SELECT q6 FROM users WHERE username = '{user_id}'")
    q6 = sql.fetchone()[0]
    sql.execute(f"SELECT q7 FROM users WHERE username = '{user_id}'")
    q7 = sql.fetchone()[0]
    sql.execute(f"SELECT q8 FROM users WHERE username = '{user_id}'")
    q8 = sql.fetchone()[0]
    sql.execute(f"SELECT q9 FROM users WHERE username = '{user_id}'")
    q9 = sql.fetchone()[0]
    sql.execute(f"SELECT q10 FROM users WHERE username = '{user_id}'")
    q10 = sql.fetchone()[0]

    sql.execute(f"SELECT res FROM results WHERE q1 = '{q1}' AND q2 = '{q2}' AND q3 = '{q3}' AND q4 = '{q4}' AND "
                f"q5 = '{q5}' AND q6 = '{q6}' AND q7 = '{q7}' AND q8 = '{q8}' AND q9 = '{q9}' AND q10 = '{q10}'")
    res = sql.fetchone()[0]

    '''for i in range(1, 3457):
        if (str(sheet['A' + str(i)].value) == str(q1) and
                str(sheet['B' + str(i)].value) == str(q2) and
                str(sheet['C' + str(i)].value) == str(q3) and
                str(sheet['D' + str(i)].value) == str(q4) and
                str(sheet['E' + str(i)].value) == str(q5) and
                str(sheet['F' + str(i)].value) == str(q6) and
                str(sheet['G' + str(i)].value) == str(q7) and
                str(sheet['H' + str(i)].value) == str(q8) and
                str(sheet['I' + str(i)].value) == str(q9) and
                str(sheet['J' + str(i)].value) == str(q10)):
            print('EBAAAT ', sheet['k' + str(i)].value)
            return str(sheet['k' + str(i)].value)'''
    return res


