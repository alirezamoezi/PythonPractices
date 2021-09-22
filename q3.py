first = int(input("Please enter the first number."))
second = int(input("Please enter the second number."))
while (second != 0):
    Remainder = first % second
    first = second
    second = Remainder
print(first)
