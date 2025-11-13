import random

entered_number = None
attempts = 0
number=random.randint(1, 100)
while True:
    try:
        entered_number = int(input("Enter a number between 1 and 100 for the guessing game: "))
        if not (1 <= entered_number <= 100):
            print("The number must be between 1 and 100. Please try again.")
        else:
            print(f"You have entered {entered_number}. Let's start the game!")
            attempts += 1
            if entered_number < number:
                print("Too low! Try again.")
            elif entered_number > number:
                print("Too high! Try again.")
            else:
             print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
             break
    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 100.")    