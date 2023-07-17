import tkinter as tk
from pathlib import Path



mainWindow = tk.Tk()
mainWindow.title("Pizza Place")
mainWindow.config(bg="skyblue")
mainWindow.minsize(900, 600)
mainWindow.maxsize(900, 600)
orderFile = open("orderNum.txt", "r")
orderNumber = int(orderFile.read())
orderFile.close()
orderPath = Path("/orders/")

from pizzaWindow import *

def clearWindow(windowName):
   for widgets in windowName.winfo_children():
      widgets.destroy()

def newOrder():
    clearWindow(mainLeftFrame)
    global orderNumber
    orderNumber = orderNumber + 1
    orderFile = open("orderNum.txt", "w")
    orderFile.write(str(orderNumber))
    orderFile.close()
    global orderFileName
    orderFileName = "orders/"+str(orderNumber)+".txt"
    openOrderFile = open(orderFileName, "w")
    openOrderFile.close()
    print(orderFileName)
    orderWindow()

def viewOrder():
    clearWindow(mainRightFrame)
    newOrderFile = open(orderFileName, "r")
    showOrder = tk.Text(mainRightFrame)
    showOrder.insert("1.0", newOrderFile.read())
    showOrder.config(state = "disabled")
    showOrder.grid()

    

def orderWindow():
    pizzaButton = tk.Button(mainLeftFrame, text = "PIZZA", padx = 10, pady = 10, command = pizzaWindow)
    pizzaButton.grid(padx = 5, pady = 10)

    sidesButton = tk.Button(mainLeftFrame, text = "SIDES", padx = 10, pady = 10)
    sidesButton.grid(padx = 5, pady = 10)

    dessertsButton = tk.Button(mainLeftFrame, text = "DESSERTS", padx = 10, pady = 10)
    dessertsButton.grid(padx = 5, pady = 10)

    viewOrderButton = tk.Button(mainLeftFrame, text = "VIEW/EDIT ORDER", padx = 10, pady = 10, command = viewOrder)
    viewOrderButton.grid(padx = 5, pady = 10)

    orderNumberLabel = tk.Label(text = "Order # " + str(orderNumber))
    orderNumberLabel.grid()


mainLeftFrame = tk.Frame(mainWindow)
mainLeftFrame.grid(row = 0, column = 0, padx = 10, pady = 5)

mainRightFrame = tk.Frame(mainWindow)
mainRightFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "E" )

newOrderButton = tk.Button(mainLeftFrame, text = "NEW ORDER", padx = 10, pady = 10, command = newOrder)
newOrderButton.grid(padx = 5, pady = 10)
