from ast import main
from operator import truediv
import random


def war():
    #initialize the cards for each player
    list = []
    for i in range(0, 52):
        list.append(i)
    random.shuffle(list)
    player1 = list[0:26]
    player2 = list[26:52]
    print("Player 1: ", player1)
    print("Player 2: ", player2)
    
    #start to play the game
    # end the game when one of the player has no card

    # compare first card of each player
    # if player1 wins, add both cards to player1's deck
    # if player2 wins, add both cards to player2's deck

    # if tie, take two extra cards from each side, compare the next card of each player
    # if player1 wins, add all 6 cards to player1's deck
    # if player2 wins, add all 6 cards to player2's deck

    while len(player1) > 0 and len(player2) > 0:
        if player1[0] % 13 > player2[0] % 13:
            
            player1.append(player1[0])
            player1.append(player2[0])
            player1.remove(player1[0])
            player2.remove(player2[0])
            
        elif player1[0] % 13 < player2[0] % 13:
            player2.append(player2[0])
            player2.append(player1[0])
            player2.remove(player2[0])
            player1.remove(player1[0])
        else:
            stack = [] # stack is used to store the cards that are in the war
            stack.append(player1[0])
            stack.append(player2[0])
            player1.remove(player1[0])
            player2.remove(player2[0])
            result = compareTwo(player1, player2, stack)
            if result == 'player1':
                return 'player1'
            elif result == 'player2':
                return 'player2'
            elif result == 'tie':
                return 'tie'
            # if result is null then the game still goes on
    

    if len(player1) == 0:
        print(player2)
        return 'player1'
    elif len(player2) == 0:
        print(player1)
        return 'player2'
           

#when there is a tie,  prepare two cards for each player,and compare the next card of each player
# here is possible continuous loop when there are always ties
def compareTwo(player1, player2,stack):
    # here we need to take care of coner cases when one of the player has less than 2 cards
    if len(player1) < 2 and len(player2) < 2:
        return 'tie'
    elif len(player1)<2:
        return 'player2'
    elif len(player2)<2:
        return 'player1'
    
    tie = False
    if player1[1] % 13 > player2[1] % 13:
        #for each war, it will require to add two cards to the stack for each side
        player1.append(player1[0])
        player1.append(player2[0])
        player1.append(player1[1])
        player1.append(player2[1])
    elif player1[1] % 13 < player2[1] % 13:
        player2.append(player2[0])
        player2.append(player1[0])
        player2.append(player2[1])
        player2.append(player1[1])
    else: #if there is still a tie, prepare two more cards for each player
        tie = True
        stack.append(player1[0])
        stack.append(player2[0])
        stack.append(player1[1])
        stack.append(player2[1])

    player1.remove(player1[0])
    player1.remove(player1[0])
    player2.remove(player2[0])
    player2.remove(player2[0])

    if tie:
        #keep comparing until there is a winner
        compareTwo(player1, player2, stack)
    
   
#main
if __name__ == '__main__':
    result = war()
    print(result)