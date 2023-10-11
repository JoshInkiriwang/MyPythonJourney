# scaling-happiness : CLI Guessing Game - Python

This is a simple command-line guessing game implemented in Python. The game includes two modes: guessing a number and guessing a word. Players have a limited number of attempts to guess the correct answer and earn points based on their performance.

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Prerequisites

- Python 3 SDK
- Python extension for Visual Studio Code (optional, but recommended)

## How to Play

1. Clone this repository to your local machine or download the source code.

```bash
git clone [https://github.com/JoshInkiriwang/happy-guessGame.git]
```

2. Navigate to the project directory.

```bash
cd happy-guessGame
```

3. Run the game by executing the `guessGame.py` file.

```bash
python guessGame.py
```

4. Follow the on-screen instructions to play the game. You will have 5 attempts to guess the correct number or word.

## Features

- Guessing a Number: You need to guess a number between 1 and 20.
- Guessing a Word: You need to guess a secret word about colours chosen by the program (pre-set color name list).
- Computer Guessing a Number : Computer randomly guess a number between 1 and 20, and player will give some hints
- Point System: You earn points based on your performance - more points for fewer attempts (future development).
- Input/Output: The game provides clear instructions and communicates the results effectively.
- Repetition: The game loop allows you to play multiple rounds without restarting the program.
- Conditional Statements: The program uses conditionals to check if your guess is correct.
- Read/Write from Text Files: Username is stored in a text file ; High scores are stored in a text file (`high_scores.txt`) and updated as needed.

## File Structure

- `guessGame.py`: The main game script containing the game logic.
- `myfile.txt`: Text file to store and read username and high scores (future development) .

## Contribution

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License

This project is created by JoshInkiriwang or Joshua Verbiano Inkiriwang and licensed under the [MIT License](LICENSE).

---

Have fun playing the CLI Guessing Game! If you have any questions or need assistance, please don't hesitate to ask.
```
