import configparser
import mysql.connector
from mysql.connector import Error
class DBConnection:
    'establish a singleton connection with db'
    '''this class will create only one instance'''
    __instance = None

    def __new__(cls):
        '''override to implement singleton 
        Ensures only one instance of DBConnection is ever created'''
        if cls.__instance is None:#if no instance created
            cls.__instance = super(DBConnection, cls).__new__(cls)
            cls.__instance.__initialize()#initialize the connection 
        return cls.__instance
    def __initialize(self):
        '''
        initialize the database connection using properties from the db_config.ini
        '''
        try:
            # load the configuration file
            config = configparser.ConfigParser()
            config.read("db_config.ini")
            # establish the Mysql connection
            self.connection = mysql.connector.connect(
                host = config.get("mysql","host"),
                user = config.get("mysql","user"),
                password = config.get("mysql","password"),
                database = config.get("mysql","database")
            )
            if self.connection.is_connected():
                print('Connected to MYSQL database...')
        except Error as e:
            print(f'Error while connecting to MYSQL:{e}')
            self.connection = None

    def get_connection(self):
        return self.connection

