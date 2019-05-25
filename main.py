import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='sql2.freesqldatabase.com',
            user='sql2293245',
            password='pX4!eJ8%',
            db='sql2293245'
        )
        self.cursor = self.connection.cursor()   

        print('Conexion establecida.') 

myfreedb = DataBase()

