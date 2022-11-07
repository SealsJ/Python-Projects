#Create a class to hold our functions for shopping cart
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        #Creaty empty list, use __cart to prevent 'hackers'/ can only access from inside function
        self.__cart = []

    #take item and add it to the cart
    def addCart(self, item):
        self.__cart.append(item)

    #take item and remove it from the cart
    def removeCart(self, index):
        self.__cart.pop(index)

    def total(self):
        total = 0
        for item in self.__cart:
            total += item.price

        return total

    def displayCart(self):
        for i in range(0, len(self.__cart)):
            print(i, self.__cart[i].name)

#Creating store variable and prompt user to add things into their cart
store = Store()
store.displayCart()

print("Hello! Welcome to the Seals Store!")
#Use while loop to keep prompting user to add things to cart
while True:
    store.displayCart()
    store.total()


    print("Press a to add an item!")
    print("Press r to remove an item!")
    print("press x to exit")
    userChoice = input("Please enter a command: ").lower()

    #if statements for the options that are available for the user to use
    if userChoice == "x":
        break
    elif userChoice == "a":
        name = input("Please enter the item's name: ")
        price = int(input("Please ente the item's price: $"))
        store.addCart(Item(name, price))
    elif userChoice == "r":
        index = int(input("Please rovide the index of the item to remove: "))
        store.removeCart(index)
    else: #incase the user inputs something unexpected
        print("Please enter a valid input")

