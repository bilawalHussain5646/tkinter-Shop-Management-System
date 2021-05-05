import tkinter as tkr
from tkinter import *
from tkinter.ttk import Notebook
import modal as query
from OrderDetails import Order
from productClass import Products
from tkcalendar import *

# # general things
# # -----------------------
FONT = "Arial"
headingFont = 24
paragraphFont = 14
popupresolution = "500x500"

# window
# -----------------------
master = Tk()

Title = Frame(master)
Content = Frame(master)

LeftContent = Frame(Content)
RightContent = Frame(Content)

my_scrollbar = Scrollbar(LeftContent, orient=VERTICAL)
myList = Listbox(LeftContent, yscrollcommand=my_scrollbar.set, font=(FONT, paragraphFont))

tablayout = Notebook(LeftContent)
productsTab = Notebook(LeftContent)
orderTab = Notebook(LeftContent)

# product layout
products = Frame(productsTab)
products.pack(fill="both")

# Order layout
Orderss = Frame(orderTab)
Orderss.pack(fill="both")

# Review layout
tab1 = Frame(tablayout)
tab1.pack(fill="both")

tablayout2 = Notebook(RightContent)
tab2 = Frame(tablayout2)
tab2.pack(fill="both")
# scrollbar here
my_scrollbar.config(command=myList.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)


# Database Option
# -----------------------

def ResetWindow():
    global myList
    myList.delete(0, END)
    myList.pack_forget()
    tablayout.pack_forget()
    tablayout2.pack_forget()

    productsTab.pack_forget()
    orderTab.pack_forget()
    for widget in RightContent.winfo_children():
        widget.pack_forget()


# Adding Product
# Work : Done
def AddComponentProduct():
    PopUpWindowProduct = Toplevel()

    ProductCanvas = Canvas(PopUpWindowProduct, width=400, height=300)
    ProductCanvas.pack()
    Title_Name = Label(PopUpWindowProduct, text="BUSINESS HELPER", font=(FONT, paragraphFont),
                       fg="white", anchor=N, background="black", width=400)
    ProductCanvas.create_window(200, 10, window=Title_Name)

    ProductNameLabel = Label(PopUpWindowProduct, text="Name")
    ProductCanvas.create_window(50, 50, window=ProductNameLabel)

    Product_Name = Entry(PopUpWindowProduct)
    ProductCanvas.create_window(200, 50, window=Product_Name, width=200)
    defaultValue = StringVar(PopUpWindowProduct)

    choices = {'CPU', 'GPU', 'PSU', 'RAM', 'Case', 'Secondary_Motherboard'}
    defaultValue.set('CPU')  # set the default option

    TypeLabel = Label(PopUpWindowProduct, text="Type")
    ProductCanvas.create_window(50, 80, window=TypeLabel)
    Product_Type = OptionMenu(PopUpWindowProduct, defaultValue, *choices)
    ProductCanvas.create_window(200, 80, window=Product_Type, width=200)

    PriceLabel = Label(PopUpWindowProduct, text="Type")
    ProductCanvas.create_window(50, 110, window=PriceLabel)
    Product_Price = Entry(PopUpWindowProduct)
    ProductCanvas.create_window(200, 110, window=Product_Price, width=200)

    def getProductName():
        return Product_Name.get()

    def getProductType():
        return defaultValue.get()

    def getProductPrice():
        return Product_Price.get()

    def saveDataProduct():
        product = Products()
        product.PRODUCT_NAME = getProductName()
        product.PRODUCT_TYPE = getProductType()
        product.PRODUCT_PRICE = int(getProductPrice())

        result = query.InsertProduct(product)
        if result:
            PopUpWindowProduct.destroy()

    SaveDetails = Button(PopUpWindowProduct, text='SAVE', command=saveDataProduct)
    ProductCanvas.create_window(200, 140, window=SaveDetails, width=200)

    PopUpWindowProduct.title("Add Product")
    PopUpWindowProduct.geometry(popupresolution)
    PopUpWindowProduct.resizable(False, False)


# Adding Order
# Work : Done
def AddOrder():
    PopUpWindow = Toplevel()
    OrderCanvas = Canvas(PopUpWindow, width=400, height=600)
    OrderCanvas.pack()
    Title_Name = Label(PopUpWindow, text="BUSINESS HELPER", font=(FONT, paragraphFont),
                       fg="white", anchor=N, background="black", width=400)
    OrderCanvas.create_window(200, 10, window=Title_Name)

    NameLabel = Label(PopUpWindow, text="Name")
    OrderCanvas.create_window(78, 50, window=NameLabel)
    Name = Entry(PopUpWindow)
    OrderCanvas.create_window(200, 50, window=Name, width=200)

    defaultCPU = StringVar(PopUpWindow)
    defaultGPU = StringVar(PopUpWindow)
    defaultPSU = StringVar(PopUpWindow)
    defaultRAM = StringVar(PopUpWindow)
    defaultCase = StringVar(PopUpWindow)
    defaultSecondary_Motherboard = StringVar(PopUpWindow)

    CPU, GPU, PSU, RAM, Case, Secondary_Motherboard = query.fetchRespectiveData()

    defaultCPU.set('')

    CPULabel = Label(PopUpWindow, text="CPU")
    OrderCanvas.create_window(80, 80, window=CPULabel)

    CPU = OptionMenu(PopUpWindow, defaultCPU, *CPU)
    OrderCanvas.create_window(200, 80, window=CPU, width=200)

    defaultGPU.set('')

    GPULabel = Label(PopUpWindow, text="GPU")
    OrderCanvas.create_window(80, 110, window=GPULabel)
    GPU = OptionMenu(PopUpWindow, defaultGPU, *GPU)
    OrderCanvas.create_window(200, 110, window=GPU, width=200)

    defaultPSU.set('')

    PSULabel = Label(PopUpWindow, text="PSU")
    OrderCanvas.create_window(80, 140, window=PSULabel)
    PSU = OptionMenu(PopUpWindow, defaultPSU, *PSU)
    OrderCanvas.create_window(200, 140, window=PSU, width=200)

    defaultRAM.set('')

    RAMLabel = Label(PopUpWindow, text="RAM")
    OrderCanvas.create_window(80, 170, window=RAMLabel)
    RAM = OptionMenu(PopUpWindow, defaultRAM, *RAM)
    OrderCanvas.create_window(200, 170, window=RAM, width=200)

    defaultSecondary_Motherboard.set('')

    Secondary_MotherboardLabel = Label(PopUpWindow, text="Secondary Motherboard")
    OrderCanvas.create_window(30, 200, window=Secondary_MotherboardLabel)
    Secondary_Motherboard = OptionMenu(PopUpWindow, defaultSecondary_Motherboard, *Secondary_Motherboard)
    OrderCanvas.create_window(200, 200, window=Secondary_Motherboard, width=200)

    defaultCase.set('')

    CaseLabel = Label(PopUpWindow, text="Case")
    OrderCanvas.create_window(78, 230, window=CaseLabel)
    Case = OptionMenu(PopUpWindow, defaultCase, *Case)
    OrderCanvas.create_window(200, 230, window=Case, width=200)

    DateOfDeliveryLabel = Label(PopUpWindow, text="Date Of Delivery")
    OrderCanvas.create_window(45, 350, window=DateOfDeliveryLabel)
    DateOfDelivery = Calendar(PopUpWindow, selectmode="day", year=2021, month=4, day=3)
    OrderCanvas.create_window(200, 350, window=DateOfDelivery, width=200)

    def getName():
        return Name.get()

    def getCPU():
        return defaultCPU.get()

    def getGPU():
        return defaultGPU.get()

    def getPSU():
        return defaultPSU.get()

    def getRAM():
        return defaultRAM.get()

    def getSecondary_Motherboard():
        return defaultSecondary_Motherboard.get()

    def getCase():
        return defaultCase.get()

    def getDateOfDelivery():
        return DateOfDelivery.get_date()

    def saveData():
        order = Order()
        order.Name = getName()
        order.CPU = getCPU()
        order.GPU = getGPU()
        order.PSU = getPSU()
        order.RAM = getRAM()
        order.Case = getCase()
        order.Secondary_Motherboard = getSecondary_Motherboard()
        order.DateOfDelivery = getDateOfDelivery()
        order.price, order.profit = query.PricesAndTotal(order)

        result = query.InsertOrder(order)
        if result:
            PopUpWindow.destroy()

    SaveDetails = Button(PopUpWindow, text='Save', command=saveData)
    OrderCanvas.create_window(200, 460, window=SaveDetails, width=200)

    PopUpWindow.title("Order Details")
    PopUpWindow.geometry(popupresolution)
    PopUpWindow.resizable(False, False)


# Edit Order
# Work : Done
def EditOrder(OrderDetails):
    PopUpWindow = Toplevel()
    OrderCanvas = Canvas(PopUpWindow, width=400, height=620)
    OrderCanvas.pack()
    Title_Name = Label(PopUpWindow, text="BUSINESS HELPER", font=(FONT, paragraphFont),
                       fg="white", anchor=N, background="black", width=400)
    OrderCanvas.create_window(200, 10, window=Title_Name)

    NameLabel = Label(PopUpWindow, text="Name")
    OrderCanvas.create_window(78, 50, window=NameLabel)
    Name = Entry(PopUpWindow)
    OrderCanvas.create_window(200, 50, window=Name, width=200)

    defaultCPU = StringVar(PopUpWindow)
    defaultGPU = StringVar(PopUpWindow)
    defaultPSU = StringVar(PopUpWindow)
    defaultRAM = StringVar(PopUpWindow)
    defaultCase = StringVar(PopUpWindow)
    defaultSecondary_Motherboard = StringVar(PopUpWindow)

    CPU, GPU, PSU, RAM, Case, Secondary_Motherboard = query.fetchRespectiveData()

    defaultCPU.set(OrderDetails.CPU)  # set the default option

    CPULabel = Label(PopUpWindow, text="CPU")
    OrderCanvas.create_window(80, 80, window=CPULabel)
    CPU = OptionMenu(PopUpWindow, defaultCPU, *CPU)
    OrderCanvas.create_window(200, 80, window=CPU, width=200)

    defaultGPU.set(OrderDetails.GPU)  # set the default option

    GPULabel = Label(PopUpWindow, text="GPU")
    OrderCanvas.create_window(80, 110, window=GPULabel)
    GPU = OptionMenu(PopUpWindow, defaultGPU, *GPU)
    OrderCanvas.create_window(200, 110, window=GPU, width=200)

    defaultPSU.set(OrderDetails.PSU)  # set the default option

    PSULabel = Label(PopUpWindow, text="PSU")
    OrderCanvas.create_window(80, 140, window=PSULabel)
    PSU = OptionMenu(PopUpWindow, defaultPSU, *PSU)
    OrderCanvas.create_window(200, 140, window=PSU, width=200)

    defaultRAM.set(OrderDetails.RAM)  # set the default option

    RAMLabel = Label(PopUpWindow, text="RAM")
    OrderCanvas.create_window(80, 170, window=RAMLabel)
    RAM = OptionMenu(PopUpWindow, defaultRAM, *RAM)
    OrderCanvas.create_window(200, 170, window=RAM, width=200)

    defaultSecondary_Motherboard.set(OrderDetails.Secondary_Motherboard)  # set the default option

    Secondary_MotherboardLabel = Label(PopUpWindow, text="Secondary Motherboard")
    OrderCanvas.create_window(30, 200, window=Secondary_MotherboardLabel)
    Secondary_Motherboard = OptionMenu(PopUpWindow, defaultSecondary_Motherboard, *Secondary_Motherboard)
    OrderCanvas.create_window(200, 200, window=Secondary_Motherboard, width=200)

    defaultCase.set(OrderDetails.Case)  # set the default option
    CaseLabel = Label(PopUpWindow, text="Case")
    OrderCanvas.create_window(78, 230, window=CaseLabel)
    Case = OptionMenu(PopUpWindow, defaultCase, *Case)
    OrderCanvas.create_window(200, 230, window=Case, width=200)

    DateOfDeliveryLabel = Label(PopUpWindow, text="Date Of Delivery")
    OrderCanvas.create_window(45, 350, window=DateOfDeliveryLabel)
    dateSelected = OrderDetails.DateOfDelivery.split('/', 3)
    DateOfDelivery = Calendar(PopUpWindow, selectmode="day", year=int(dateSelected[2]),
                              month=int(dateSelected[0]), day=int(dateSelected[1]))
    OrderCanvas.create_window(200, 350, window=DateOfDelivery, width=200)

    Name.insert(0, OrderDetails.Name)

    def getID():
        return OrderDetails.ID

    def getName():
        return Name.get()

    def getCPU():
        return defaultCPU.get()

    def getGPU():
        return defaultGPU.get()

    def getPSU():
        return defaultPSU.get()

    def getRAM():
        return defaultRAM.get()

    def getSecondary_Motherboard():
        return defaultSecondary_Motherboard.get()

    def getCase():
        return defaultCase.get()

    def getDateOfDelivery():
        return DateOfDelivery.get_date()

    def updateData():
        order = Order()

        order.ID = getID()
        order.Name = getName()
        order.CPU = getCPU()
        order.GPU = getGPU()
        order.PSU = getPSU()
        order.RAM = getRAM()
        order.Case = getCase()
        order.Secondary_Motherboard = getSecondary_Motherboard()
        order.DateOfDelivery = getDateOfDelivery()
        order.price, order.profit = query.PricesAndTotal(order)

        result = query.UpdateOrder(order)
        if result:
            PopUpWindow.destroy()

    SaveDetails = Button(PopUpWindow, text='UPDATE', command=updateData)
    OrderCanvas.create_window(200, 490, window=SaveDetails, width=200)

    PopUpWindow.title("Order Update")
    PopUpWindow.geometry(popupresolution)
    PopUpWindow.resizable(False, False)

    # sql query here for Edit


# Edit Product
# Work:
def EditProduct(ProductDetails):
    PopUpWindowProduct = Toplevel()

    ProductCanvas = Canvas(PopUpWindowProduct, width=400, height=300)
    ProductCanvas.pack()
    Title_Name = Label(PopUpWindowProduct, text="BUSINESS HELPER", font=(FONT, paragraphFont),
                       fg="white", anchor=N, background="black", width=400)
    ProductCanvas.create_window(200, 10, window=Title_Name)

    ProductNameLabel = Label(PopUpWindowProduct, text="Name")
    ProductCanvas.create_window(50, 50, window=ProductNameLabel)
    Product_Name = Entry(PopUpWindowProduct)
    ProductCanvas.create_window(200, 50, window=Product_Name, width=200)

    defaultValue = StringVar(PopUpWindowProduct)

    choices = {'CPU', 'GPU', 'PSU', 'RAM', 'Case', 'Secondary_Motherboard'}
    defaultValue.set(ProductDetails.PRODUCT_TYPE)  # set the default option

    TypeLabel = Label(PopUpWindowProduct, text="Type")
    ProductCanvas.create_window(50, 80, window=TypeLabel)
    Product_Type = OptionMenu(PopUpWindowProduct, defaultValue, *choices)
    ProductCanvas.create_window(200, 80, window=Product_Type, width=200)

    PriceLabel = Label(PopUpWindowProduct, text="Type")
    ProductCanvas.create_window(50, 110, window=PriceLabel)
    Product_Price = Entry(PopUpWindowProduct)
    ProductCanvas.create_window(200, 110, window=Product_Price, width=200)

    Product_Name.insert(0, ProductDetails.PRODUCT_NAME)
    Product_Price.insert(0, ProductDetails.PRODUCT_PRICE)

    def getProductID():
        return ProductDetails.ID

    def getProductName():
        return Product_Name.get()

    def getProductType():
        return defaultValue.get()

    def getProductPrice():
        return Product_Price.get()

    def saveDataProduct():
        product = Products()
        product.ID = int(getProductID())
        product.PRODUCT_NAME = getProductName()
        product.PRODUCT_TYPE = getProductType()
        product.PRODUCT_PRICE = int(getProductPrice())

        result = query.UpdateProduct(product)
        if result:
            PopUpWindowProduct.destroy()

    SaveDetails = Button(PopUpWindowProduct, text='SAVE', command=saveDataProduct)
    ProductCanvas.create_window(200, 140, window=SaveDetails, width=200)

    PopUpWindowProduct.title("Edit Product")
    PopUpWindowProduct.geometry(popupresolution)
    PopUpWindowProduct.resizable(False, False)


# Showing Database
# Work : Done
def show_DataBase():
    ResetWindow()

    global LeftContent
    global RightContent

    global my_scrollbar
    global myList

    def deleteData(btn):
        row = btn.grid_info()['row']
        column = btn.grid_info()['column']
        print("Column : " + str(column) + " Row : " + str(row))
        widget = products.grid_slaves(row=row, column=0)[0]
        widget2 = products.grid_slaves(row=row, column=1)[0]
        widget3 = products.grid_slaves(row=row, column=2)[0]
        widget4 = products.grid_slaves(row=row, column=3)[0]
        widget5 = products.grid_slaves(row=row, column=4)[0]
        widget6 = products.grid_slaves(row=row, column=5)[0]

        print(str(widget.cget("text")))
        # --------------------------
        query.DeleteProduct(int(widget.cget("text")))
        # Delete Here #
        # -------------------
        for widget in products.winfo_children():
            widget.destroy()
        Data = query.FetchAllProducts()
        for R in range(len(Data)):
            for column in range(6):
                if R == 0:
                    if column == 5:
                        label = Label(products, text="Action", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    elif column == 4:
                        label = Label(products, text="Action", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        products.grid_columnconfigure(column, weight=1)
                    elif column == 0:
                        label = Label(products, text="ID", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        products.grid_columnconfigure(column, weight=1)
                    elif column == 1:
                        label = Label(products, text="PRODUCT NAME", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        products.grid_columnconfigure(column, weight=1)
                    elif column == 2:
                        label = Label(products, text="PRODUCT TYPE", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        products.grid_columnconfigure(column, weight=1)
                    elif column == 3:
                        label = Label(products, text="PRODUCT PRICE", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        products.grid_columnconfigure(column, weight=1)

                if R >= 0:
                    if column == 5:

                        button = Button(products, text="Delete", bg="RED", fg="white", padx=3, pady=3)

                        button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                        button['command'] = lambda btn=button: deleteData(btn)

                        products.grid_columnconfigure(column, weight=1)
                    elif column == 4:

                        button = Button(products, text="Edit", bg="blue", fg="white", padx=3, pady=3)

                        button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                        button['command'] = lambda btn=button: editDataProduct(btn)

                        products.grid_columnconfigure(column, weight=1)

                    elif column == 0:

                        label = Label(products, text=str(Data[R][column]), bg="white", fg="black", padx=3, pady=3)

                        label.config(font=('Arial', 14))

                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                        products.grid_columnconfigure(column, weight=1)

                    elif column == 1:

                        label = Label(products, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)

                        label.config(font=('Arial', 14))

                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                        products.grid_columnconfigure(column, weight=1)

                    elif column == 2:

                        label = Label(products, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)

                        label.config(font=('Arial', 14))

                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                        products.grid_columnconfigure(column, weight=1)
                    elif column == 3:

                        label = Label(products, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)

                        label.config(font=('Arial', 14))

                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                        products.grid_columnconfigure(column, weight=1)

        productsTab.add(products, text="Products")

        productsTab.pack(fill="both")

    def editDataProduct(btn):
        row = btn.grid_info()['row']
        column = btn.grid_info()['column']
        # print("Column : " + str(column) + " Row : " + str(row))
        widget = products.grid_slaves(row=row, column=0)[0]
        widget1 = products.grid_slaves(row=row, column=1)[0]
        widget2 = products.grid_slaves(row=row, column=2)[0]
        widget3 = products.grid_slaves(row=row, column=3)[0]

        ID = int(widget.cget("text"))

        productDetails = query.FetchProduct(ID)
        if productDetails is not None:
            EditProduct(productDetails)
            widget1.config(text=productDetails.PRODUCT_NAME)
            widget2.config(text=productDetails.PRODUCT_TYPE)
            widget3.config(text=productDetails.PRODUCT_PRICE)
        # EDIT HEREEE
        #   ______________________________

    Data = query.FetchAllProducts()

    for R in range(len(Data)):
        for column in range(6):
            if R == 0:
                if column == 5:
                    label = Label(products, text="Action", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                elif column == 4:
                    label = Label(products, text="Action", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    products.grid_columnconfigure(column, weight=1)
                elif column == 0:
                    label = Label(products, text="ID", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    products.grid_columnconfigure(column, weight=1)
                elif column == 1:
                    label = Label(products, text="PRODUCT NAME", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    products.grid_columnconfigure(column, weight=1)
                elif column == 2:
                    label = Label(products, text="PRODUCT TYPE", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    products.grid_columnconfigure(column, weight=1)
                elif column == 3:
                    label = Label(products, text="PRODUCT PRICE", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    products.grid_columnconfigure(column, weight=1)

            if R >= 0:
                if column == 5:

                    button = Button(products, text="Delete", bg="RED", fg="white", padx=3, pady=3)

                    button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                    button['command'] = lambda btn=button: deleteData(btn)

                    products.grid_columnconfigure(column, weight=1)
                elif column == 4:

                    button = Button(products, text="Edit", bg="blue", fg="white", padx=3, pady=3)

                    button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                    button['command'] = lambda btn=button: editDataProduct(btn)

                    products.grid_columnconfigure(column, weight=1)

                elif column == 0:

                    label = Label(products, text=str(Data[R][column]), bg="white", fg="black", padx=3, pady=3)

                    label.config(font=('Arial', 14))

                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                    products.grid_columnconfigure(column, weight=1)

                elif column == 1:

                    label = Label(products, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)

                    label.config(font=('Arial', 14))

                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                    products.grid_columnconfigure(column, weight=1)

                elif column == 2:

                    label = Label(products, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)

                    label.config(font=('Arial', 14))

                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                    products.grid_columnconfigure(column, weight=1)
                elif column == 3:

                    label = Label(products, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)

                    label.config(font=('Arial', 14))

                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)

                    products.grid_columnconfigure(column, weight=1)

    productsTab.add(products, text="Products")

    productsTab.pack(fill="both")

    Button_Add = Button(RightContent, text="Add Component", fg="white", bg="#f0ad4e", font=(FONT, paragraphFont),
                        command=AddComponentProduct)
    Button_Add.pack(fill="x", pady=5)


# Showing OrderPlacement
# Work : Done
def OrderPlacement():
    ResetWindow()

    global LeftContent
    global RightContent

    global my_scrollbar
    global myList

    # scrollbar here
    # Select all query from database table

    # adding table into tab

    def deliverData(btn):
        row = btn.grid_info()['row']
        C = btn.grid_info()['column']
        print("Column : " + str(C) + " Row : " + str(row))
        widget = Orderss.grid_slaves(row=row, column=0)[0]
        widget2 = Orderss.grid_slaves(row=row, column=1)[0]
        widget3 = Orderss.grid_slaves(row=row, column=2)[0]

        ID = widget.cget("text")

        print(str(widget.cget("text")))
        # --------------------------
        query.InsertHistory(ID)
        # Delete Here #
        # -------------------
        for widget in Orderss.winfo_children():
            widget.destroy()

        Data = query.FetchAllOrders()

        for R in range(len(Data)):
            for C in range(6):
                if R == 0:
                    if C == 5:
                        label = Label(Orderss, text="Status", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    if C == 4:
                        label = Label(Orderss, text="Action", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 3:
                        label = Label(Orderss, text="Action", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 0:
                        label = Label(Orderss, text="ID", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 1:
                        label = Label(Orderss, text="NAME", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 2:
                        label = Label(Orderss, text="Date Of Delivery", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)

                if R >= 0:
                    if C == 5:
                        button = Button(Orderss, text="Set As Delivered", bg="#5cb85c", fg="white", padx=3, pady=3)
                        button.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        button['command'] = lambda btn=button: deliverData(btn)
                        Orderss.grid_columnconfigure(C, weight=1)
                    if C == 4:
                        button = Button(Orderss, text="Delete", bg="RED", fg="white", padx=3, pady=3)
                        button.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        button['command'] = lambda btn=button: deleteData(btn)
                        Orderss.grid_columnconfigure(C, weight=1)
                    if C == 3:
                        button = Button(Orderss, text="Edit", bg="blue", fg="white", padx=3, pady=3)
                        button.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        button['command'] = lambda btn=button: editData(btn)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 0:
                        label = Label(Orderss, text=str(Data[R][C]), bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 1:
                        label = Label(Orderss, text=Data[R][C], bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 2:
                        label = Label(Orderss, text=Data[R][C], bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)

        orderTab.add(Orderss, text="Orders")
        orderTab.pack(fill="both")

    def deleteData(btn):
        row = btn.grid_info()['row']
        C = btn.grid_info()['column']
        print("Column : " + str(C) + " Row : " + str(row))
        widget = Orderss.grid_slaves(row=row, column=0)[0]
        widget2 = Orderss.grid_slaves(row=row, column=1)[0]
        widget3 = Orderss.grid_slaves(row=row, column=2)[0]

        ID = widget.cget("text")

        print(str(widget.cget("text")))
        # --------------------------
        query.DeleteOrder(int(ID))
        # Delete Here #
        # -------------------
        for widget in Orderss.winfo_children():
            widget.destroy()

        Data = query.FetchAllOrders()

        for R in range(len(Data)):
            for C in range(6):
                if R == 0:
                    if C == 5:
                        label = Label(Orderss, text="Status", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    if C == 4:
                        label = Label(Orderss, text="Action", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 3:
                        label = Label(Orderss, text="Action", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 0:
                        label = Label(Orderss, text="ID", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 1:
                        label = Label(Orderss, text="NAME", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 2:
                        label = Label(Orderss, text="Date Of Delivery", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)

                if R >= 0:
                    if C == 5:
                        button = Button(Orderss, text="Set As Delivered", bg="#5cb85c", fg="white", padx=3, pady=3)
                        button.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        button['command'] = lambda btn=button: deliverData(btn)
                        Orderss.grid_columnconfigure(C, weight=1)
                    if C == 4:
                        button = Button(Orderss, text="Delete", bg="RED", fg="white", padx=3, pady=3)
                        button.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        button['command'] = lambda btn=button: deleteData(btn)
                        Orderss.grid_columnconfigure(C, weight=1)
                    if C == 3:
                        button = Button(Orderss, text="Edit", bg="blue", fg="white", padx=3, pady=3)
                        button.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        button['command'] = lambda btn=button: editData(btn)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 0:
                        label = Label(Orderss, text=str(Data[R][C]), bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 1:
                        label = Label(Orderss, text=Data[R][C], bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)
                    elif C == 2:
                        label = Label(Orderss, text=Data[R][C], bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=C, sticky="nsew", padx=1, pady=1)
                        Orderss.grid_columnconfigure(C, weight=1)

        orderTab.add(Orderss, text="Orders")
        orderTab.pack(fill="both")

    def editData(btn):
        row = btn.grid_info()['row']
        column = btn.grid_info()['column']
        # print("Column : " + str(column) + " Row : " + str(row))
        widget = Orderss.grid_slaves(row=row, column=0)[0]
        widget1 = Orderss.grid_slaves(row=row, column=1)[0]
        widget2 = Orderss.grid_slaves(row=row, column=2)[0]

        ID = int(widget.cget("text"))
        orderDetails = query.FetchOrder(ID)
        if orderDetails is not None:
            EditOrder(orderDetails)
            widget1.config(text=orderDetails.Name)
            widget2.config(text=orderDetails.DateOfDelivery)
        # EDIT HEREEE
        #   ______________________________

    Data = query.FetchAllOrders()

    for R in range(len(Data)):
        for column in range(7):
            if R == 0:

                if column == 6:
                    label = Label(Orderss, text="Status", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                if column == 5:
                    label = Label(Orderss, text="Action", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 4:
                    label = Label(Orderss, text="Action", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 0:
                    label = Label(Orderss, text="ID", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 1:
                    label = Label(Orderss, text="NAME", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 2:
                    label = Label(Orderss, text="Date Of Delivery", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 3:
                    label = Label(Orderss, text="Price", bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)

            if R >= 0:
                if column == 6:
                    button = Button(Orderss, text="Set As Delivered", bg="#5cb85c", fg="white", padx=3, pady=3)
                    button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    button['command'] = lambda btn=button: deliverData(btn)
                    Orderss.grid_columnconfigure(column, weight=1)
                if column == 5:
                    button = Button(Orderss, text="Delete", bg="RED", fg="white", padx=3, pady=3)
                    button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    button['command'] = lambda btn=button: deleteData(btn)
                    Orderss.grid_columnconfigure(column, weight=1)
                if column == 4:
                    button = Button(Orderss, text="Edit", bg="blue", fg="white", padx=3, pady=3)
                    button.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    button['command'] = lambda btn=button: editData(btn)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 0:
                    label = Label(Orderss, text=str(Data[R][column]), bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 1:
                    label = Label(Orderss, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 2:
                    label = Label(Orderss, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)
                elif column == 3:
                    label = Label(Orderss, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)
                    label.config(font=('Arial', 14))
                    label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                    Orderss.grid_columnconfigure(column, weight=1)

    orderTab.add(Orderss, text="Orders")

    orderTab.pack(fill="both")

    Button_Add = Button(RightContent, text="Add Component", fg="white", bg="#f0ad4e", font=(FONT, paragraphFont),
                        command=AddOrder)
    Button_Add.pack(fill="x", pady=5)


# Showing Review
# Work :
def ReviewWindow():
    ResetWindow()

    global LeftContent
    global RightContent

    global my_scrollbar
    global myList

    # scrollbar here
    # Select all query from database table

    # adding table into tab

    tablayout.add(tab1, text="Progress Report")

    tablayout.pack(fill="both")

    ReviewCanvas = Canvas(RightContent, width=300, height=300)
    ReviewCanvas.pack()
    # canvas for rightcontent

    defaultMonth = StringVar(RightContent)
    defaultYear = StringVar(RightContent)

    MonthLabel = Label(ReviewCanvas, text="Month")
    ReviewCanvas.create_window(50, 50, window=MonthLabel)
    choices = ['ALL', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    defaultMonth.set('ALL')
    Month = OptionMenu(ReviewCanvas, defaultMonth, *choices)
    ReviewCanvas.create_window(200, 50, window=Month, width=150)

    YearLabel = Label(ReviewCanvas, text="Year")
    ReviewCanvas.create_window(50, 80, window=YearLabel)
    choicesYearly = query.FetchAllYears()
    defaultYear.set(choicesYearly[0])
    Year = OptionMenu(ReviewCanvas, defaultYear, *choicesYearly)
    ReviewCanvas.create_window(200, 80, window=Year, width=150)


    def SearchReport():
        Year = defaultYear.get()
        Month = defaultMonth.get()

        Data = query.FetchReport(Year,Month)

        for R in range(len(Data)):
            for column in range(3):
                if R == 0:

                    if column == 0:
                        label = Label(tab1, text="Number of Sales", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)
                    elif column == 1:
                        label = Label(tab1, text="Total Price", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)
                    elif column == 2:
                        label = Label(tab1, text="Total Profit", bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)


                if R >= 0:

                    if column == 0:
                        label = Label(tab1, text=str(Data[R][column]), bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)
                    elif column == 1:
                        label = Label(tab1, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)
                    elif column == 2:
                        label = Label(tab1, text=Data[R][column], bg="white", fg="black", padx=3, pady=3)
                        label.config(font=('Arial', 14))
                        label.grid(row=R + 1, column=column, sticky="nsew", padx=1, pady=1)
                        tab1.grid_columnconfigure(column, weight=1)



    Button_Search = Button(RightContent, text="SEARCH", fg="white", bg="#f0ad4e", font=(FONT, paragraphFont),
                           command=SearchReport)
    ReviewCanvas.create_window(200, 120, window=Button_Search,width=150)


# Labels
# -----------------------


# Buttons on Title
# -----------------------
Business_Helper_Label = Label(Title, text="BUSINESS HELPER", font=(FONT, headingFont),
                              fg="white", anchor=N, background="black")
Business_Helper_Label.pack(fill=X)

Buttons_Layer = Frame(Title)
Buttons_Layer.pack(fill=X)

Button_Database = Button(Buttons_Layer, text="Database", fg="black", bg="#f0ad4e", font=(FONT, paragraphFont),
                         command=show_DataBase)
Button_Database.pack(side=LEFT, fill="x", expand=1)
Button_Order = Button(Buttons_Layer, text="Order", fg="black", bg="#f0ad4e", font=(FONT, paragraphFont),
                      command=OrderPlacement)
Button_Order.pack(side=LEFT, fill="x", expand=1)
Button_Review = Button(Buttons_Layer, text="Review", fg="black", bg="#f0ad4e", font=(FONT, paragraphFont),
                       command=ReviewWindow)
Button_Review.pack(side=LEFT, fill="x", expand=1)

# PACK
# ----------------------

Title.pack(fill=X)
Content.pack(fill="both", expand="yes", padx=10)
LeftContent.pack(fill="both", expand="yes", padx=10, pady=10, side=LEFT)
RightContent.pack(fill="both", expand="yes", padx=10, pady=10, side=RIGHT)
myList.pack(fill="both", expand=1, pady=15)

w, h = master.winfo_screenwidth(), master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (w, h))
master.title("Computer Management System")

# # root main loop
# # ------------------------


tkr.mainloop()
