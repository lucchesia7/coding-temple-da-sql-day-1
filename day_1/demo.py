from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()
class PGSQL:
    __user = getenv("USER")
    __password = getenv("PASSWORD")
    __server = getenv("SERVER")
    __pg_con = psycopg2.connect(
        dbname=__user,
        user=__user,
        password=__password,
        host=__server
        )
    __cur = __pg_con.cursor()

    def create_tables(self, sql_filepath: str):
        start = self.create_file(sql_filepath)
        tables = start.split(';')
        for table in tables:
            try:
                print(table)
                self.__cur.execute(table)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command Skipped: {msg}')
        
    def insert_data(self, sql_filepath: str):
        start = self.create_file(sql_filepath)
        commands = start.split(';')
        for command in commands:
            try:
                print(command)
                self.__cur.execute(command)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(command)
                print(f'Command Skipped: {msg}')
                
    def query_db(self, sql_filepath: str):
        start = self.create_file(sql_filepath)
        queries = start.split(';')
        for query in queries:
            try:
                print(query)
                self.__cur.execute(query)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:

    @staticmethod
    def create_file(fpath: str):
        """ Open a file by filepath and apply it to an SQL table """
        with open(fpath, 'r') as f:
            sql_file = f.read()
            f.close()
        return sql_file


if __name__ == '__main__':
    p = PGSQL()
    p.create_tables(r'C:\Users\Alex Lucchesi\coding-temple\coding_temple_da_sql_week\postgresql\day_1\amazon_mock_create (1).sql')
    p.insert_data(r'C:\Users\Alex Lucchesi\coding-temple\coding_temple_da_sql_week\postgresql\day_1\amazon_mock_insert (1).sql')
