

def sumfunction():
    total = 0
    numlist = [1, 4, 6, 10]

    for i in range(0, len(numlist)):
        total = total + numlist[i]

    print("Sum of " + str(numlist) + " is " + str(total))


sumfunction()