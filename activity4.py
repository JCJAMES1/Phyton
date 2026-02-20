x = 300

def closest(a, b, c):
    if abs(x - a) < abs(x - b) and abs(x - a) <abs(x - c):
        print("A or", a, "is the closest to", x)
    elif abs (x - b) < abs(x - a) and abs (x - b) < abs(x - c):
        print("B or", b, "is the closest to", x)
    else:
        print("C or", c, "is the closest to", x)
        
print("Find the closest number to", x)

    
a = int(input("\nEnter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

closest(a, b, c)
