import random

number = random.randint(1,100)
running = True
numberGuess = 0

while running:
    guess = int(input('Enter an integer : '))
    numberGuess += 1
    
    if guess == number:
        print('Congratulations, you guessed it.')
        print("Number of tries: {}".format(numberGuess))
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
        # Do anything else you want to do here

print('Done')