import sys
import urllib.request
import urllib.error
import urllib.parse
#from tkinter import *
#from twill.commands import *
import tkinter as tk # Importing Tkinter as tk
import win32gui, win32con

# Hides the console when executing the program
#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide , win32con.SW_HIDE)

# Setting up variables
url = "https://www.ebay.com"
test = 0
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"
# user_agent to trick site that a program is not accessing it
headers = {"User-Agent" : user_agent}
values_1 = {"username":" ",
          "password":" ",
          "url":" ",
          "bid":" "}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

def put_bid(finalBid):
	print(finalBid)

def log_in(url, email, password, bid):
	#go(url)

	#fv("1", "email-email", "blabla.com")
	#fv("1", "password-clear", "testpass")

	#submit('0')
	values_1.update({"username" : email, "password" : password, "url" : url, "bid" : bid})
	[print(key + ": " + values_1[key]) for key in values_1]
	bid = float(bid)
	print(bid)
	put_bid(bid)

	#print(keys)

#
#email = "email@email.com"
#password = "password"
#bid = "20"
#log_in(url, email, password, bid)
#

# Requesting info from URL
req = urllib.request.Request(url)#, headers=headers)
response = urllib.request.urlopen(req)
the_page = response.read()
#print(the_page)

# Tkinter for displaying the graphical part of this program
root = tk.Tk() # Initializing Tkinter through a root window

# Text displayed at the top of the window
title1 = tk.Label(root) 
title1["text"] = "Please enter a valid eBay URL:"
title1.pack()

# entry box widget
tkInput1 = tk.Entry(root) # Creates an entry box
tkInput1.pack()

# Text that is displayed
title2 = tk.Label(root) 
title2["text"] = "Please enter the highest bid you want:"
title2.pack()

# Entry widget
tkInput2 = tk.Entry(root)
tkInput2.pack()

# Text displayed at the top of the window
title3 = tk.Label(root) 
title3["text"] = "Please enter a valid eBay login email:"
title3.pack()

# entry box widget
tkInput3 = tk.Entry(root) # Creates an entry box
tkInput3.pack()

# Text that is displayed
title4 = tk.Label(root) 
title4["text"] = "Please enter your eBay password:"
title4.pack()

# Entry widget
tkInput4 = tk.Entry(root)
tkInput4.pack()

def check_url():
	print("needs work")

def gather_values():
	url = tkInput1.get() # Gets the input given to the 'Entry' widget
	bid = tkInput2.get()
	email = tkInput3.get()
	password = tkInput4.get()
	newStringOutput = url+bid+email+password
	log_in(url, email, password, bid)
	print(bid)
	return w2.configure(text="%s" % newStringOutput) # Updates the answer each time submit is clicked %.2f for floats

# button widget
button = tk.Button(root, text="-=Submit=-", command=gather_values) # Creates a button that runs a command
button.pack()

#w1 = tk.Label(root, image=gif).pack(side="top") # Displays an image (using the label widget)
w2 = tk.Label(root, justify=tk.CENTER, text = "") # Label widget with the parent window "root"
w2.pack() # Fits the size of the window to the text allowing for the view of all text

root.mainloop() # Allows the window to be displayed until it is closed