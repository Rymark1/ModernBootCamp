import random


total_wins = 0
while True:
    answer = random.randint(1, 11)
    player_choice = 0
    tries = 0
    while player_choice != answer:
        player_choice = int(input("Please enter your guess: "))
        tries += 1
        if player_choice < answer:
            print("You guessed too low.  Please try again.")
        elif player_choice > answer:
            print("You guessed too high.  Please try again.")
        else:
            print(f"You guessed correctly in {tries} tries.")
            total_wins += 1
    again = input("Would you like to play again? (Y/N): ")
    if str.upper(again) != "Y":
        break

print(f"You guessed correctly {total_wins} times.")
