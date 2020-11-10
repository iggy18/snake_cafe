def line():
    print(38*"*")

def short_line():
    print(35*"*")

active = True

menu = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0,
}

print("$ python snakes_cafe.py")
line()
print('''
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
''')
print("** To quit at any time, type \"quit\" **")
line()
print('''

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

''')
short_line()
print("** What would you like to order? **")
short_line()

while active:
    order = input(">")
    if order == "quit":
        active = False
        print(" your order is: ")
        for item in menu.keys():
            if menu[item] == 1:
                print(f" ** {menu[item]} order of {item} ** ")
            if menu[item] > 1:
                print(f" ** {menu[item]} orders of {item} ** ")
        print("thanks for your order!")
        break
    if order not in menu:
      print("we do not offer " + (order))
    else:
        for item in menu.keys():
          if item == order:
            menu[order] += 1
            number = menu[order]

        if number == 1:
            print(f"** {str(number)} order of {order} has been added to your meal **")
        elif number > 1:
          print(f"** {str(number)} orders of {order} have been added to your meal **")