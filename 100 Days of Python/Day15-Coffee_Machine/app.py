import time
import os

is_turned_off= False
resources = {
    "Water": 0,
    "Milk": 0,
    "Sugar": 0,
    "Coffee Beans": 0,
    "Chocolate": 0,
    "Creamer": 0,
    "Money": 0
}

coffee_requirements = ([50,150,0,20,0,0,1.75],[200,150,0,24,0,0,2.5],[150,150,0,24,0,0,3],[0,250,0,0,80,0,2.25])

def add_resource():
    _water = int(input("Please enter amount of water in ml: "))
    resources["Water"] += _water 
    print("Water added!")
    _milk = int(input("Please enter amount of milk in ml: "))
    resources["Milk"] += _milk
    print("Milk added!") 
    _sugar = int(input("Please enter weight of sugar in g: "))
    resources["Sugar"] += _sugar 
    print("Sugar added!")
    _coffee_beans = int(input("Please enter weight of coffee beans in g: "))
    resources["Coffee Beans"] += _coffee_beans 
    print("Coffee Beans added!")
    _chocolate = int(input("Please enter weight of chocolate in g: "))
    resources["Chocolate"] += _chocolate 
    print("Chocolate added!")
    _creamer = int(input("Please enter amount of creamer in ml: "))
    resources["Creamer"] += _creamer 
    print("Creamer added!")

    print_report()

def check_transaction():
    pass

def process_coin(str):
    quarters = 0.25
    dimes = 0.10
    nickle = 0.05
    pennies = 0.01
    price = 0

    if str == 'espresso':
        price = coffee_requirements[0][-1]
        print("Please Enter ")

    elif str == 'latte':
        pass
    elif str == 'cappuccino':
        pass
    elif str == 'hot chocolate':
        pass
    


def check_resources(str):
    str = str.lower()
    if str == 'espresso':
        if resources["Water"]> coffee_requirements[0][0]:
            if resources["Milk"] > coffee_requirements[0][1]:
                if resources["Coffee Beans"] > coffee_requirements[0][3]:
                    print("Resource Requirements are met for Espresso")
                    print("Starting Coffee Making")
                    os.system("Clear")
                    make_coffee('espresso')


    elif str == 'latte':
        if resources["Water"]> coffee_requirements[1][0]:
            if resources["Milk"] > coffee_requirements[1][1]:
                if resources["Coffee Beans"] > coffee_requirements[1][3]:
                    print("Resource Requirements are met for Latte")
                    print("Starting Coffee Making")
                    os.system("Clear")
                    make_coffee('latte')

    elif str == 'cappuccino':
        if resources["Water"]> coffee_requirements[2][0]:
            if resources["Milk"] > coffee_requirements[2][1]:
                if resources["Coffee Beans"] > coffee_requirements[2][3]:
                    print("Resource Requirements are met for Cappuccino")
                    print("Starting Coffee Making")
                    os.system("Clear")
                    make_coffee('cappuccino')
    elif str == 'hot chocolate':
        if resources["Milk"] > coffee_requirements[3][1]:
            if resources["Chocolate"] > coffee_requirements[3][4]:
                print("Resource Requirements are met for Hot Chocolate")
                print("Starting Hot Chocolate Making")
                os.system("Clear")
                make_coffee('hot chocolate')
                    
    else:
        print("Invalid Entry!")

def place_order():
    order = input("What would you like? (espresso / latte / cappuccino / hot chocolate ): ")
    check_resources(order)


def make_coffee(str):
    if str == 'espresso':
        resources["Water"] = resources["Water"] - coffee_requirements[0][0]
        resources["Milk"] = resources["Milk"] - coffee_requirements[0][1]
        resources["Coffee Beans"] = resources["Coffee Beans"] - coffee_requirements[0][3]

    elif str == '':
        pass
    elif str == '':
        pass
    elif str == '':
        pass
    else:
        pass


def turn_off(str):
    if str.lower() == "off":
        is_turned_off = True
        return is_turned_off
        # exit(0)
    else:
        print('invalid value returning to main menu')
        time.sleep(10)
        os.system('clear')
        

def print_report():
    print("###############   Report   ###############")
    print("# Water: " + str(resources["Water"]) + "ml\t \t \t \t #" )
    print("# Milk: " + str(resources["Milk"])  + "ml\t \t \t \t #")
    print("# Sugar: " + str(resources["Sugar"]) + "g\t \t \t \t #")
    print("# Coffee Beans: " + str(resources["Coffee Beans"])  + "g \t \t \t #")
    print("# Chocolate: " + str(resources["Chocolate"]) + "g\t \t \t #")
    print("# Creamer: " + str(resources["Creamer"]) + "ml\t \t \t #")
    print("# Money: " + str(resources["Money"])  + "$\t \t \t \t #")
    print("##########################################")
    
    
# while not is_turned_off:

add_resource()

