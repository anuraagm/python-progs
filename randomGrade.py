import random
import math

def randGrade(num):
    if(num > 0.9):
        return "A"
    if(num > 0.8):
        return "B"
    if(num > 0.7):
        return "C"
    if(num > 0.6):
        return "D"        
    if(num < 0.6):
        return "F"
while(True):        
    num = random.random()
    print(num, randGrade(num))