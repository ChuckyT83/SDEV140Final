import tkinter as tk
from tkinter import ttk


mainWindow = tk.Tk() # creates main window
style = ttk.Style(mainWindow) # sets the style for the program
style.theme_use("default")
style.configure("TFrame", background = "green")
style.configure("TButton", background="white")
style.map("TButton", background = [("active", "red")])
style.configure("TLabel", background = "green")
style.configure("TFrame", background = "green")
style.configure("TRadiobutton", background = "green")
style.map("TRadiobutton", indicatorcolor=[("pressed", "red"), ("selected", "red")])
mainWindow.title("Pizza Place") # main window title
mainWindow.config(bg="green")
mainWindow.resizable(height = 0, width = 0) # makes the main window unresizable
orderFile = open("orderNum.txt", "r") # opens the file the stores the current order number
orderNumber = int(orderFile.read()) # sets the order number variable from file
orderFile.close() # closes order number file
logo = tk.PhotoImage(file = "logo.png", height = 450, width = 450, name = "Logo") # creates the logo from the image file
thanksImage = tk.PhotoImage(file = "thanks.png", name = "Thank You")
orderSelection = tk.StringVar() # creates a tkinter string variable for editing the order
name = tk.StringVar() # creates a tkinter string variable for the orderer's name
addressOne = tk.StringVar() # creates a tkinter string variable for the orderer's first address line
addressTwo = tk.StringVar() # creates a tkinter string variable for the orderer's second address line
city = tk.StringVar() # creates a tkinter string variable for the orderer's city
zipCode = tk.StringVar() # creates a tkinter string variable for the orderer's zip code
tax = 1.07 # creates a tax variable

from orders import * # imports the orders.py file which has functionality and variables for adding items to an order

def clearWindow(windowName): # creates the function that clears a window by destroying its widgets
    for widgets in windowName.winfo_children():
      widgets.destroy()

def newOrder(): # creates the function for the new order button
    clearWindow(mainLeftFrame) # clears the window
    global orderNumber # sets orderNumber variable global so other functions can access it
    orderNumber = orderNumber + 1 # increments the order number
    orderFile = open("orderNum.txt", "w") # opens the order number file
    orderFile.write(str(orderNumber)) # writes new order number to order number file
    orderFile.close() # closes order number file
    global orderFileName # sets the orderFileName variable global so other functions can access it
    orderFileName = "orders/"+str(orderNumber)+".txt" # sets the orderFileName variable to the orders folder + ordernumber.txt
    openOrderFile = open(orderFileName, "w") # opens and creates the file where the order will be stored
    openOrderFile.close() # closes order file
    orderWindow() # creates order window
    logoCanvas = tk.Canvas(mainRightFrame, height = 450, width = 450, bg = "green", highlightthickness=0) # creates the logo canvas
    logoCanvas.create_image(225,225,image = logo) # loads the image file 
    logoCanvas.grid()
        
def orderWindow():
    pizzaButton = ttk.Button(mainLeftFrame, text = "PIZZA",  command = pizzaWindow) # creates pizza button
    pizzaButton.grid(padx = 5, pady = 10)

    sidesButton = ttk.Button(mainLeftFrame, text = "SIDES", command = sidesWindow) # creates sides button
    sidesButton.grid(padx = 5, pady = 10)

    viewOrderButton = ttk.Button(mainLeftFrame, text = "VIEW/EDIT ORDER", command = viewOrder) # creates view/edit order button
    viewOrderButton.grid(padx = 5, pady = 10)

    completeOrderButton = ttk.Button(mainLeftFrame, text = "COMPLETE ORDER", command = completeOrder) # creates the complete order button
    completeOrderButton.grid(padx = 5, pady = 10)

    cancelOrderButton = ttk.Button(mainLeftFrame, text = "CANCEL ORDER", command = cancelOrder) # creates the canvel order button
    cancelOrderButton.grid(padx = 5, pady = 10)

    orderNumberLabel = ttk.Label(text = "Order # " + str(orderNumber)) # create the label that shows order number below buttons
    orderNumberLabel.grid()

def viewOrder(): # creates the view order frame
    if order == {}: # throw error if order is empty
        messagebox.showerror("Empty Order","Your order is empty.") # creates error popup
        clearWindow(mainRightFrame) # clears right frame
        logoCanvas = tk.Canvas(mainRightFrame, height = 450, width = 450, bg = "green", highlightthickness=0) # reloads image
        logoCanvas.create_image(225,225,image = logo)
        logoCanvas.grid()
    else: # shows an editable order list if the order is not empty
        clearWindow(mainRightFrame) # clears right frame
        global orderRadioFrame # sets variable global so other functions can access it
        orderRadioFrame = tk.Frame(mainRightFrame, background = "green") # creates radio buttons frame
        orderRadioFrame.grid(column = 1, row = 0, padx = 160, pady = 200) 
        orderLabel = ttk.Label(orderRadioFrame, text = "ITEM / SIZE")
        orderLabel.grid()
        orderSelection.set("0") # sets the order selection to the first item in the list
        subTotal = 0 # creates subtotal variable
        global orderRadio # sets variable global so other functions can access it
        for items in order: # loop that gathers order information from the order dictionary
            orderRadio = ttk.Radiobutton(orderRadioFrame, text = order[items]["type"] + " / " + order[items]["size"] + " / " + str(order[items]["cost"]), variable = orderSelection,
                                        value = items) # creates tkinter radio buttons from the order dictionary
            orderRadio.grid(sticky = "W")
            subTotal = order[items]["cost"] + subTotal # adds item cost to subtotal
        removeButton = ttk.Button(orderRadioFrame, text = "Remove From Order", command = removeFromOrder) 
        removeButton.grid()
        totalLabel = ttk.Label(orderRadioFrame, text = f"\nSubtotal:\t${subTotal:.2f}\nTotal:\t${subTotal * tax:.2f}")
        totalLabel.grid()       

def removeFromOrder(): # function for remove from order button
    if order == {}: # creates error if order is empty
        messagebox.showerror("Empty Order","Your order is empty.")
    else:
        removePopup() # loads order removal confirmation

def removePopup(): # function for order removal confirmation
    global removePopupWindow 
    removePopupWindow = tk.Toplevel() # creates new window
    removePopupWindow.title("Remove Item") # sets title for new window
    removeFrame = ttk.Frame(removePopupWindow)
    removeFrame.grid()
    removeLabel = ttk.Label(removeFrame, text = "Are you sure you would like to remove " + str(order[int(orderSelection.get())]["type"]) + "?")
    removeLabel.grid(row = 0, padx = 5, pady = 10)
    buttonFrame = ttk.Frame(removeFrame)
    buttonFrame.grid(row = 1)
    noRemoveButton = ttk.Button(buttonFrame, text = "No", command = lambda: removePopupWindow.destroy()) # closes window without removing selected item
    noRemoveButton.grid(row = 0, column = 0, padx = 5, pady = 10)
    yesRemoveButton = ttk.Button(buttonFrame, text = "Yes", command = removeItem) # removes selected order radio button item
    yesRemoveButton.grid(row = 0, column = 1, padx = 5, pady = 10)

def removeItem(): # function to remove selected item
    order.pop(int(orderSelection.get())) # removes selected order radio button item
    clearWindow(orderRadioFrame) # clears edit order frame
    viewOrder() # repopulates edit order frame
    removePopupWindow.destroy() # closes edit order popup

def completeOrder(): # function to complete order
    if order == {}: # creates error popup if order is empty
        messagebox.showerror("Empty Order","Your order is empty.")
    else:
        complete() # creates complete order window if order is not empty

def complete(): # function to create complete order window
    completeWindow = tk.Toplevel() # creates a new window for order completion
    completeWindow.grab_set() # locks input to only the complete window
    completeWindow.title("Complete Order")
    completeWindow.config(bg = "green")
    completeWindow.resizable(height = 0, width = 0)
    formLabel = ttk.Label(completeWindow, text = "Please complete the information below.\nOrders are cash only. Please tip your delivery driver.\n* fields are required.")
    formLabel.grid(padx = 5, pady = 10, column = 0, row = 0, columnspan = 2)
    orderLeftFrame = ttk.Frame(completeWindow)
    orderLeftFrame.grid(column = 0, row = 1, padx = 5, pady = 10)
    nameLabel = ttk.Label(orderLeftFrame, text = "Name *")
    nameLabel.grid(row = 0, column = 0, sticky = "E")
    global nameEntry
    nameEntry = ttk.Entry(orderLeftFrame, textvariable = name) # creates entry box for orderer's name
    nameEntry.grid(row = 0, column = 1)
    addressOneLabel = ttk.Label(orderLeftFrame, text = "Address 1 *")
    addressOneLabel.grid(row = 1, column = 0, sticky = "E")
    global addressOneEntry
    addressOneEntry = ttk.Entry(orderLeftFrame, textvariable = addressOne) # creates entry for orderer's first address line
    addressOneEntry.grid(row = 1, column = 1)
    addressTwoLabel = ttk.Label(orderLeftFrame, text = "Address 2")
    addressTwoLabel.grid(row = 2, column = 0, sticky = "E")
    global addressTwoEntry
    addressTwoEntry = ttk.Entry(orderLeftFrame, textvariable = addressTwo) # creates entry for orderer's second address line
    addressTwoEntry.grid(row = 2, column = 1)
    cityLabel = ttk.Label(orderLeftFrame, text = "City *")
    cityLabel.grid(row = 3, column = 0, sticky = "E")
    global cityEntry
    cityEntry = ttk.Entry(orderLeftFrame, textvariable = city) # creates entry for orderer's city
    cityEntry.grid(row = 3, column = 1)
    zipLabel = ttk.Label(orderLeftFrame, text = "Zip Code *")
    zipLabel.grid(row = 4, column = 0, sticky = "E")
    global zipEntry
    zipEntry = ttk.Entry(orderLeftFrame, textvariable = zipCode) # creates entry for orderer's zip code
    zipEntry.grid(row = 4, column = 1)
    orderRightFrame = ttk.Frame(completeWindow)
    orderRightFrame.grid(column = 1, row = 1, padx = 5, pady = 10)
    subTotal = 0
    for items in order: # loop that prints the current order and calculates subtotal
        orderLabel = ttk.Label(orderRightFrame, text = order[items]["type"] + " / " + order[items]["size"] + " / " + str(order[items]["cost"]))
        orderLabel.grid(sticky = "W")
        subTotal = order[items]["cost"] + subTotal
    subTotalLabel = ttk.Label(orderRightFrame, text = f"\nSub-Total: ${subTotal:.2f}\nTotal:\t   ${subTotal * tax:.2f}")
    subTotalLabel.grid()
    submitOrderButton = ttk.Button(completeWindow, text = "SUBMIT ORDER", command = submitOrder)
    submitOrderButton.grid(padx = 5, pady = 10, columnspan = 2)

def submitOrder(): # function for submit order button
    if testEntry() == True: # calls testEntry function to ensure that order information is within required parameters
        subTotal = 0
        orderFileName = "orders/"+str(orderNumber)+".txt" # sets file name variable to orders/orderNumber.txt
        openOrderFile = open(orderFileName, "w") # opens order file for writing
        # writes order information to orderNumber.txt in the orders folder
        openOrderFile.write(f"Order #{orderNumber}\n\nName: {nameEntry.get()}\nAddress 1: {addressOneEntry.get()}\nAddress 2: {addressTwoEntry.get()}\n"
                            f"City: {cityEntry.get()}\nZip Code: {zipEntry.get()}\n\n ---Order---\n\n")
        for items in order: # loop writes order information to the order file
            subTotal = subTotal + order[items]['cost']
            openOrderFile.write(f"Item: {order[items]['type']} \n    Size: {order[items]['size']} \n    "
                                f"Ingredients: {order[items]['ingredients']} \n    Price: {str(order[items]['cost'])}\n\n")
        openOrderFile.write(f"\nSubtotal: ${subTotal:.2f}\nTotal:\t  ${subTotal * tax:.2f}")
        openOrderFile.close()
        thanksPopup() # calls the thank you popup

def testEntry(): # function to test the orderer's entry information
    if zipEntry.get().isdigit() == False or len(zipEntry.get()) != 5: # creates error popup if the zip entry is not five digits
        messagebox.showerror("Invalid zip","Please enter a valid five digit numeric zip code.")
    elif nameEntry.get() == "" or addressOneEntry.get() == "" or cityEntry.get() == "" or zipEntry.get() == "": # creates error popup if required fields are left blank
        messagebox.showerror("Empty Entry","Please fill all required fields.")
    else:
        return True # returns True if input is valid

def thanksPopup(): # creates thank you popup
    thanksWindow = tk.Toplevel(bg = "green")
    thanksWindow.grab_set()
    thanksWindow.title("Thank you for your order!")
    thanksCanvas = tk.Canvas(thanksWindow, width = 195, height = 132, bg = "green", highlightthickness=0) # creates the thanks image canvas
    thanksCanvas.create_image(97, 66, image = thanksImage) # loads the image file 
    thanksCanvas.grid(pady = 10)
    thanksFrame = ttk.Frame(thanksWindow)
    thanksFrame.grid()
    thanksLabel = ttk.Label(thanksFrame, text = "Your order will hit our ovens ASAP! Thanks!")
    thanksLabel.grid(row = 0, padx = 5, pady = 10)
    buttonFrame = ttk.Frame(thanksFrame)
    buttonFrame.grid(row = 1)
    orderFileName = "orders/"+str(orderNumber)+".txt"
    openOrderFile = open(orderFileName, "r")
    orderText = str(openOrderFile.read())
    openOrderFile.close()
    orderLabel = ttk.Label(thanksFrame ,text = orderText)
    orderLabel.grid()
    closeButton = ttk.Button(buttonFrame, text = "Close", command = lambda: mainWindow.destroy()) # closes program
    closeButton.grid(row = 0, column = 0, padx = 5, pady = 10)

def cancelOrder(): # creates cancel order popup
    cancelWindow = tk.Toplevel()
    cancelWindow.grab_set()
    cancelWindow.title("Cancel Order")
    cancelFrame = ttk.Frame(cancelWindow)
    cancelFrame.grid()
    cancelLabel = ttk.Label(cancelFrame, text = "Are you sure you would like to cancel your order? This will close the program.")
    cancelLabel.grid(row = 0, padx = 5, pady = 10)
    buttonFrame = ttk.Frame(cancelFrame)
    buttonFrame.grid(row = 1)
    noButton = ttk.Button(buttonFrame, text = "No", command = lambda: cancelWindow.destroy()) # closes cancel popup
    noButton.grid(row = 0, column = 0, padx = 5, pady = 10)
    yesButton = ttk.Button(buttonFrame, text = "Yes", command = lambda: mainWindow.destroy()) # closes ordering program
    yesButton.grid(row = 0, column = 1, padx = 5, pady = 10)


    

    

mainLeftFrame = ttk.Frame(mainWindow) # creates the left frame for buttons
mainLeftFrame.grid(row = 0, column = 0, padx = 10, pady = 5)

mainRightFrame = ttk.Frame(mainWindow) # creates right frame for logo and order viewing/editing
mainRightFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "E" )

newOrderButton = ttk.Button(mainLeftFrame, text = "NEW ORDER", command = newOrder) # creates the new order button on program start up
newOrderButton.grid(padx = 245 , pady = 245)