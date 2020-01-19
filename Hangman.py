import pickle 
import sys 
import subprocess as sp 
from random import randint 
import time
import os

def breakline():
    print('*'*75)

def clrscr():
    if os.name == 'posix': #Posix stands for Linux.
        sp.call('clear', shell=True) 
    else:
        sp.call('cls', shell=True) 

def get_indices(List, element):
    return [x for x,y in enumerate(List) if y == element]

def get_word(List):
    x = randint(0, len(List))
    return List[x]

def main():
    #Loading all the files we saved using savePickle.py 
    BoW = pickle.load(open('words.pkl', 'rb'))
    HANGMAN = pickle.load(open('hangman.pkl', 'rb'))

    V = list('AEIOU')

    #get a word. 
    word = get_word(BoW).upper()
    #print(word)
    wordL = [x.upper() if x.upper() in V else '_' for x in word]

    i = 0
    Entered = []
    slow = False 

    while i < len(HANGMAN):

        if ''.join(wordL) == word:
            print(f"CONGRATS! YOU WON! YOUR SCORE IS {len(HANGMAN)-i}!")
            sys.exit()
        
        breakline()
        print('HANGMAN!')
        breakline()
        print(f'Tries left: {len(HANGMAN)-i}')
        breakline()

        print(HANGMAN[i])
        print(*wordL, sep='')

        l = input("Guess a Letter: ").upper()
        if len(l) != 1:
            slow = True 
            print('I said, A LETTER! A letter is of length 1!')
        else:
            if l in V:
                print('WHY DID YOU ENTER A VOWEL? AREN\'T VOWELS ALREADY LISTED!')
                slow = True 
            else:
                if l in Entered:
                    print('You entered that letter already!')
                    slow = True 
                else:
                    Entered.append(l)
                    if l in word:
                        X = get_indices(word, l)
                        print(X)
                        print(wordL)
                        for j in X:
                            wordL[j] = l 
                    else:
                        i += 1 
                        slow = False
        
        if slow:
            time.sleep(2)
        clrscr()

    print(f'Sorry buddy, you lost :( Don\'t Worry, Happens to everybody, the word was: {word}')
    print('\n\n\n')

if __name__ == "__main__":
    clrscr()
    main()
    input('Press Enter To Exit.')
    clrscr()
    
