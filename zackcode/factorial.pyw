import sys
#from tkinter import *
import tkinter as tk # Importing Tkinter
import win32gui, win32con

# Hides the console when executing the program
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)

# -= Code to find the factorial of a number =-
#x = input("Enter a number to find its factorial...\n")
x = 0

# Function to find factorial
def factorial(z):
	if z == 1:
		return 1
	else:
		y = z * factorial(z-1)
		return y
# -= =-

# Tkinter for displaying the graphical part of this program
root = tk.Tk() # Initializing Tkinter through a root window

# Text displayed at the top of the window
title = tk.Label(root) 
title["text"] = "Please enter a number here:"
title.pack()

# entry box widget
tkInput = tk.Entry(root) # Creates an entry box
tkInput.pack()

# Function that takes the input from the entry box and diplays it on screen
def return_string():
	stringOutput = tkInput.get() # Gets the input given to the 'Entry' widget
	stringOutput = int(stringOutput) 
	newStringOutput = factorial(stringOutput) # Runs the number through the factorial function
	return w2.configure(text="%.2f" % newStringOutput) # Updates the answer each time submit is clicked

# button widget
button = tk.Button(root, text="-=Submit=-", command=return_string) # Creates a button that runs a command
button.pack()
gif = tk.PhotoImage(file="giphy_40.gif")
#def gif_test():
#	prgif = "gif not found"
#	try:
#		gif = tk.PhotoImage(file="giphy_40.gif") # Creates an image using the specified gif
#	#return:
#	return prgif
#gif_test()
w1 = tk.Label(root, image=gif).pack(side="top") # Displays an image (using the label widget)
w2 = tk.Label(root, justify=tk.CENTER, text = "") # Label widget with the parent window "root"
w2.pack() # Fits the size of the window to the text allowing for the view of all text

root.mainloop() # Allows the window to be displayed until it is closed