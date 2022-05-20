from tkinter import *
import sqlite3


root = Tk()
# Creating a tk object to create the main window with adjusting features
root.title('Car Rental Database')
root.geometry("400x400")


# Connecting to sqlite3

connection = sqlite3.connect('cr.db')



def closeWindow():
    pass

def custInfo():


    # Creating text fields with labels for the user to enter
    # information as a new customer
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    name = Entry(newWindow, width = 30)
    name.grid(row = 0, column = 1, padx = 20,pady=10)

    phone = Entry(newWindow, width = 30)
    phone.grid(row = 1, column = 1,pady=10)

    # Creating the labels corresponding to each entry

    lname = Label(newWindow, text = 'Name')
    lname.grid(row =0, column = 0,pady=10)

    lphone = Label(newWindow, text = 'Phone')
    lphone.grid(row =1, column = 0,pady=10)

    submit_btn = Button(newWindow, text ='Add Customer ', command = lambda: addCustomerDB(name, phone))
    submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

def addCustomerDB(name, phone):
    
    # Connecting again to make the access cocurrent active
    submit_conn = sqlite3.connect('cr.db')
    
    # Creating a cursor to execute queries and commit changes
    submit_cur = submit_conn.cursor()
    
    submit_cur.execute("INSERT INTO CUSTOMER VALUES (:CustID ,:Name, :Phone)",
		{
            'CustID': None,
			'Name': name.get(),
			'Phone': phone.get()
		})
    
	#commit changes
    submit_conn.commit()

	#close the DB connection
    submit_conn.close()


def VecInfo():
    # Creating text fields with labels for the user to enter
    # information as a new vehicle
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    vin = Entry(newWindow, width = 30)
    vin.grid(row = 0, column = 1, padx = 20,pady=10)

    description = Entry(newWindow, width = 30)
    description.grid(row = 1, column = 1,pady=10)

    year = Entry(newWindow, width = 30)
    year.grid(row = 2, column = 1,pady=10)

    type = Entry(newWindow, width = 30)
    type.grid(row = 3, column = 1,pady=10)

    category = Entry(newWindow, width = 30)
    category.grid(row = 4, column = 1,pady=10)

    # Creating the labels corresponding to each entry

    lvin = Label(newWindow, text = 'VIN')
    lvin.grid(row =0, column = 0,pady=10)

    ldescription = Label(newWindow, text = 'Description')
    ldescription.grid(row =1, column = 0,pady=10)

    lyear = Label(newWindow, text = 'Year')
    lyear.grid(row =2, column = 0,pady=10)

    ltype = Label(newWindow, text = 'Type')
    ltype.grid(row =3, column = 0,pady=10)

    lcategory = Label(newWindow, text = 'Category')
    lcategory.grid(row =4, column = 0,pady=10)

    submit_btn = Button(newWindow, text ='Add Vehicle ', command = lambda: addVehicleDB(vin,description,year,type,category))
    submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

def addVehicleDB(vin,description,year,type,category):
	submit_conn = sqlite3.connect('cr.db')

	submit_cur = submit_conn.cursor()

	submit_cur.execute("INSERT INTO VEHICLE VALUES (:VehicleID, :Description, :year, :type, :category) ",
		{
			'VehicleID': vin.get(),
			'Description': description.get(),
			'year': year.get(),
			'type': type.get(),
			'category': category.get()
		})

	#commit changes

	submit_conn.commit()
	#close the DB connection
	submit_conn.close()


def RentInfo():
    # Creating text fields with labels for the user to enter
    # information as a new vehicle
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    vin = Entry(newWindow, width = 30)
    vin.grid(row = 0, column = 1, padx = 20,pady=10)

    description = Entry(newWindow, width = 30)
    description.grid(row = 1, column = 1,pady=10)

    year = Entry(newWindow, width = 30)
    year.grid(row = 2, column = 1,pady=10)

    type = Entry(newWindow, width = 30)
    type.grid(row = 3, column = 1,pady=10)

    category = Entry(newWindow, width = 30)
    category.grid(row = 4, column = 1,pady=10)

    # Creating the labels corresponding to each entry

    lvin = Label(newWindow, text = 'VIN')
    lvin.grid(row =0, column = 0,pady=10)

    ldescription = Label(newWindow, text = 'Description')
    ldescription.grid(row =1, column = 0,pady=10)

    lyear = Label(newWindow, text = 'Year')
    lyear.grid(row =2, column = 0,pady=10)

    ltype = Label(newWindow, text = 'Type')
    ltype.grid(row =3, column = 0,pady=10)

    lcategory = Label(newWindow, text = 'Category')
    lcategory.grid(row =4, column = 0,pady=10)

    submit_btn = Button(newWindow, text ='Add Vehicle ', command = lambda: addVehicleDB(vin,description,year,type,category))
    submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

def retRental():
    pass

def lookCust():
    pass

def lookVec():
    pass

def MainMenu():


    # Creating Widgets for the Main Menu
    welcome = Label(root,text= 'Welcome to Our Car Rental Database')
    welcome.grid(row= 1, column= 1, padx= 85,pady=5)

    opt = Label(root,text= 'Select an option from the list')
    opt.grid(row= 2, column= 1, padx= 85,pady=5)

    addCust = Button(root,text= 'Add Customer', command= custInfo)
    addCust.grid(row= 3, column= 1,pady=10)

    addVehicle = Button(root,text= 'Add Vehicle', command= VecInfo)
    addVehicle.grid(row= 4, column= 1,pady=10)

    addRental = Button(root,text= 'Add test Rental', command= RentInfo)
    addRental.grid(row= 5, column= 1,pady=10)

    returnRental = Button(root,text= 'Add Rental', command= retRental)
    returnRental.grid(row= 6, column= 1,pady=10)

    lookByCust = Button(root,text= 'Look Up By Customer', command= lookCust)
    lookByCust.grid(row= 7, column= 1,pady=10)

    lookByVehicle = Button(root,text= 'Look Up By Vehicle', command= lookVec)
    lookByVehicle.grid(row= 8, column= 1,pady=10)



    root.mainloop()



MainMenu()