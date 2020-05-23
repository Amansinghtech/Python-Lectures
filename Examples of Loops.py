nth = int(input("Enter nth term: "))

n1 = 0
n2 = 1

count = 0

while count < nth:
    print(n1)
    n3 = n1 + n2

    n1 = n2
    n2 = n3

    count += 1
