# Rules
https://bicyclecards.com/how-to-play/war/
no kings involved.
when in pairs, if one player has not enough card, that player lose.


# Instruction about how to use the api
image.png

## start_game:
visit: localhost:8000/start
this page will return a JSON response

after visiting the page, it will start a new round of game and return these info of the new game:

   - "initial_status": start cards of each player
   - "hands": what they had for each hand, and the result of each hand
   - "final_result":final result of the winner and loser of this round

    {"initial_status": 
    {"player1": ["Heart J", "Spade 6",...], "player2": ["Club Q", "Heart 5", ...]},"hands": 
    {"1": 
    {"player1": "Heart J", "player2": "Club Q"}, "2": 
    {"player1": "Spade 6", "player2": "Heart 5"}, "3":
     {"player1": "Club 9", "player2": "Diamond J"}, 
     .....},
    "final_result": "player1"}

## Summary of the game history
visit: localhost:8000/history
    this page will return a UI web page
    lifetime wins for each player
    image.png

# DB structure
## what is stored in db?
The rounds info:
    the id of the round
    the start cards of each player for each round
    each round result
    the timestamp

## what is not stored in db?
The cards of each hand of each player and the result of each hand




