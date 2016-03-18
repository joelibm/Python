cost = float(input("What was the cost? "))
pay = float(input("What did the customer pay? "))
change = pay - cost
dollars = int(change)
cents = (change - dollars) * 100
quarters = int(cents // 25)
cents = cents - quarters * 25
dimes = int(cents // 10)
cents = cents - dimes * 10
nickels = int(cents // 5)
cents = int(cents - nickels * 5)
print (dollars," dollars, ", quarters," quarters, ", dimes," dimes, ", nickels," nickels, and ", cents," pennies.")

dollars = 0
quarters = 0
dimes = 0
nickels = 0
cents = 0
while change >= 1:
    dollars += 1
    change -= 1
while change >= .25:
    quarters += 1
    change -= .25
while change >= .1:
    dimes += 1
    change -= .1
while change >= .05:
    nickels += 1
    change -= .05
while change >= .01:
    cents += 1
    change -= .01
print (dollars," dollars, ", quarters," quarters, ", dimes," dimes, ", nickels," nickels, and ", cents," pennies.")

