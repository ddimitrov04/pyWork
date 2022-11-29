print("What is your figure: square, rectangle, triangle")
figureName = input()
face = 0
if figureName == "square" :
    print("Enter side `a`")
    a = int(input())
    face = a*a
    print(face)
elif figureName == "rectangle":
    print("Enter side `a`")
    a = int(input())
    print("Enter side `b`")
    b = int(input())
    face = a*b
    print(face)     
elif figureName == "triangle":
    print("Enter side `a`")
    a = int(input())
    print("Enter side `b`")
    b = int(input())
    face = (a*b)/2
else:
    print("Info not valid")    
    
