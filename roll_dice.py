import random

def roll_dice():
    """Simulate rolling two six-sided dice and return their values as a tuple."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)

# Ask how many times to roll
games_to_play = 0
while games_to_play <= 0:
    try:
        games_to_play = int(input("How many times do you want to roll the dice? "))
        if games_to_play <= 0:
            print("Please enter a positive number.")
    except ValueError:
        print("You must enter a number.")

total_played_games = 0

# Game loop
while total_played_games < games_to_play:
    choice = input("Do you want to roll the dice? (y/n): ").strip().lower()
    
    if choice == "y":
        die1, die2 = roll_dice()
        total_played_games += 1
        print(f"You rolled a {die1} and a {die2}. Total: {die1 + die2}")
        print(f"Game {total_played_games}/{games_to_play}\n")
        
        if total_played_games == games_to_play:
            print("You’ve reached your game limit. Thanks for playing!")
            break
    elif choice == "n":
        print(f"You played {total_played_games} out of {games_to_play} games. Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
