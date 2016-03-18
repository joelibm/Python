#number = int(input("What pocket number would you like to know the color of? "))
number = 0
while (number <= 37):
    if number == 0:
        color = "green"
    elif (1 <= number <= 10) or (19 <= number <= 28):
        if number % 2 == 1:
            color = "red"
        elif number % 2 == 0:
            color = "black"
    elif (11 <= number <= 18) or (29 <= number <= 36):
        if number % 2 == 1:
            color = "black"
        elif number % 2 == 0:
            color = "red"
    else:
        color = "not on a roulette wheel"
    print ("Pocket number ", number, " is ",color,".",sep='')
    number = number + 1

