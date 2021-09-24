print("Welcome, to Abby's Merchandizing! This tool can be used to place an order with us as well as to calculate the total cost of your order. Let's get started!")

polo = 1
tshirt = 2

blue = 3
red = 4
green = 5
yellow = 6
orange = 7
white = 8
black = 9

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
    print("Oops! The color you want is not in stock :( ")
    colorinput = int(input("Please select a different shirt color.: "))

typeinput = int(input("What type of shirt would you like?:  "))
