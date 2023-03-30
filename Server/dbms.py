import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='database-1.c5kmzx0rtavj.ap-northeast-1.rds.amazonaws.com',
            user='admin',
            password='Eigen100%bot',
            database='myapp_production_db'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection

    except Error as e:
        print(f'Error connecting to MySQL database: {e}')

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print('Connection to MySQL database closed')

