def add(x,y):
    sum = x+y
    global funcVar
    funcVar = 40
    return sum
num1 = 10
num2 = 20
print("Sum of the numbers =", add(num1,num2))
print("funVar = ", funcVar)