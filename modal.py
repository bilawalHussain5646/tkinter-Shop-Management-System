import sqlite3
from productClass import Products
from OrderDetails import Order


def FetchAllProducts():
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT ID,PRODUCT_NAME,PRODUCT_TYPE,PRODUCT_PRICE FROM PRODUCTS;"""
    )
    data: list = []
    result = cursor.fetchall()
    if result is None:
        data = None
    else:
        for d in result:
            data.append(d)
    connection.commit()
    cursor.close()
    connection.close()
    return data


def FetchOrder(ID):
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT ID,NAME,CPU,GPU,PSU,RAM,Case_,Secondary_Motherboard,DateOfDelivery,price,profit 
        FROM ORDERS WHERE ID = '{ID}';""".format(ID=ID, )
    )

    result = cursor.fetchone()
    if result is None:
        return None

    order = Order()
    order.ID = int(result[0])
    order.Name = result[1]
    order.CPU = result[2]
    order.GPU = result[3]
    order.PSU = result[4]
    order.RAM = result[5]
    order.Case = result[6]
    order.Secondary_Motherboard = result[7]
    order.DateOfDelivery = result[8]
    order.price = int(result[9])
    order.profit = int(result[10])
    connection.commit()
    cursor.close()
    connection.close()
    return order


def FetchProduct(ID):
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT ID,PRODUCT_NAME,PRODUCT_TYPE,PRODUCT_PRICE FROM PRODUCTS WHERE ID = '{ID}';""".format(ID=ID, )
    )

    result = cursor.fetchone()
    if result is None:
        return None

    product = Products()
    product.ID = int(result[0])
    product.PRODUCT_NAME = result[1]
    product.PRODUCT_TYPE = result[2]
    product.PRODUCT_PRICE = result[3]
    connection.commit()
    cursor.close()
    connection.close()
    return product


def InsertProduct(Item):
    PRODUCT_NAME = Item.PRODUCT_NAME
    PRODUCT_TYPE = Item.PRODUCT_TYPE
    PRODUCT_PRICE = Item.PRODUCT_PRICE

    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO PRODUCTS(PRODUCT_NAME,PRODUCT_TYPE,PRODUCT_PRICE) 
        VALUES('{PRODUCT_NAME}','{PRODUCT_TYPE}','{PRODUCT_PRICE}'); 
      """.format(PRODUCT_NAME=PRODUCT_NAME, PRODUCT_TYPE=PRODUCT_TYPE, PRODUCT_PRICE=PRODUCT_PRICE, )
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def FetchAllOrders():
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT ID,NAME,DateOfDelivery,price FROM ORDERS;"""
    )
    data: list = []

    result = cursor.fetchall()
    if result is None:
        data = None
    else:
        for d in result:
            data.append(d)
    connection.commit()
    cursor.close()
    connection.close()
    return data


def InsertOrder(Person):
    NAME = Person.Name
    CPU = Person.CPU
    GPU = Person.GPU
    PSU = Person.PSU
    RAM = Person.RAM
    Case_ = Person.Case
    Secondary_Motherboard = Person.Secondary_Motherboard
    DateOfDelivery = Person.DateOfDelivery
    price = Person.price
    profit = Person.profit
    # fetch price of each product
    # ---------------------------

    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO ORDERS(NAME,CPU,GPU,PSU,RAM,Case_,Secondary_Motherboard,DateOfDelivery,price,profit) 
        VALUES('{NAME}','{CPU}','{GPU}','{PSU}','{RAM}','{Case_}','{Secondary_Motherboard}','{DateOfDelivery}','{price}','{profit}'); 
      """.format(NAME=NAME, CPU=CPU, GPU=GPU, PSU=PSU, RAM=RAM, Case_=Case_,
                 Secondary_Motherboard=Secondary_Motherboard, DateOfDelivery=DateOfDelivery, price=price, profit=profit)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def UpdateProduct(PRODUCT):
    ID = PRODUCT.ID
    PRODUCT_NAME = PRODUCT.PRODUCT_NAME
    PRODUCT_TYPE = PRODUCT.PRODUCT_TYPE
    PRODUCT_PRICE = PRODUCT.PRODUCT_PRICE
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """UPDATE PRODUCTS SET PRODUCT_NAME='{PRODUCT_NAME}',PRODUCT_TYPE='{PRODUCT_TYPE}'
        ,PRODUCT_PRICE='{PRODUCT_PRICE}'
        WHERE ID = '{ID}'; 
        """.format(ID=ID, PRODUCT_NAME=PRODUCT_NAME, PRODUCT_TYPE=PRODUCT_TYPE, PRODUCT_PRICE=int(PRODUCT_PRICE), )
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def UpdateOrder(OrderDetails):
    ID = int(OrderDetails.ID)
    Name = OrderDetails.Name
    CPU = OrderDetails.CPU
    GPU = OrderDetails.GPU
    PSU = OrderDetails.PSU
    RAM = OrderDetails.RAM
    Case = OrderDetails.Case
    Secondary_Motherboard = OrderDetails.Secondary_Motherboard
    DateOfDelivery = OrderDetails.DateOfDelivery
    Price = OrderDetails.price
    profit = OrderDetails.profit
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)

    cursor = connection.cursor()

    cursor.execute(
        """UPDATE ORDERS SET NAME='{Name}',CPU='{CPU}',GPU='{GPU}',PSU='{PSU}',RAM='{RAM}',
        Case_='{Case}',Secondary_Motherboard='{Secondary_Motherboard}',DateOfDelivery='{DateOfDelivery}',price='{Price}',profit='{profit}' 
        WHERE ID = '{ID}'; 
        """.format(ID=ID, Name=Name, CPU=CPU, GPU=GPU, PSU=PSU, RAM=RAM,
                   Case=Case, Secondary_Motherboard=Secondary_Motherboard,
                   DateOfDelivery=DateOfDelivery, Price=Price, profit=profit)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def DeleteProduct(ID):
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """DELETE FROM PRODUCTS WHERE ID = '{ID}'; 
        """.format(ID=ID)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def DeleteOrder(ID):
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """DELETE FROM ORDERS WHERE ID = '{ID}'; 
        """.format(ID=ID)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def fetchRespectiveData():
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_TYPE='CPU';"""
    )
    CPU = ['']
    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            CPU.append(d[0])

    cursor.execute(
        """SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_TYPE='GPU';"""
    )
    GPU = ['']
    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            GPU.append(d[0])

    cursor.execute(
        """SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_TYPE='PSU';"""
    )
    PSU = ['']
    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            PSU.append(d[0])

    cursor.execute(
        """SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_TYPE='RAM';"""
    )
    RAM = ['']
    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            RAM.append(d[0])

    cursor.execute(
        """SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_TYPE='Case';"""
    )
    Case = ['']
    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            Case.append(d[0])

    cursor.execute(
        """SELECT PRODUCT_NAME FROM PRODUCTS WHERE PRODUCT_TYPE='Secondary_Motherboard';"""
    )
    Secondary_Motherboard = ['']
    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            Secondary_Motherboard.append(d[0])
    connection.commit()
    cursor.close()
    connection.close()

    return CPU, GPU, PSU, RAM, Case, Secondary_Motherboard


def PricesAndTotal(OrderDetails):
    CPU = OrderDetails.CPU
    GPU = OrderDetails.GPU
    PSU = OrderDetails.PSU
    RAM = OrderDetails.RAM
    Case = OrderDetails.Case
    Secondary_Motherboard = OrderDetails.Secondary_Motherboard
    totalPrice = 0
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)

    cursor = connection.cursor()

    cursor.execute(
        """SELECT PRODUCT_PRICE FROM PRODUCTS WHERE PRODUCT_TYPE='CPU' AND PRODUCT_NAME = '{CPU}';""".format(CPU=CPU, )
    )
    result = cursor.fetchone()
    if result is None:
        totalPrice = totalPrice + 0

    else:
        totalPrice += result[0]

    cursor.execute(
        """SELECT PRODUCT_PRICE FROM PRODUCTS WHERE PRODUCT_TYPE='GPU' AND PRODUCT_NAME = '{GPU}';""".format(GPU=GPU, )
    )

    result = cursor.fetchone()
    if result is None:
        totalPrice = totalPrice + 0

    else:
        totalPrice += result[0]

    cursor.execute(
        """SELECT PRODUCT_PRICE FROM PRODUCTS WHERE PRODUCT_TYPE='PSU' AND PRODUCT_NAME = '{PSU}';""".format(PSU=PSU, )
    )
    result = cursor.fetchone()
    if result is None:
        totalPrice = totalPrice + 0

    else:
        totalPrice += result[0]

    cursor.execute(
        """SELECT PRODUCT_PRICE FROM PRODUCTS WHERE PRODUCT_TYPE='RAM' AND PRODUCT_NAME = '{RAM}';""".format(RAM=RAM, )
    )

    result = cursor.fetchone()
    if result is None:
        totalPrice = totalPrice + 0

    else:
        totalPrice += result[0]

    cursor.execute(
        """SELECT PRODUCT_PRICE FROM PRODUCTS WHERE PRODUCT_TYPE='Case' AND PRODUCT_NAME = '{Case}';""".format(
            Case=Case, )
    )

    result = cursor.fetchone()
    if result is None:
        totalPrice = totalPrice + 0

    else:
        totalPrice += result[0]

    cursor.execute(
        """SELECT PRODUCT_PRICE FROM PRODUCTS WHERE PRODUCT_TYPE='Secondary_Motherboard' AND 
        PRODUCT_NAME = '{Secondary_Motherboard}';""".format(Secondary_Motherboard=Secondary_Motherboard, )
    )
    result = cursor.fetchone()
    if result is None:
        totalPrice = totalPrice + 0

    else:
        totalPrice += result[0]
    connection.commit()
    cursor.close()
    connection.close()
    profit = (totalPrice * 10) / 100
    totalPrice = profit + totalPrice
    return totalPrice, profit


def InsertHistory(ID):
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(
        """SELECT NAME,CPU,GPU,PSU,RAM,Case_,Secondary_Motherboard,DateOfDelivery,price,profit 
        FROM ORDERS WHERE ID = '{ID}';""".format(ID=ID, )
    )
    result = cursor.fetchone()
    NAME = result[0]
    tempDetails = ''
    for i in range(6):
        if result[i + 1] == '':
            pass
        else:
            tempDetails = result[i + 1] + ", " + tempDetails
    Details = ''
    for i in range(len(tempDetails) - 2):
        Details += tempDetails[i]

    DateOfDelivery = result[7]
    Date_ = DateOfDelivery.split('/', 3)
    YEAR = int(Date_[2])
    Month = int(Date_[0])
    price = result[8]
    profit = result[9]
    Status = "Delivered"

    cursor.execute(
        """INSERT INTO HISTORY(NAME,DETAILS,DATEOFDELIVERY,price,PROFIT,MONTH,YEAR,STATUS) 
        VALUES('{NAME}','{Details}','{DateOfDelivery}','{price}','{Profit}','{Month}','{YEAR}','{Status}'); 
      """.format(NAME=NAME, Details=Details, DateOfDelivery=DateOfDelivery, price=price, Profit=profit, Month=Month,
                 YEAR=YEAR,
                 Status=Status)
    )
    cursor.execute(
        """DELETE FROM ORDERS WHERE ID = '{ID}'; 
        """.format(ID=ID)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True


def FetchReport(Year, Month):
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    if Month == 'ALL':
        cursor.execute(
            """SELECT COUNT(ID),SUM(price),SUM(PROFIT) FROM HISTORY 
            WHERE YEAR='{Year}';""".format(Year=Year)
        )
    else:
        cursor.execute(
            """SELECT COUNT(ID),SUM(price),SUM(PROFIT) FROM HISTORY 
            WHERE YEAR='{Year}' AND MONTH = '{Month}';""".format(Year=Year, Month=Month)
        )
    data: list = []

    result = cursor.fetchall()
    if result is None:
        data = None
    else:
        for d in result:
            data.append(d)
    connection.commit()
    cursor.close()
    connection.close()
    return data


def FetchAllYears():
    connection = sqlite3.connect('shopApp.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT DISTINCT(YEAR) FROM HISTORY;"""
    )
    data: list = ['']

    result = cursor.fetchall()
    if result is None:
        pass
    else:
        for d in result:
            data.append(d[0])
    connection.commit()
    cursor.close()
    connection.close()
    return data
