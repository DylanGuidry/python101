#Input for user
print('Please choose a number between 0 and 6 below... ')

#Numeric for each day of the week
try:
    day = int(input('(0-6)? '))

    if (day) == 0:
        print("Sunday")
    elif (day) == 1:
        print("Monday")
    elif (day) == 2:
        print("Tuesday")
    elif (day) == 3:
        print("Wednesday")
    elif (day) == 4:
        print("Thursday")
    elif (day) == 5:
        print("Friday")
    elif (day) == 6:
        print("Saturday")
    else:
        print("Please insert a listed value.")
except ValueError: print("Invalid.")