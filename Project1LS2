#1 Display Welcome Message
print ("Welcome to the 1089 trick!")
#2 Display About Message
about_message_1 = " This trick's sure to amaze your friends."
about_message_2 = """It's believed that the "1089 trick" was a favorite of Albert Einstein."""
about_message_3 = "To begin, enter a number with 3 digits, where the 1st digit and the 3rd digit differ by at least 2."
print (about_message_1,"\n",about_message_2,"\n",about_message_3)
#3 Input a number from the user
number= int(input("Enter a number: "))
#4 Check that the number has 3 digits, and do not continue if not
#5 Check that the 1st digit and the 3rd digit differ by at least 2, and do not continue ifnot
#6 Calculate the reverse of the input
firstNumber = number // 100
lastTwo = number % (firstNumber * 100)
secondNumber = lastTwo // 10
thirdNumber = lastTwo % (secondNumber * 10)
reversed = int(str(thirdNumber) + str(secondNumber) + str(firstNumber))
#7 Calculate the difference of the input and its reverse
difference = abs(number - reversed)
#8 Calculate the reverse of the difference
firstDifference = difference // 100
lastTwo = difference % (firstDifference * 100)
secondDifference = lastTwo // 10
thirdDifference = lastTwo % (secondDifference * 10)
reversed_difference = int(str(thirdDifference) + str(secondDifference) + str(firstDifference))
#9 Calculate the sum of the difference and its reverse
sum = reversed_difference + difference
#10Output the results of the calculations
print(reversed)
print(difference)
print(reversed_difference)
print(sum)
