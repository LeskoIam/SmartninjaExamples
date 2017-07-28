__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

menu = {}
def add_dish():
    while True:
        item = raw_input("Would you like to add a new dish(yes/no)?")
        if item == "yes":
            while True:
                name = raw_input("Enter new DISH: ")
                if len(name) > 0 and name.isalpha():
                    print name
                    break
                else:
                    print "Wrong input. Try again"
                    pass

            while True:
                try:
                    price = float(raw_input("Enter a cost of the dish: "))
                    if price == int(price) or price == float(price):
                        print price
                        break
                except (ValueError, IndexError) as e:
                    print e.message
                    pass
            menu[name] = price
            print "Menu: %s" % menu

        elif item == "no":
            print "Goodbye"
            break

def del_dish():
    print menu
    dish_remove = str(raw_input("Enter a dish you would like to remove: "))
    if dish_remove in menu:
        del menu[dish_remove]


def see_menu():
    print "Menu: %s" % menu

print "This is MenuPlan program. Welcome!"
a = raw_input ("You can add, remove and see dishes from the menu. To ADD new dishes choose 1, to REMOVE dishes choose 2, to SEE the menu choose 3, to QUIT choose 4: ")
while True:
    if a == "1":
        add_dish()
    a = raw_input("You can add, remove and see dishes from the menu. To ADD new dishes choose 1, to REMOVE dishes choose 2, to SEE the menu choose 3, to QUIT choose 4: ")

    if a == "2":
        del_dish()
        print menu
    if a== "3":
        see_menu()
        continue
    if a =="4":
        break

with open("menu.txt", "w+") as menu_file:
   menu_file.write("Menu:  %s = %s" %(name, price))

