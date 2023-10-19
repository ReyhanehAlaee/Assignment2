a = int(input("Enter First Side: "))
b = int(input("Enter Second Side: "))
c = int(input("Enter Third Side: "))

if a+b>c and b+c>a and a+c>b: 
    print("yes")
else: 
    print("no")