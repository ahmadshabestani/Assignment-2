counter = 0
avrage = 0
while True:
    student_number = input("Enter your Student Number :")
    if student_number == "exit":
        break
    else:
        avrage += float(student_number)
        counter += 1

print("avrage is :",avrage/counter)
