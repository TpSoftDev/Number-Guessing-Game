# Number Guessing Game

## Overview
This Python script implements a simple number guessing game where the user tries to guess a randomly generated number within a specified range. The program provides feedback to the user after each guess, indicating whether the guess is too high or too low, until the correct number is guessed. Upon successful guessing, the program congratulates the user and reveals the correct number.

## How to Play
1. Run the Python script `guess_number.py`.
2. Enter the upper limit of the range for generating the random number.
3. Start guessing numbers within the range until you guess the correct number.
4. Receive feedback on whether your guess is too high or too low after each attempt.
5. Once you guess the correct number, the program will congratulate you and display the correct number.

## Programming Techniques
- **Random Number Generation**: The script uses the `random.randint()` function to generate a random number within the specified range.
- **User Input**: It utilizes the `input()` function to receive user guesses as input.
- **Looping**: A `while` loop is employed to repeatedly prompt the user for guesses until the correct number is guessed.
- **Conditional Statements**: `if-elif-else` statements are used to provide feedback to the user based on the comparison between the guessed number and the random number.
- **Function Definition**: The functionality of the game is encapsulated within a function `guess_number()` for modularity and reusability.
- **Documentation**: The script includes comments to explain the purpose of each section of code and adheres to Python docstring standards for documenting the function.

## Example
```
Guess a number between 1 and 10: 5
Your guess is too low. Try again!
Guess a number between 1 and 10: 8
Your guess is too high. Try again!
Guess a number between 1 and 10: 7
Your guess is too high. Try again!
Guess a number between 1 and 10: 6
Congratulations! You have guessed the number 6 correctly.
```
