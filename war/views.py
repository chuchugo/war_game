from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def get_home(request):
    return render(request, "home.html")

def start_game(request):
    cards1, cards2 = initialize_game()
    result = war(cards1, cards2)
    # return all the hands 
    
    #save the game result in db

    #'game_process', 'winner'
    dictionary = {'cards1':cards1, 'cards2':cards2,'winner':result}
    print(dictionary)
    return JsonResponse(dictionary)


def review_game(request):
    return render(request, "history.html")


from ast import main
from operator import truediv
import random


def initialize_game():
    #initialize the cards for each player
    list = []
    for i in range(0, 52):
        list.append(i)
    random.shuffle(list)
    player1 = list[0:26]
    player2 = list[26:52]
    return player1, player2

def war(player1,player2):
    #start to play the game
    # end the game when one of the player has no card

    # compare first card of each player
    # if player1 wins, add both cards to player1's deck
    # if player2 wins, add both cards to player2's deck

    # if tie, take two extra cards from each side, compare the next card of each player
    # if player1 wins, add all 6 cards to player1's deck
    # if player2 wins, add all 6 cards to player2's deck

    # keep record of the game process with hands{}
    hand_num = 0

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
            compareTwo(player1, player2, stack)

    if  len(player1) == len(player2) == 0:
        return 'tie'
    elif len(player2) == 0:
        print(player1)
        return 'player1'
    elif  len(player1) == 0:
        print(player2)
        return 'player2'
#when there is a tie,  prepare two cards for each player,and compare the next card of each player
# here is possible continuous loop when there are always ties
def compareTwo(player1, player2,stack):
    # here we need to take care of coner cases when one of the player has less than 2 cards
    if len(player1) < 2 and len(player2) < 2:
        if len(player1) > len(player2):
            return 'player1'
        elif len(player1) < len(player2):
            return 'player2'
        else:
            return 'tie'
    elif len(player1)<2:
        return 'player2'
    elif len(player2)<2:
        return 'player1'
    if len(player1) < 2 or len(player2) < 2:
        return
    
    #record hand
    

    tie = True
    if player1[1] % 13 > player2[1] % 13:
        tie = False
        #for each war, it will require to add two cards to the stack for each side
        player1.append(player1[0])
        player1.append(player2[0])
        player1.append(player1[1])
        player1.append(player2[1])
    elif player1[1] % 13 < player2[1] % 13:
        tie = False
        player2.append(player2[0])
        player2.append(player1[0])
        player2.append(player2[1])
        player2.append(player1[1])
    else: #if there is still a tie, prepare two more cards for each player
        stack.append(player1[0])
        stack.append(player2[0])
        stack.append(player1[1])
        stack.append(player2[1])

    player1.remove(player1[0])
    player1.remove(player1[0])
    player2.remove(player2[0])
    player2.remove(player2[0])

    if not tie:
        return 'continue game'
    else:
        #keep comparing until there is a winner
        return compareTwo( player1, player2, stack)

#map all 52 values to cards
def map_value_to_card(value):
    num = value % 13
    suit = value//13
    maptoSuit = {0: 'Spade', 1: 'Heart', 2: 'Diamond', 3: 'Club'}
    maptoCardNum = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', 7: '9', 8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}
    return maptoSuit[suit] +' ' + maptoCardNum[num]

# this is to record the game process, 
# for each hand, record the cards of each player
def record_hand(hands, hand_num,player1_num, player2_num):
    player1_card = map_value_to_card(player1_num)
    player2_card = map_value_to_card(player2_num)
    hands[hand_num] = {'player1': player1_card, 'player2': player2_card}

    
    