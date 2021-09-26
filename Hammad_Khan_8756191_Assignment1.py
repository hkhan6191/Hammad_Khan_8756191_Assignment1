print("Welcome, to Abby's Merchandizing! This tool can be used to place an order with us as well as to calculate the total cost of your order. Let's get started!")

num = 0

polo = 1
tshirt = 2

blue = 3
red = 4
green = 5
yellow = 6
orange = 7
white = 8
black = 9

cost = 9.99
hst = 0.13

colorinput = int(input("What color shirt would you like?: "))

if colorinput == blue:
    print("Blue, great choice! ")

elif colorinput == red:
    print("Red, great choice! ")

elif colorinput == green:
    print("Green, great choice! ")

elif colorinput == yellow:
    print("Yellow, great choice! ")

elif colorinput == orange:
    print("Orange, great choice! ")

elif colorinput == white:
    print("White, great choice! ")

elif colorinput == black:
    print("Black, great choice! ")

else:
    print("Oops! The color you want is not in stock  :( ")
    colorinput = int(input("Please select a different shirt color: "))


typeinput = int(input("Next, select the type of shirt would you like?: "))

if typeinput == polo:
    print("Polo. Great choice!")

elif typeinput == tshirt:
    print("T-Shirt. Great choice!")

else:
    print("Looks like we are all out of that type of shirt... ")
    typeinput = int(input("Please select either a Polo or a T-Shirt: "))

numinput = int(input("Lastly, decide how many shirts you would like!: "))

print("Alright, lets recap your order.")

print("Color of shirt: " + str(colorinput))
print("Type of shirt: " + str(typeinput))
print("Number of shirts: " + str(numinput))

print("Your total cost today will be: " + str(cost * numinput))

print("Thank you for choosing Abby's Merchandizing today! We hope you enjoyed your shopping experience with us!  ")