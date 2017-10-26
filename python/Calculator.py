def sub(a, b):
   return a - b

def add(a, b):
   return a + b

def multi(a, b):
   return a * b

def div(a, b):
   return a / b

print("1.) Subtract")
print("2.) Add")
print("3.) Multiply")
print("4.) Divide")

choice = input("Enter your choice:")
dig1 = int(input("Enter first digit: "))
dig2 = int(input("Enter second digit: "))

if choice == "1":
    print(dig1, "-", dig2, "=" , sub(dig1, dig2))

elif choice == "2":
   print(dig1, "+", dig2, "=" , add(dig1, dig2))

elif choice == "3":
   print(dig1, "*" ,dig2, "=" , multi(dig1,dig2))

elif choice == "5":
   print(dig1, "/" ,dig2, "=" , div(dig1,dig2))
else:
   print("Invalid")