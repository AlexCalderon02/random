import random

def main():
    
    min = 1;max = 6
    reroll = "yes"
    while reroll == "yes" or reroll == "y":

        print("Rolling... Values are: ")
        print(random.randint(min, max))
        print(random.randint(min, max))
        
        # Ask the user if they want to rerun
        reroll = input("Do you want to roll again?")

if __name__ == '__main__':
    # Rerun program
    main()
