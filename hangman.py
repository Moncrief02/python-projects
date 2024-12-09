import random
from word import words
import string

def get_valid_words(words):
    word=random.choice(words)
    while '_'in word or '' in word:
        word=random.choice(words)
    
    return word


def hangman():
    word= get_valid_words(words)
    words_letters= set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #what user guessed
    
    lives= 6
    while len(words_letters)>0 or lives > 0:
        #letters used
        print('you have ' + lives + ' left and you have used these letters: ', ' '.join(used_letters))

        word_list= [letter if letter in used_letters else  '_' for letter in word]
        print('current word: ',''.join(word_list))

        user_letter= input('Guess a letter')
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in words_letters:
                words_letters.remove(user_letter)
            
            else:
                lives=lives-1
                print('Letter not in word')

        elif user_letter in used_letters:
            print('you have already used that character.Please try again')
        
        else:
            print('Invalid characters')
    if lives ==0:
        print('sorry you lose')
    else:
        print("Congratulations!!!")

user_input=input('type something')
print(user_input)
hangman()