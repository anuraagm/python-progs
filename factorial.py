def findFactorial(number):
    if(number == 0):
        return number
    else:
        return number*(number-1)
num = input("Enter the number to find factorial of: ")
print("The factorial = ",findFactorial(num))
