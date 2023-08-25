import sqlite3

from table import tables

class DataBase:
    @classmethod
    def create_db() -> None:
        with open('MyDataBase.db', 'r') as f:
            sql = f.read()

        with sqlite3.connect('MyDataBase.db') as con:
            cur = con.cursor()
            cur.executescript(sql)

    @classmethod
    def create_table():
        dataset = list()

        for table_info in tables:
            table_name = table_info['name']
            strings = ', '.join([i for i in table_info['data']])

        insert_query = f"INSERT INTO {table_name} VALUES ({strings})"
        dataset.append(insert_query)

        with sqlite3.connect('MyDataBase.sql') as con:
            cur = con.cursor()
            cur.executescript(dataset)
        

    
    # def create_columns(self) -> None:
    #     column = list()
    #     for table_info in tables:
    #         table_name = table_info['name']
    #         columns = ', '.join([f'{col_name} {col_type}' for col_name, col_type in table_info['columns']])
    #         create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    #         column.append(create_table_query)

    #     with sqlite3.connect('MyDataBase.sql') as con:
    #         cur = con.cursor()
    #         cur.executescript(column)
        






if __name__ == "__main__":
    DataBase
