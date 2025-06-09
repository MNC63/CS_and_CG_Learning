from random import randint

print("Wellcome to Rock, Paper, Scissors!")
print("Choose your move: rock, paper, or scissors")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "rock"
elif computer == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"You chose: {player}")
print(f"Computer chose: {computer}")

if player == computer:
    print("DRAW!")
else:
    if player == "rock":
        if computer == "paper":
            print("You Lose!")
        else:
            print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("You Lose!")
        else:
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("You Lose!")
        else:
            print("You Win!")
    else:
        print("Wrong input! Please choose rock, paper, or scissors.")