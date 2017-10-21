import sys
import random

print('Press enter to exit!')
question = input('Ask the Magic 8 Ball a question: ')

answers = random.randint(1,20)

if question == "": #Checks for empty answer, if so terminate program.
    sys.exit()


elif answers == 1:
    print('It is certain')

elif answers == 2:
    print('As I see it, yes')

elif answers == 3:
    print('Reply hazy try again')

elif answers == 4:
    print('Do not count on it')

elif answers == 5:
    print('It is decidedly so')

elif answers == 6:
    print('Most likely')

elif answers == 7:
    print('Ask again later')

elif answers == 8:
    print('My reply is no')

elif answers == 9:
    print('Without a doubt')

elif answers == 10:
    print('Outlook good')

elif answers == 11:
    print('Better not tell you now')

elif answers == 12:
    print('My sources say no')

elif answers == 13:
    print('Yes definitely')

elif answers == 14:
    print('Yes')

elif answers == 15:
    print('Cannot predict now')

elif answers == 16:
    print('Outlook not so good')

elif answers == 17:
    print('You may rely on it')

elif answers == 18:
    print('Signs point to yes')

elif answers == 19:
    print('Concentrate and ask again')

elif answers == 20:
    print('Very doubtful')
