# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 

# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

test = int(input("Give me a number: "))

if test % 4 == 0:
    print(f"{test} is divisible by 4.")
elif test % 2 == 0:
    print(f"{test} is divisible by 2.")
else:
    print(f"{test} is not divisible by 2 or 4.")

num = int(input("What number would you like to check? "))
check = int(input("What number will you use to check? "))

if num % check == 0:
    print(f"{num} is divisible by {check}.")
else:
    print(f"{num} is not divisible by {check}.")