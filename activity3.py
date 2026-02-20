def find_largest(a, b, c):
    if a >= b and a>= c:
        return "A", a
    elif b >= a and b>= c:
        return "B", b
    else:
        return "C", c
            
a = int(input("Enter  your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

letter,value = find_largest(a, b, c)

    
print(f"Letter {letter} is the largest number with a Value of {value}")
