def comma(arguments):

    new_args = ''
    for item in arguments[:-1]:
        new_args += item + ', '    
    new_args += 'and ' + arguments[-1]

    return new_args 


myList = []

while True:

    print('Enter list item {} (Or enter to quit)'.format(str(len(myList) + 1)))
    listItem = input()

    if listItem == '':
        break

    myList.append(listItem)

print(comma(myList))