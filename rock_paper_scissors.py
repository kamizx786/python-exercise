import random

ROCK='r'
PAPER='p'
SCISSORS='s'

emojis={
    ROCK: '✊',  # Rock
    PAPER: '✋',  # Paper
    SCISSORS: '✌️'   # Scissors
}
choices=tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
         print("Invalid choice. Please enter 'r', 'p', or 's'.")
    
def display_choice(choice,type):
    if type=='user':
        print(f"You chose: {emojis[choice]}")
    else:
        print(f"Computer chose: {emojis[choice]}")
def determine_winner(user_choice, computer_choice):
       if user_choice == computer_choice:
        print("It's a tie!")
       elif (user_choice == ROCK and computer_choice == SCISSORS) or \
         (user_choice == PAPER and computer_choice == ROCK) or \
         (user_choice == SCISSORS and computer_choice == PAPER):
        print("You win!")
       else:
        print("Computer wins!")
def play_again_prompt():
       while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        return play_again
while True:
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)
    display_choice(user_choice,'user')
    display_choice(computer_choice,'computer')
    determine_winner(user_choice, computer_choice)
    play_again = play_again_prompt()
    if play_again == 'n':
        print("Thanks for playing!")
        break  # exit main loop too
