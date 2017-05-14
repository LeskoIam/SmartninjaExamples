import Tkinter
import random
import tkMessageBox
import time

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


def check_guess():
    # Simulate long running process
    time.sleep(10)
    if int(guess.get()) == secret:
        result_text = "CORRECT!"
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    tkMessageBox.showinfo("Result", result_text)

# GUI
window = Tkinter.Tk()

# Greeting text
greeting = Tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# Select random number
secret = random.randint(1, 100)

# Guess entry field
guess = Tkinter.Entry(window)
guess.pack()

# submit button
submit = Tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()


window.mainloop()
