import ChemTest
import Game2048
import Hangman
import MathQuiz
import TicTacToe
import os 


def get_choice():
    choice = input("Your choice: ")
    breakline()
    return choice


def breakline():
    print('-' * 70)


def clrscr():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def take_input(List, *args):
    """
    A function to let the user choose some thing from a list, and give a list of functions to for that specific command.
    Each Element of args, is a list, containing the function, and it's arguments.
    """
    assert len(args) == len(List)
    breakline()
    for i, elem in enumerate(List):
        print(f'{i + 1}: {elem}')
    breakline()

    choice = get_choice()
    assert choice.isdigit() and int(choice) in range(1, len(List) + 1)

    choice = int(choice) - 1
    args[choice]()
    return True


def main():
    clrscr()
    breakline()
    print('WELCOME TO THE PYTHON GAME COLLECTION!')
    breakline()
    print('Which Game Do You Wanna Play?')
    take_input(['A Chemistry Guessing game', 'TicTacToe', '2048', 'Hangman', 'A Math Quiz'], ChemTest.main, TicTacToe.main, Game2048.main, Hangman.main, MathQuiz.main)


if __name__ == '__main__':
    main()