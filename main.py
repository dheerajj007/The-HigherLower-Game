import random as rd
import os
from art import logo
from art import vs

#function to generate a random choice from data list
def selectItem():
    from gameData import data
    item = rd.choice(data)
    return item

#function to play the game
def playGame():
    score = 0
    isGameOver = False
    scoreMessage = ""
    A = selectItem()
    while not isGameOver:
        os.system('cls')
        print(logo)
        if score != 0:
            print(f"You're right! Current Score: {score}")
        
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        
        print(vs)
        B = selectItem()
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a' and A['follower_count'] > B['follower_count']:
            score += 1 
        elif choice == 'b' and B['follower_count'] > A['follower_count']:
            score += 1
            A = B
            
        else:
            isGameOver = True
            os.system('cls')
            print(f"Sorry, that's wrong. Final score: {score}")
    
playGame()