import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv('HOST')
LOG = os.getenv('LOG')
PASSWORD = os.getenv('PASSWORD')
DB = os.getenv('DB')

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = HOST,
            user = LOG,
            password = PASSWORD,
            db = DB
        )
        self.cursor = self.connection.cursor()   
        print('Conexion establecida.') 
    
    def showDB(self):
        sqlQuery= "SHOW DATABASES"
        self.cursor.execute(sqlQuery)
        print('-----DATABASE-----')
        print (self.cursor.fetchall())
    
    def showTables(self):
        sqlQuery= "SHOW TABLES"
        self.cursor.execute(sqlQuery)
        print('-----TABLAS-----')
        print (self.cursor.fetchall())

    def createEmployeeTable(self):
        sqlQuery= 'DROP TABLE IF EXISTS Employee'
        self.cursor.execute(sqlQuery)
        sqlQuery= '''
        CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)  
        '''
        self.cursor.execute(sqlQuery)
    
    def createCustomersTable(self):
        sqlQuery= 'DROP TABLE IF EXISTS customers'
        self.cursor.execute(sqlQuery)
        sqlQuery= '''
        CREATE TABLE customers (
            customerNumber int(11) NOT NULL,
            customerName varchar(50) NOT NULL,
            contactLastName varchar(50) NOT NULL,
            contactFirstName varchar(50) NOT NULL,
            phone varchar(50) NOT NULL,
            addressLine1 varchar(50) NOT NULL,
            addressLine2 varchar(50) DEFAULT NULL,
            city varchar(50) NOT NULL,
            state varchar(50) DEFAULT NULL,
            postalCode varchar(15) DEFAULT NULL,
            country varchar(50) NOT NULL,
            salesRepEmployeeNumber int(11) DEFAULT NULL,
            creditLimit decimal(10,2) DEFAULT NULL,
            PRIMARY KEY (customerNumber)
        )
        '''
        self.cursor.execute(sqlQuery)

    def insertCustomers(self):
        sqlQuery='''
        insert  into `customers`(`customerNumber`,`customerName`,`contactLastName`,`contactFirstName`,`phone`,`addressLine1`,`addressLine2`,`city`,`state`,`postalCode`,`country`,`salesRepEmployeeNumber`,`creditLimit`) values 
        (103,'Atelier graphique','Schmitt','Carine ','40.32.2555','54, rue Royale',NULL,'Nantes',NULL,'44000','France',1370,'21000.00'),
        (112,'Signal Gift Stores','King','Jean','7025551838','8489 Strong St.',NULL,'Las Vegas','NV','83030','USA',1166,'71800.00'),
        (114,'Australian Collectors, Co.','Ferguson','Peter','03 9520 4555','636 St Kilda Road','Level 3','Melbourne','Victoria','3004','Australia',1611,'117300.00'),
        (119,'La Rochelle Gifts','Labrune','Janine ','40.67.8555','67, rue des Cinquante Otages',NULL,'Nantes',NULL,'44000','France',1370,'118200.00');
        '''
        self.cursor.execute(sqlQuery)

    def selectCustomers(self):
        sqlQuery= 'SELECT * FROM customers'
        self.cursor.execute(sqlQuery)
        return self.cursor.fetchall()


myfreedb= DataBase()
myfreedb.showDB()
myfreedb.createEmployeeTable()
myfreedb.createCustomersTable()
myfreedb.showTables()
myfreedb.insertCustomers()
customers= myfreedb.selectCustomers()
print(customers)
print('Name: {}'.format(customers[0][1]))