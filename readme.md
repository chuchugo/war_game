# Rules
https://bicyclecards.com/how-to-play/war/
no kings involved.
when in pairs, if one player has not enough card, that player lose.


# Instruction about how to use the api
## start_game:
it will start a new round of game. and it will return these info:
    start cards of each player
    what they had for each hand, and the result of each hand
    final result of the winner and loser of this round

## Summary of the game history
    lifetime wins for each player

# DB structure
what is stored in db?
The rounds info:
    the id of the round
    the start cards of each player for each round
    each round result

what is not?
The cards of each hand of each player and the result of each hand

# Tests 


