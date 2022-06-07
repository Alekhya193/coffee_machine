MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 20,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit=0
is_on=True

# def money(esp,lat,cap):
#     one=input("how many one: ")
#     two=input("how many two: ")
#     five=input("how many five: ")
#     if

# def enoughmoney():

def resource_sufficient(ordIng):
    for i in ordIng:
        if ordIng[i]>resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

def process_coins():
    print("Insert coins: ")
    total = int(input("how many 1 rs coins: "))*1
    total += int(input("how many 2 rs coins: "))*2
    total+= int(input("how many 5 rs coins: "))*5
    return total

def transaction(rec_money,act_cost):
    if rec_money>=act_cost:
        change = act_cost = rec_money
        print(f"Here i ur change {change}")
        global profit
        profit+=act_cost

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,ord_ing):
    for i in ord_ing:
        resources[i]-=ord_ing[i]
    print(f"Here is your {drink_name} !!!")


while is_on:
 choose=input("What would you like? (espresso/latte/cappuccino):")
 if choose=="off":
     is_on=False
 elif choose=="report":
     print(f"Water: {resources['water']}ml")
     print(f"Milk: {resources['milk']}ml")
     print(f"Coffee: {resources['coffee']}g")
     print(f"Money: ${profit}")
 else:
     drink=MENU[choose]
     if resource_sufficient(drink["ingredients"]):
         payed=process_coins()
         if transaction(payed,drink["cost"]):
             make_coffee(choose,drink["ingredients"])





