# Script to print a triangle
h = int(input("Enter the height: "))
w = (2 * h) - 2
for i in range(h):
    for j in range(w):
        print(end = " ")
    w = w - 1
    for j in range(i + 1):
        print("*", end=' ')
    print(" ")
