def collatz(number):
    value = 0
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1

    return value


print('Enter number:')

try:
    number = int(input())
except ValueError:
    print('Please enter an integer')

while number != 1:
    number = collatz(number)
    print(number)
