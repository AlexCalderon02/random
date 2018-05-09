#from graphics import *


file = open("data.txt","w+")
file.write("jhlk")
interval = len(file.readlines())
file.close
raw_input()

def main():
    file()
	
	
#def http():
#    print("temp")


def file(): 
    try:
        file = open("data.txt","a+")
        file.write("jhlk")
        #interval = len(file.readlines())
    finally:
        file.close
    return 0
	
	
file()