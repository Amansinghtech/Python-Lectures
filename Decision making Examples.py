a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

if a > b:
    
    if a > c:
        print("%d is the largest number "%a)
    else:
        print("%d is the largest number "%c)

else:

    if b > c:
        print("%d is the largest number "%b)
    else:
        print("%d is the largest number "%c)