import Tkinter
import random
import tkMessageBox
import time

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

# check guess
def check_guess():
    time.sleep(10)
    if int(guess.get()) == secret:
        result_text = "CORRECT!"
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    tkMessageBox.showinfo("Result", result_text)


window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# Select number to guess
secret = random.randint(1, 100)

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# submit button
submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()
