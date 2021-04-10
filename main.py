import random as rd

from art import logo
print(logo)

#function to generate a random choice from data list
def selectItem():
    from gameData import data
    item = rd.choice(data)
    return item

#function to play the game
def playGame():
    score = 0
    isGameOver = False
    A = selectItem()
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    B = selectItem()
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    
    choice = input("Who has more followers? Type 'A' or 'B'").lower()
    if choice == 'a' and A['follower_count'] > B['follower_count']:
        score += 1 
    elif choice == 'b' and B['follower_count'] > A['follower_count']:
        score += 1
    else:
        isGameOver = True
        print("You lose")
    
    
playGame()