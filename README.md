# Flask Number Guessing Game

## Overview

This is a simple web-based number guessing game built with Flask, a lightweight web framework for Python. The game generates a random number between 0 and 9, and the user is prompted to guess the number by entering their guess in the URL. Depending on the guess, the application provides feedback on whether the guess was too high, too low, or correct.

## How It Works

1. **Random Number Generation:**  
   At the start, a random number between 0 and 9 is generated using Python's `random.randint(0, 9)` function. This number is stored and remains the same until the Flask server is restarted.

2. **Game Interface:**  
   - When the user visits the homepage (`/`), they see a message prompting them to guess a number between 0 and 9.
   - The user makes a guess by appending the number to the URL (e.g., `/5` to guess the number 5).
   - Based on the guess, the application responds with one of the following:
     - If the guess is too high, a message is displayed with an animated GIF.
     - If the guess is too low, a different message is shown with another GIF.
     - If the guess is correct, a congratulatory message appears along with a celebratory GIF.

## Routes

- **`/`**  
  Displays the homepage with the prompt to guess a number between 0 and 9.

- **`/<int:guess>`**  
  Displays feedback based on the user's guess:
  - If the guess is too high, a message saying "Too high, try again!" is shown.
  - If the guess is too low, a message saying "Too low, try again!" is shown.
  - If the guess is correct, a message saying "You found it!" is displayed.

## Getting Started

### Prerequisites

- Python 3.x
- Flask


