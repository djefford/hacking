# This program says hello and asks for my name.

print ('Hello World!')

print('What is your name?') # ask for the name
myName = input()

print('It is good to meet you, {}'.format(myName))
print('The length of your name is: {}'.format(len(myName)))

print('What is your age?') # ask for the age
myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year.')