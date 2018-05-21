count = 0
sum = 0
while True:
    elem = input("Enter the element: ")    
    try:
        ele = int(elem)
        count += 1
        sum += ele
    except:
        if(elem == "done"):
            break 
        else:
            print("Invalid input!")
            continue
print("Total = ", count, " Sum = ",sum," Average = ",sum/count)
