import random

def guess_number(max_number):
    """
    Guess the randomly generated number within a given range.

    Args:
        max_number (int): The upper limit of the range for generating a random number.

    Returns:
        None
    """
    # Generate a random number within the given range
    random_number = random.randint(1, max_number)
    guess = 0  # Initialize guess to 0
    
    # Continue looping until the guess matches the random number
    while guess != random_number:
        # Ask user to input their guess
        guess = int(input(f'Guess a number between 1 and {max_number}: '))
        
        # Check if the guess is higher or lower than the random number
        if guess > random_number:
            print("Your guess is too high. Try again!")
        elif guess < random_number:
            print("Your guess is too low. Try again!")

    # Once the correct number is guessed, print a congratulatory message
    print(f"Congratulations! You have guessed the number {random_number} correctly.")

# Test the function with a maximum number of 10
guess_number(10)
