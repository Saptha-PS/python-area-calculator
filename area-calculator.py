# Finding areas of different shapes
print("Hello friend,Today we are here to calculate 'AREAS'.You can see four options below , choose anyone.")
print("lets begin")
print("")
print("Select from below")
print("Press 1 for finding area of square.")
print("Press 2 for finding area of rectangle.")
print("Press 3 for finding area of triangle.")
print("Press 4 for finding area of circle.")
while True:

 print("")
 operation=int(input("Enter your choice:"))
 print("")
 if operation==1:
     l1=float(input("Enter the lenght of the square:"))
     A1=l1*l1
     print("Area of the square is",A1)
 elif operation==2:
     l2=float(input("Enter the length of the rectangle:"))
     b2=float(input("Enter the breadth of the rectangle:"))
     A2=l2*b2
     print("The area of the rectangle is",A2)
 elif operation==3:
    b3=float(input("Enter the base length of the triangle:"))
    h=float(input("Enter the height of the triangle:"))
    A3=(b3*h)/2
    print("The area of the triangle is",A3)
 elif operation==4:
    r=float(input("Enter the radius of the circle:"))
    pi=3.14
    if r!=0:
      A4=pi*r**2
      print("The area of the circle is",A4)
    else:
      print("The circle with a radius ZERO is called DOT!!!")
 else:
    print("INVALID OPERATION")
 print("")
 again=input("Do you want to calculate another area? (yes/no):")
 if again.lower()!="yes":
    print("Thank you for using the area calculator!")
    break
