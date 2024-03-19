import random

user_score = 0
computer_score = 0
mosavi = 0
# computer_choice = random.choice(["1","2",3])
# print(computer_choice)
counter = int(input("chand bar dost dari bazi koni ? : "))
for i in range(counter):
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computer_choice = "rock"
    elif randomNumber == 2:
        computer_choice = "paper"
    elif randomNumber == 3:
        computer_choice = "scissors"
    user_choice = input("Enter rock or  paper or scissors : ")

    if computer_choice == "rock" and user_choice == "rock":
        mosavi += 1
    elif computer_choice == "rock" and user_choice == "paper":
        user_score += 1
    elif computer_choice == "rock" and user_choice == "scissors":
        computer_choice += 1

    if computer_choice == "paper" and user_choice == "paper":
        mosavi += 1
    elif computer_choice == "paper" and user_choice == "rock":
        computer_score += 1
    elif computer_choice == "paper" and user_choice == "scissors":
        user_score += 1

    if computer_choice == "scissors" and user_choice == "scissors":
        mosavi += 1
    elif computer_choice == "scissors" and user_choice == "paper":
        computer_score += 1
    elif computer_choice == "scissors" and user_choice == "rock":
        user_score += 1
    print(user_choice)
    print(computer_choice)
    print("emtiyaz user : ",user_score)
    print("emtiyaz computer : ",computer_score)

if user_score > computer_score:
    print("user win")
elif computer_score > user_score:
    print("computer win")
else:
    print("mosavi")
