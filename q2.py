import math

n = int(input("Please enter the number"))
listOfDenominators = []
listOfPrimes = []
for i in range (1, n+1):
    listOfDenominators.clear()
    for j in range (1, i+1):
        if i % j == 0:
            listOfDenominators.append(j)
    if len(listOfDenominators) == 2:
        listOfPrimes.append(i)
for item in listOfPrimes:
    print(item)