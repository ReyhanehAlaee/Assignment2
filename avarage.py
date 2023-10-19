name = input("Enter first name: ")
family = input("Enter last name: ")
a = int(input(" Enter first score: "))
b = int(input("Enter second score: "))
c = int(input("Enter third score: "))

average = (a + b + c)/3

if average >=17:
    print("great")
if average <17 and average >=12:
    print("normal")
if average <12:
    print("fail")