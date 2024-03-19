b = 0
a = 1
number = int(input("Enter your Number : "))

for i in range(number):
    if number ==1:
        print(number)
        break
    else:
        c = a + b
        a = b
        b = c
    print(b)
