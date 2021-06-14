# Wap to find area of cirle or rectangle or triangle as per user's choice

import math
choice=input("whose area you wanna find  (circle or rectangle or triangle)")

if choice == "circle":
    rad = float(input("enter the radius of the circle"))
    print(3.14 * rad ** 2)

elif choice == "rectangle":
    length = float(input("Enter the length of the rectangle"))
    breadth = float(input("Enter the breadth of the rectangle"))
    print(length * breadth)

elif choice == "triangle":
    a = float(input("Enter the first side of the triangle"))
    b = float(input("Enter the second side of the triangle"))
    c = float(input("Enter the third side of the triangle"))

    s = (a + b + c)/2
    area = s * (s-a)*(s-b)*(s-c)
    print( math.sqrt(area))

else :
    print("Entered choice is wrong")

