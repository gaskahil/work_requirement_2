import random

highest = 100

num1 = random.randint(1, highest)
num2 = random.randint(1, highest)

answer = num1 + num2

#print(answer)      #Used while testing code
try:
    guess = int(input("Please add "'{}'" + "'{}: '.format(num1, num2)))
    if answer != guess:
        print('Sorry, incorrect')
    elif answer == guess:
        print('Correct!')
except ValueError:
    print("That is not a number. Try again!")
