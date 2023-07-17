import tkinter as tk
import mainWindow as main

pizzaIngredients = [None]
pizzaSize = [None]
pizzaSauce = [None]
pizzaType = [None]
sizeSelection = tk.StringVar()
sauceSelection = tk.StringVar()
ingredientList = ["Pepperoni", "Sausage", "Chicken", "Bacon", "Onions", "Bell Peppers", "Mushrooms", "Black Olives",
                   "Green Olives", "Anchovies", "Fresh Basil", "Fresh Mozzerella", "Extra Cheese"]
ingSelectVar = tk.StringVar(value = ingredientList)

def clearWindow(windowName):
   for widgets in windowName.winfo_children():
      widgets.destroy()

def pizzaWindow():
    global pizzaWindow
    pizzaWindow = tk.Toplevel()
    pizzaWindowMain()

def pizzaWindowMain():
    pizzaWindow.title("Pizza")
    pizzaWindow.config(bg = "skyblue")
    pizzaWindow.minsize(900, 600)
    pizzaWindow.maxsize(900, 600)
    pizzaWindow.grab_set()
    buttonPWFrame = tk.Frame(pizzaWindow, width = 200, height = 500)
    buttonPWFrame.grid(row = 0, column = 0, padx = 10, pady = 5)
    supremeButton = tk.Button(buttonPWFrame, text = "Supreme", padx = 10, pady = 10, command = supreme)
    supremeButton.grid(row = 0, column = 0, padx = 5, pady = 10)
    bbqChickenButton = tk.Button(buttonPWFrame, text = "BBQ Chicken", padx = 10, pady = 10, command = bbqChicken)
    bbqChickenButton.grid(row = 0, column = 1, padx = 5, pady = 10)
    margaritaButton = tk.Button(buttonPWFrame, text = "Margarita", padx = 10, pady = 10, command = margarita)
    margaritaButton.grid(row = 0, column = 2, padx = 5, pady = 10)
    veggieButton = tk.Button(buttonPWFrame, text = "Veggie Explosion", padx = 10, pady = 10, command = veggieExplostion)
    veggieButton.grid(row = 1, column = 0, padx = 5, pady = 10)
    chickenAlfButton = tk.Button(buttonPWFrame, text = "Chicken Alfredo", padx = 10, pady = 10, command = chickenAlfredo)
    chickenAlfButton.grid(row = 1, column = 1, padx = 5, pady = 10)
    customButton = tk.Button(buttonPWFrame, text = "Custom", padx = 10, pady = 10, command = customPizza)
    customButton.grid(row = 1, column = 2, padx = 5, pady = 10)
    

def supreme():
    clearWindow(pizzaWindow)
    pizzaType[0] = "Supreme"
    pizzaWindow.title(pizzaType[0])
    pizzaIngredients[0]= ["Pepperoni", "Sausage", "Onions", "Black Olives", "Bell Peppers", "Mushrooms", "Cheese"]
    pizzaSauce[0] = "Marinara"
    showIngredients()
    radioSize()
    backToPizzaButton()
    addToOrderButton()

def bbqChicken():
    clearWindow(pizzaWindow)
    pizzaType[0] = "BBQ Chicken"
    pizzaWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Chicken", "Bacon", "Onion", "Cheese"]
    pizzaSauce[0] = "BBQ"
    showIngredients()
    radioSize()
    backToPizzaButton()
    addToOrderButton()

def margarita():
    clearWindow(pizzaWindow)
    pizzaType[0] = "Margarita"
    pizzaWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Fresh Mozzerella", "Fresh Basil"]
    pizzaSauce[0] = "Marinara"
    showIngredients()
    radioSize()
    backToPizzaButton()
    addToOrderButton()

def veggieExplostion():
    clearWindow(pizzaWindow)
    pizzaType[0] = "Veggie Explosion"
    pizzaWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Bell Peppers", "Onion", "Mushrooms", "Black Olives", "Green Olives", "Cheese"]
    pizzaSauce[0] = "Marinara"
    showIngredients()
    radioSize()
    backToPizzaButton()
    addToOrderButton()

def chickenAlfredo():
    clearWindow(pizzaWindow)
    pizzaType[0] = "Chicken Alfredo"
    pizzaWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Chicken", "Cheese"]
    pizzaSauce[0] = "Alfredo"
    showIngredients()
    radioSize()
    backToPizzaButton()
    addToOrderButton()

def customPizza():
    clearWindow(pizzaWindow)
    pizzaType[0] = "Custom Pizza"
    pizzaWindow.title(pizzaType[0])
    pizzaIngredients[0] = []
    showIngredients()
    customPizzaIngredients()
    radioSize()
    radioSauce()
    backToPizzaButton()
    addToOrderButton()

def radioSize():
    sizeSelection.set("Small")
    pizzaSize[0] = sizeSelection.get()
    radioSizeFrame = tk.Frame(pizzaWindow)
    radioSizeFrame.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "NW")
    sizeLabel = tk.Label(radioSizeFrame, text = "Size: ")
    sizeLabel.grid()
    sizeSmallRadio = tk.Radiobutton(radioSizeFrame, padx = 10, pady = 10, text = "Small", var = sizeSelection, value = "Small", command = setSize)
    sizeSmallRadio.grid()
    sizeMedRadio = tk.Radiobutton(radioSizeFrame, padx = 10, pady = 10, text = "Medium", var = sizeSelection, value = "Med", command = setSize)
    sizeMedRadio.grid()
    sizeLargeRadio = tk.Radiobutton(radioSizeFrame, padx = 10, pady = 10, text = "Large", var = sizeSelection, value = "Large", command = setSize)
    sizeLargeRadio.grid()

def radioSauce():
    sauceSelection.set("Marinara")
    pizzaSauce[0] = sauceSelection.get()
    radioSauceFrame = tk.Frame(pizzaWindow)
    radioSauceFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "NW")
    sauceLabel = tk.Label(radioSauceFrame, text = "Sauce: ")
    sauceLabel.grid()
    sauceMarRadio = tk.Radiobutton(radioSauceFrame, padx = 10, pady = 10, text = "Marinara", var = sauceSelection, value = "Marinara", command = setSauce)
    sauceMarRadio.grid()
    sauceBBQRadio = tk.Radiobutton(radioSauceFrame, padx = 10, pady = 10, text = "BBQ", var = sauceSelection, value = "BBQ", command = setSauce)
    sauceBBQRadio.grid()
    sauceAlfRadio = tk.Radiobutton(radioSauceFrame, padx = 10, pady = 10, text = "Alfredo", var = sauceSelection, value = "Alfredo", command = setSauce)
    sauceAlfRadio.grid()
    sauceNoneRadio = tk.Radiobutton(radioSauceFrame, padx = 10, pady = 10, text = "None", var = sauceSelection, value = "None", command = setSauce)
    sauceNoneRadio.grid()

def setSize():
    pizzaSize[0] = sizeSelection.get()

def setSauce():
    pizzaSauce[0] = sauceSelection.get()

def backToPizzaButton():
    backToPizzaButton = tk.Button(pizzaWindow, padx = 10, pady = 10, text = "Back", command = backToPizza)
    backToPizzaButton.grid(padx = 5, pady = 10)

def backToPizza():
    for items in pizzaWindow.winfo_children():
      items.destroy()    
    pizzaWindowMain()

def addToOrderButton():
    addToOrderButton = tk.Button(pizzaWindow, padx = 10, pady = 10, text = "Add To Order", command = addToOrder)
    addToOrderButton.grid(padx = 5, pady = 10)

def addToOrder():
    print("Type =", pizzaType[0], "| Size =", pizzaSize[0], "| Sauce =", pizzaSauce[0], "| Ingredients =", ", ".join(pizzaIngredients[0]), "\n")
    newOrderFile = open(main.orderFileName, "a+")
    newOrderFile.write("Pizza = " + pizzaType[0] + "\n\tSize = " + pizzaSize[0] + "\n\tSauce = " + pizzaSauce[0] + 
                         "\n\tIngredients = " + " , ".join(pizzaIngredients[0]) + "\n\n")
    newOrderFile.close()

def showIngredients():
    global ingredientsFrame
    ingredientsFrame = tk.Frame(pizzaWindow)
    ingredientsFrame.grid(row = 1, column = 0, columnspan = 150, padx = 5, pady = 10, sticky = "W")
    ingredientsLabel = tk.Label(ingredientsFrame, text = "Ingredients: ")
    ingredientsLabel.grid()
    ingredientsListLabel = tk.Label(ingredientsFrame, text = ", ".join(pizzaIngredients[0]))
    ingredientsListLabel.grid()

def customPizzaIngredients():
    customIngFrame = tk.Frame(pizzaWindow)
    customIngFrame.grid(row = 0, column = 3)
    global ingListbox
    ingredientsLabel = tk.Label(customIngFrame, text = "Ingredients: ")
    ingredientsLabel.grid()
    ingListbox = tk.Listbox(customIngFrame, height = 13, selectmode = "multiple", listvariable = ingSelectVar)
    ingListbox.grid()
    applyCustomButton = tk.Button(customIngFrame, padx = 10, pady = 10, text = "Apply Ingredients", command = setCustomIng)
    applyCustomButton.grid()

def setCustomIng():
    pizzaIngredients[0] = [ingredientList[item] for item in ingListbox.curselection()]
    ingredientsFrame.destroy()
    showIngredients()
