import tkinter as tk # imports tkinter
from tkinter import ttk # imports tkinter theme options
from tkinter import messagebox # imports tkinter error message box
import main as main # imports functions from main.py as main.functionName

pizzaIngredients = [None] # creates variable for adding pizza ingredients to a pizza
pizzaSize = [None] # creates variable for setting the pizza size
pizzaSauce = [None] # creates variable for setting the pizza sauce
pizzaType = [None] # crates variable for setting the pizza type
cost = [None] # creates variable for setting the item cost
itemCount = 0 # crates the item count variable used to identify items in the order dictionary
itemCost = [None] # creates variable for setting item cost
order = {} # creates dictionary that will be populated with items added to order
sizeSelection = tk.StringVar() # creates tkinter string variable for size selection radio buttons
sauceSelection = tk.StringVar() # creates tkinter string variable for sauce selection radio buttons
ingredientList = ["Pepperoni", "Sausage", "Chicken", "Bacon", "Onions", "Bell Peppers", "Mushrooms", "Black Olives",
                   "Green Olives", "Anchovies", "Fresh Basil", "Fresh Mozzerella", "Extra Cheese"] # ingredients list
ingSelectVar = tk.StringVar(value = ingredientList) # creates tkinter string variable for custom pizza ingredient selection radio buttons
# creates side item dictionary for sides selection radio buttons
sidesList = {0: {"item": "Bone-in Wings", "cost": 9.99}, 1: {"item": "Bonesless Wings", "cost": 9.99}, 2: {"item": "Breadsticks", "cost": 5.99},
              3: {"item": "Cheesey Bread", "cost": 6.99}, 4: {"item": "Garlic Knots", "cost": 5.99}, 5: {"item": "Chef's Salad", "cost": 7.99}}
sideSelection = tk.StringVar() # creates tkinter string variable for side selection radio buttons


def pizzaWindow(): # creates new window for pizza ordering
    global ordersWindow
    ordersWindow = tk.Toplevel()
    ordersPizzaMain() # populates pizza window

def ordersPizzaMain(): # function that populates pizza window the buttons to select pizzas
    ordersWindow.title("Pizza")
    ordersWindow.config(bg = "green")
    ordersWindow.resizable(height = 0, width = 0)
    ordersWindow.grab_set() # locks input to only order window
    buttonPWFrame = ttk.Frame(ordersWindow, width = 200, height = 500)
    buttonPWFrame.grid(row = 0, column = 0, padx = 10, pady = 5)
    supremeButton = ttk.Button(buttonPWFrame, text = "Supreme", command = supreme)
    supremeButton.grid(row = 0, column = 0, padx = 5, pady = 10)
    bbqChickenButton = ttk.Button(buttonPWFrame, text = "BBQ Chicken", command = bbqChicken)
    bbqChickenButton.grid(row = 0, column = 1, padx = 5, pady = 10)
    margaritaButton = ttk.Button(buttonPWFrame, text = "Margherita", command = margherita)
    margaritaButton.grid(row = 0, column = 2, padx = 5, pady = 10)
    veggieButton = ttk.Button(buttonPWFrame, text = "Veggie Explosion", command = veggieExplostion)
    veggieButton.grid(row = 1, column = 0, padx = 5, pady = 10)
    chickenAlfButton = ttk.Button(buttonPWFrame, text = "Chicken Alfredo", command = chickenAlfredo)
    chickenAlfButton.grid(row = 1, column = 1, padx = 5, pady = 10)
    customButton = ttk.Button(buttonPWFrame, text = "Custom", command = customPizza)
    customButton.grid(row = 1, column = 2, padx = 5, pady = 10)


def supreme(): # function for adding supreme pizza to order
    main.clearWindow(ordersWindow) # clears the orders window so it can be repopulated with pizza item information
    pizzaType[0] = "Supreme Pizza" # sets pizza type
    ordersWindow.title(pizzaType[0]) # sets window title 
    pizzaIngredients[0]= ["Pepperoni", "Sausage", "Onions", "Black Olives", "Bell Peppers", "Mushrooms", "Cheese"] # populates ingredient list
    pizzaSauce[0] = "Marinara" # sets sauce
    radioSize() # calls size selection radio buttons
    showIngredients() # calls the ingredient list display
    backToPizzaButton() # calls the button to return to the main pizza order window
    addToOrderButton() # calls the button to add the current pizza selection to the order

def bbqChicken(): # function for adding BBQ chicken pizza to order. See supreme() for more information.
    main.clearWindow(ordersWindow)
    pizzaType[0] = "BBQ Chicken Pizza"
    ordersWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Chicken", "Bacon", "Onion", "Cheese"]
    pizzaSauce[0] = "BBQ"
    radioSize()
    showIngredients()
    backToPizzaButton()
    addToOrderButton()

def margherita(): # function for adding margherita pizza to order. See supreme() for more information.
    main.clearWindow(ordersWindow)
    pizzaType[0] = "Margherita Pizza"
    ordersWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Fresh Mozzerella", "Fresh Basil"]
    pizzaSauce[0] = "Marinara"
    radioSize()
    showIngredients()
    backToPizzaButton()
    addToOrderButton()

def veggieExplostion(): # function for adding vegetable pizza to order. See supreme() for more information.
    main.clearWindow(ordersWindow)
    pizzaType[0] = "Veggie Explosion Pizza"
    ordersWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Bell Peppers", "Onion", "Mushrooms", "Black Olives", "Green Olives", "Cheese"]
    pizzaSauce[0] = "Marinara"
    radioSize()
    showIngredients()
    backToPizzaButton()
    addToOrderButton()

def chickenAlfredo(): # function for adding chicken alfredo pizza to order. See supreme() for more information.
    main.clearWindow(ordersWindow)
    pizzaType[0] = "Chicken Alfredo Pizza"
    ordersWindow.title(pizzaType[0])
    pizzaIngredients[0] = ["Chicken", "Cheese"]
    pizzaSauce[0] = "Alfredo"
    radioSize()
    showIngredients()
    backToPizzaButton()
    addToOrderButton()

def customPizza(): # function for adding custom pizza to order. See supreme() for more information.
    main.clearWindow(ordersWindow)
    pizzaType[0] = "Custom Pizza"
    ordersWindow.title(pizzaType[0])
    pizzaIngredients[0] = []
    radioSize()
    showIngredients()
    customPizzaIngredients()
    radioSauce()
    backToPizzaButton()
    addToOrderButton()

def radioSize(): # function that creates size selection radio buttons
    sizeSelection.set("Small") # sets the default size to small
    cost[0] = 9.99 # sets default cost to 9.99
    pizzaSize[0] = sizeSelection.get() # sets pizza size to currently selected size radio button
    radioSizeFrame = ttk.Frame(ordersWindow)
    radioSizeFrame.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "NW")
    sizeLabel = ttk.Label(radioSizeFrame, text = "Size: ")
    sizeLabel.grid()
    # creates size radio buttons
    sizeSmallRadio = ttk.Radiobutton(radioSizeFrame, text = "Small", var = sizeSelection, value = "Small", command = setSize)
    sizeSmallRadio.grid()
    sizeMedRadio = ttk.Radiobutton(radioSizeFrame, text = "Medium", var = sizeSelection, value = "Med", command = setSize)
    sizeMedRadio.grid()
    sizeLargeRadio = ttk.Radiobutton(radioSizeFrame, text = "Large", var = sizeSelection, value = "Large", command = setSize)
    sizeLargeRadio.grid()

def radioSauce(): # fucntion that creates sauce selection radio buttons
    sauceSelection.set("Marinara") # sets default sauce to marinara
    pizzaSauce[0] = sauceSelection.get() # sets pizza size to currently selected sauce radio button
    radioSauceFrame = ttk.Frame(ordersWindow)
    radioSauceFrame.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "NW")
    sauceLabel = ttk.Label(radioSauceFrame, text = "Sauce: ")
    sauceLabel.grid()
    # creates sauce radio buttons
    sauceMarRadio = ttk.Radiobutton(radioSauceFrame, text = "Marinara", var = sauceSelection, value = "Marinara", command = setSauce)
    sauceMarRadio.grid()
    sauceBBQRadio = ttk.Radiobutton(radioSauceFrame, text = "BBQ", var = sauceSelection, value = "BBQ", command = setSauce)
    sauceBBQRadio.grid()
    sauceAlfRadio = ttk.Radiobutton(radioSauceFrame, text = "Alfredo", var = sauceSelection, value = "Alfredo", command = setSauce)
    sauceAlfRadio.grid()
    sauceNoneRadio = ttk.Radiobutton(radioSauceFrame, text = "None", var = sauceSelection, value = "None", command = setSauce)
    sauceNoneRadio.grid()

def setSize(): # function that sets pizza size and cost to currently seleceted size 
    pizzaSize[0] = sizeSelection.get()
    if sizeSelection.get() == "Small":
        cost[0] = 9.99
    elif sizeSelection.get() == "Med":
        cost[0] = 14.99
    elif sizeSelection.get() == "Large":
        cost[0] = 19.99
    global costLabel
    costLabel.destroy() # destroys costLabel so it can be repopulated
    costLabel = ttk.Label(ingredientsFrame, text = "\nPrice: " + str(cost[0]))
    costLabel.grid()

def setSauce(): # function that sets pizza sauce to currentlt selected sauce
    pizzaSauce[0] = sauceSelection.get()

def backToPizzaButton(): # function that creates button for returning to the main pizza ordering window
    backToPizzaButton = ttk.Button(ordersWindow, text = "Back", command = backToPizza)
    backToPizzaButton.grid(padx = 5, pady = 10)

def backToPizza(): # function that clears current pizza window so it can be repopulated with the main buttons
    main.clearWindow(ordersWindow)    
    ordersPizzaMain()

def addToOrderButton(): # function that creates the button for adding a pizza to order
    addToOrderButton = ttk.Button(ordersWindow, text = "Add To Order", command = addPizzaOrder)
    addToOrderButton.grid(padx = 5, pady = 10)

def addPizzaOrder(): # function for pizza add to order button
    if pizzaIngredients[0] == []: # creates error messages if selected ingredients list is empty
        messagebox.showerror("Please add ingredients","You must add at least one ingredient to your pizza.")
    else:
        global itemCount
        # creates dictionary entry for currently selected pizza
        order[itemCount] = {"type": pizzaType[0], "size": pizzaSize[0], "sauce": pizzaSauce[0], "ingredients": str(", ".join(pizzaIngredients[0])), "cost": cost[0]}
        itemCount = itemCount + 1 # iterates item count to identify items in order
        labelFrame = ttk.Frame(ordersWindow)
        labelFrame.grid(row = 5, columnspan = 5)
        addPizzaLabel = ttk.Label(labelFrame, text = pizzaSize[0] + " " + pizzaType[0] + " has been added to the order.")
        addPizzaLabel.grid(columnspan = 5)


def showIngredients(): # creates frame for ingreditents on currently selected pizza
    global ingredientsFrame
    global costLabel
    ingredientsFrame = ttk.Frame(ordersWindow)
    ingredientsFrame.grid(row = 0, column = 4, rowspan = 2, padx = 5, pady = 5, sticky = "NW")
    ingredientsLabel = ttk.Label(ingredientsFrame, text = "Ingredients:")
    ingredientsLabel.grid()
    ingredientsListLabel = ttk.Label(ingredientsFrame, text = "\n".join(pizzaIngredients[0]))
    ingredientsListLabel.grid()
    sauceLabel = ttk.Label(ingredientsFrame, text = "\nSauce:")
    sauceLabel.grid()
    sauceTypeLabel = ttk.Label(ingredientsFrame, text = pizzaSauce[0])
    sauceTypeLabel.grid()
    costLabel = ttk.Label(ingredientsFrame, text = "\nPrice: " + str(cost[0]))
    costLabel.grid()

def customPizzaIngredients(): # creates frame for selecting ingredients for custom pizza
    customIngFrame = ttk.Frame(ordersWindow)
    customIngFrame.grid(row = 0, column = 3)
    global ingListbox
    ingredientsLabel = ttk.Label(customIngFrame, text = "Ingredients: ")
    ingredientsLabel.grid()
    # creates list box for selecting multiple ingredients from the custom ingredient list
    ingListbox = tk.Listbox(customIngFrame, height = 13, selectmode = "multiple", selectbackground= "red", listvariable = ingSelectVar)
    ingListbox.grid()
    applyCustomButton = ttk.Button(customIngFrame, text = "Apply Ingredients", command = setCustomIng) # creates button for setting the currently selected ingredients
    applyCustomButton.grid()

def setCustomIng(): # function for setting the custom ingredients and repopluating displayed ingredients list
    pizzaIngredients[0] = [ingredientList[item] for item in ingListbox.curselection()]
    ingredientsFrame.destroy()
    showIngredients()


def sidesWindow(): # creates popup for adding sides to the order
    global ordersWindow
    ordersWindow = tk.Toplevel()
    ordersSides()

def ordersSides(): # populates sides radio buttons
    ordersWindow.title("Sides")
    ordersWindow.config(bg = "green")
    ordersWindow.minsize(300, 300)
    ordersWindow.maxsize(300, 300)
    ordersWindow.grab_set()
    sidesRadioFrame = ttk.Frame(ordersWindow)
    sidesRadioFrame.grid(padx = 10, pady = 10)
    sideSelection.set(0)
    cost[0] = sidesList[int(sideSelection.get())]["cost"]
    global costLabel
    for item in sidesList:
        button = ttk.Radiobutton(sidesRadioFrame, text = sidesList[item]["item"], variable = sideSelection, value = item, command = setCostSide)
        button.grid()
    addSideOrderButton()
    costLabel = ttk.Label(ordersWindow, text = "\nPrice: " + str(cost[0]))
    costLabel.grid()
    

def addSideOrderButton(): # creates button for adding selected side to order
    addToOrderButton = ttk.Button(ordersWindow, text = "Add To Order", command = addSideOrder)
    addToOrderButton.grid(padx = 5, pady = 10)

def addSideOrder(): # adds currently selected side item to the order dictionary
    global itemCount
    order[itemCount] = {"type": sidesList[int(sideSelection.get())]["item"], "size": "---", "ingredients": "---", "cost": sidesList[int(sideSelection.get())]["cost"]}
    itemCount = itemCount + 1 # iterates item count
    labelFrame = ttk.Frame(ordersWindow)
    labelFrame.grid(row = 5, columnspan = 10, sticky = "E")
    addSideOrderLabel = ttk.Label(labelFrame, text = "")
    addSideOrderLabel.grid()
    addSideOrderLabel.config(text = sidesList[int(sideSelection.get())]["item"] + " has been added to the order.") # displays that item has been added to order

def setCostSide(): # repopulates item cost when a new side item is selected
    global costLabel
    cost[0] = sidesList[int(sideSelection.get())]["cost"] # sets cost to the selected item from the sides list dictionary
    costLabel.config(text = "\nPrice: " + str(cost[0]))
