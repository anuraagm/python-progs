count = input("Enter number of numbers: ")
i=0
while i < int(count):
    num = input("Enter a number")
    if int(num)<0:
        print("number is negative")
    elif int(num) == 0:
        print("Bro do you even math?")
    else:
        print("number is positive")
    i+=1    