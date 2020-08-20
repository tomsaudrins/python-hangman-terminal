from word_list import word_list
from random import choice
from utils import cls


class Hangman:
    def __init__(self, guess=5, easy_mode=False):
        self.word = choice(word_list).lower()
        self.guess = guess
        self.guessed = set()
        self.word_display = ["_"] * len(self.word)
        if easy_mode:
            self.replace_letters([self.word[0], self.word[-1]])
        print(f"Word to guess: {self.display_name()}")
        self.start_game()

    def replace_letters(self, user_input):
        for index, letter in enumerate(self.word):
            if letter in user_input:
                self.word_display[index] = letter

    def validate_input(self, user_input):
        if len(user_input) != 1 or not user_input.isalpha() or user_input in self.guessed:
            self.ask_for_input()
        elif user_input in self.word:
            self.replace_letters(user_input)
        else:
            self.guess -= 1
            self.guessed.add(user_input)

    def guesses(self):
        return ", ".join([*self.guessed])

    def ask_for_input(self):
        cls()
        print(self.display_name())
        print(f"Guesses left: {self.guess}")
        print(
            f"Your previous incorrect guesses: {self.guesses() if len(self.guessed) != 0 else ''}")
        user_input = input("Please choose a letter: ").lower()
        self.validate_input(user_input)
        cls()
        print(self.display_name())

    def display_name(self):
        return " ".join(self.word_display).capitalize()

    def game_over(self):
        cls()
        print(
            f"Game over, you lost! \n The word was: {self.word} \n You got: {self.display_name()}")

    def start_game(self):
        while "_" in self.word_display:
            self.ask_for_input()
            if self.guess == 0:
                self.game_over()
                return
        print(f"Game over, you won! The word was {self.word}")

    def start_over(self):
        self.__init__()
