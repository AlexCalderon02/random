# noinspection PyUnresolvedReferences
import urllib.request
# noinspection PyUnresolvedReferences
import urllib.parse
# noinspection PyUnresolvedReferences
import urllib.error
# noinspection PyUnresolvedReferences
import re
from graphics import *

# URL for desired site ---------
# url = "https://pythonprogramming.net"
# url = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=USD"
# url = "https://www.google.com/search?q=test"
url = "http://x-rates.com/calculator/?from=GBP&to=USD&amount=1"
# ---------------

# Setting up variables
test = 0
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"
# user_agent to trick site that a program is not accessing it
headers = {"User-Agent" : user_agent}
values_1 = {"s":"test",
          "submit":"Search"}
values = {"Amount":"1",
            "From":"GBP",
            "To":"USD"}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')


# Requesting info from URL
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)

# Filtering HTML from site for specific value using Regular Expression module(RE)
tester = re.findall(r"<p>(.*?)</p>",str(the_page))
USD = re.findall(r"""<span class="ccOutputRslt">(.*?)<""",str(the_page))
print(str(tester))
print(str(USD[0]))  # Values gathered by RE module are stored as a list
file_check = open("data.txt","r") # Opening text file to store gathered data
file_lines = sum(1 for line in file_check) # Finds out how many lines are in the text file
file_check.seek(0)  # Sets the filing position/read cursor to 0, the beginning of the text file
file_list = []  # initializing a list to hold each line of data.txt
for line in file_check: # Appends each line of the text file into a list for later use
    print(line)
    file_list.append(line)
    print(file_list)
file_check.close()
file_list = [x.replace("\n","") for x in file_list]  # "Remove" special character '\n' from strings in the list
file_list = [x.replace(".","") for x in file_list]  # "Remove" special character '\n' from strings in the list
file_list = [int(x) for x in file_list]  # Changes strings in file_list to floats
print(file_list)
# Continue appending data to text file until there is a given amount of lines
if file_lines >= 10:
    print("lel")
else:
    print(file_lines)
    file_save = open("data.txt","a+")
    file_save.write(str(USD[0])+"\n")
    file_save.close()
print(file_list)
print(file_lines)
#response_1 = urllib.request.urlopen(url)
#print(response_1.read())

#  Rest is displaying information
def main(value_list, amount_list):
    print(value_list)
    length = 5000
    height = 5000
    line_color = "white"
    background_color = "black"
    win = GraphWin("Money", length, height) # Creates graph with specified dimensions and colors
    win.setBackground(background_color)
    horz_int = height/10
    vert_int = length/10
    # Creating graph in window
    x_temp_1 = 0
    for x in range(amount_list): # Create points and lines
        print("nein")
        x_temp_1 += 10
        line = Line(x_temp_1, value_list[x])
    print("works")
    #win.getMouse() # Waits for mouse input before closing
    win.close()

print(file_list)
main(file_list, file_lines)
