# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, {}, I am thinking of a number between 1 and 20.'.format(myName))

for guessesTaken in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"
    
    if guess > number:
        print('Your guess is too high.')
    
    if guess == number:
        break   # This is a correct answer

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, {}! You guessed my number in {} guesses!'.format(myName, guessesTaken))

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was {}.'.format(number))
