import tkMessageBox
from Tkinter import Tk, YES, NO

root = Tk()

name = raw_input("What is your name?")
name_corrected = name.strip().capitalize()


print "Hi", name_corrected, "."

answer = tkMessageBox.askyesno(title="Ask for more", message="Do you want to convert units?")

while answer == YES:

    number_of_km = raw_input("Enter number of kilometers")
    number_of_km_checked = number_of_km.isdigit()

    while not number_of_km_checked:
        print "Please enter valid number. Only digits are aceptable"
        number_of_km = raw_input("Enter number of Kilometers")
        number_of_km_checked = number_of_km.isdigit()

    number_of_m = int(number_of_km)*1000
    number_of_cm = int(number_of_km) * 10000

    print "That is", number_of_m, "meters. That is", number_of_cm, "centimeters."
    answer = tkMessageBox.askyesno(title="Ask for more", message="Do you want to convert more units?")

if answer == NO:
    print "Goodbye", name_corrected, "and thank you for your visit."