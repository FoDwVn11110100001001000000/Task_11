import sqlite3

def connector(sql):
    with sqlite3.connect('my_data.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

def create_db():
    with open('database.sql', 'r') as f:
        sql = f.read()
    
    connector(sql)



if __name__ == "__main__":
    create_db()