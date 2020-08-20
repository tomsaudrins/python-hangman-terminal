# python-hangman-terminal
Terminal based hangman game with an option to add unlimit words to the word_list.py

  - Customise amount of guesses the user has.
  - Easy mode on / off, on = display first / last letter and every occurance of it throughout the word).
  - Validate the input (if incorrect, ask again, don't reduce guesses for invalid input).
  - Display amount of guesses left until end of the game.
  - Display already guessed letters.
  - Start over feature.

### Installation

Requires [Python 3.8](https://www.python.org/).

Install the dependencies and run the application.

```
# cd python-hangman-terminal
# python3 main.py
```

### Dependencies

| Dependency | Website |
| ------ | ------ |
| random | Generate a random selection from the word list |
| os | Get the name of the system to support both windows and unix systems for the clear screen function |


