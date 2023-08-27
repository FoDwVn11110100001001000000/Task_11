import sqlite3

commands={"1":"query_1.sql",
          "2":"query_2.sql",
          "3":"query_3.sql",
          "4":"query_4.sql",
          "5":"query_5.sql",
          "6":"query_6.sql",
          "7":"query_7.sql",
          "8":"query_8.sql",
          "9":"query_9.sql",
          "10":"query_10.sql"
        }

def take_info(sql: str) -> list:
    fd = open(sql, 'r')
    sql = fd.read()
    fd.close()
    with sqlite3.connect('my_data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    
if __name__ == '__main__':
    while True:
        x = input('Введіть команду: ')
        if x == 'exit':
            break
        if int(x) > 12:
            print('Цієї команди не існує введіть число від 1 до 10')
        else:
            print(take_info(commands[x]))