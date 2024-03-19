import random
number = 0
computer_number = random.randint(10,40)
for i in range(10):
    user_number = int(input("Enter your Number :"))
    if computer_number == user_number:
        print("you win")
        print("hads : ",number)
        break
    elif computer_number > user_number:
        print("bro bala")
        number +=1
    elif user_number > computer_number:
        print("biya paiin")
        number += 1