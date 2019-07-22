#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

## Start functions

def maxLength(myList):
    
    length = 0 
    
    for item in myList:
        if len(item) > length:
            length = len(item)

    return length

def printTable(myTable, colWidths):

    for i in range(len(myTable[1])):
        for j in range(len(myTable[:])):
            print(myTable[j][i].rjust(colWidths[j]), end=' ')
        print()

## Start program

colWidths = []

for i in tableData:
    length = maxLength(i)
    colWidths.append(length)

printTable(tableData, colWidths)