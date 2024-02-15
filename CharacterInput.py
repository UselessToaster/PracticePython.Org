# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year 
# (and therefore be out of date the next year).

# 1. Add on to the previous program by asking the user for another number 
#    and printing out that many copies of the previous message. 
#    Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines. 
#    (Hint: the string "\n is the same as pressing the ENTER button)

name = input("What is your name?")
age = int(input("What is your age?"))

century = 2124 - age

message = f"Ok {name} You will be 100 in the year {century}. "

print(message)

num = int(input("Give me a number "))

print(message * num)

# an alternative to the while statemet is 
# print((message + "\n") * 5)

i = 0
while num > i:
    print(message)
    i += 1


#note, I came up with the while solution before the * solution