import random



print("~~~~~~~~~~Welcome to Rock Paper Scissor Game~~~~~~~~~")


user_score= 0
comp_score= 0
ties= 0

name= input("Enter your name here:")

print("""
winning rules:
1.paper vs Rock-->
2.Rock vs Scissors--> Rock
3.Scissors vs paper-->Scissors""")
print()

game_active=True

while game_active:
    print("""choices are:
    1.Rock 
    2.Paper
    3.Scissor""")

    choice=int(input("Enter your choice from 1-3:"))
    print()
    while not (1 <= choice <= 3):
        choice = int(input("Enter valid input: "))

    if choice==1:
        user_choice = "Rock"
    elif choice==2:
        user_choice = "Paper"
    else:
        user_choice ="Scissors"

    print("Your user's choice is",user_choice)
    print("Now computer's turn")

    computer=random.randint(1,3)

    if computer == 1:
        comp_choice="Rock"
    elif computer == 2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"


    print("The computer choice is",comp_choice)

    if((user_choice == "Paper" and comp_choice== "Rock")or (user_choice == "Rock" and comp_choice == "Paper" )):
           print("paper wins")
           result="Paper"
    elif ((user_choice == "Scissors" and comp_choice== "Rock")or (user_choice == "Rock" and comp_choice == "Scissors" )):
          print("rock wins")
          result="Rock"
    elif (user_choice==comp_choice):
            print("it's a tie")
            result= "Tie"
    else:
          print("Scissors win")
          result="Scissors"

    if  result == "Tie":
        ties+=1
    elif result == user_choice:
        print("users win")
        user_score +=1
    else:
        print("computer win")
        comp_score +=1

    print("scores are")
    print(name," 's score is",user_score)
    print("computer's score is",comp_score)
    print("ties are",ties)

    repeat=input("Do you want to play again? Enter 'Yes' or 'No'")
    if repeat.lower() != "yes":
        game_active= False

print("Game over")
print("Thanks for playing")