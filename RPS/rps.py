import random

# cpu_choice is what the cpu throws.  0 is rock, 1 is paper, 2 is scissors

while True:
    cpu_choice = random.randint(0, 2)
    answer = ["rock", "paper", "scissors"]
    player_choice = input("Choose Rock, Paper, or Scissors (R/P/S): ")
    player_choice = str.upper(player_choice)
    if player_choice == "R":
        player_choice = 0
    elif player_choice == "P":
        player_choice = 1
    elif player_choice == "S":
        player_choice = 2
    else:
        print("You didn't throw rock, paper or scissors")
        player_choice = -1

    if player_choice == -1:
        pass
    else:
        if cpu_choice == player_choice:
            print(f"You tied! and both threw {answer[cpu_choice]}")
        elif (cpu_choice == 0 and player_choice == 1) or (cpu_choice == 1 and player_choice == 2) or (cpu_choice == 2 and player_choice == 0):
            print(f"You win! The cpu threw {answer[cpu_choice]} and you threw {answer[player_choice]}")
        else:
            print(f"You lose. The cpu threw {answer[cpu_choice]} and you threw {answer[player_choice]}")
    again = input("Would you like to play again? (Y/N): ")
    if str.upper(again) != "Y":
        break
