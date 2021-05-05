import sqlite3

connection = sqlite3.connect('shopApp.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE PRODUCT_TYPE(
    NAME VARCHAR(100) PRIMARY KEY
    )
    ;'''
)
cursor.execute('''CREATE TABLE PRODUCTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,PRODUCT_NAME VARCHAR(100),PRODUCT_TYPE
VARCHAR(100),PRODUCT_PRICE INTEGER,
FOREIGN KEY (PRODUCT_TYPE)
REFERENCES PRODUCT_TYPE (NAME)




);''')

cursor.execute('''CREATE TABLE ORDERS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(100),
    CPU VARCHAR(100),
    GPU VARCHAR(100),
    PSU VARCHAR(100),
    RAM VARCHAR(100),
    Case_ VARCHAR(100),
    Secondary_Motherboard VARCHAR(100),
    DateOfDelivery VARCHAR(100),
    price INTEGER,
    profit INTEGER
    )
    ;'''
)


cursor.execute('''INSERT INTO PRODUCT_TYPE VALUES('CPU');'''
)
cursor.execute('''INSERT INTO PRODUCT_TYPE VALUES('GPU');'''
)
cursor.execute('''INSERT INTO PRODUCT_TYPE VALUES('PSU');'''
)
cursor.execute('''INSERT INTO PRODUCT_TYPE VALUES('RAM');'''
)
cursor.execute('''INSERT INTO PRODUCT_TYPE VALUES('Case');'''
)
cursor.execute('''INSERT INTO PRODUCT_TYPE VALUES('Secondary_Motherboard');'''
)

cursor.execute('''CREATE TABLE HISTORY(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(100),
    DETAILS TEXT,
    DATEOFDELIVERY VARCHAR(100),
    price INTEGER,
    PROFIT INTEGER,
    MONTH INTEGER,
    YEAR INTEGER,
    STATUS VARCHAR(100)
    )
    ;'''
)



connection.commit()
cursor.close()
connection.close()
