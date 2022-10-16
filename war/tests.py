import datetime

from django.test import TestCase
from django.utils import timezone
from .views import initialize_game, war, map_value_to_card,compareTwo
 

class WinFuncTests(TestCase):
    def test_make_value_to_card(self):
        self.assertEquals(map_value_to_card(0), 'Spade 2')
        self.assertEquals(map_value_to_card(13), 'Heart 2')
        self.assertEquals(map_value_to_card(51), 'Club A')

    def test_compareTwo(self):
        player1 = [ 2,3]
        player2 = [ 1,2]
        stack = [0,0]
        self.assertEquals(compareTwo(player1, player2, stack), 'continue game')
        player1 = [ 1, 2]
        player2 = [ 14, 15]
        stack = [0,13]
        self.assertEquals(compareTwo(player1, player2, stack), 'tie')
        player1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        player2 = [ 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        stack = [0,13]
        self.assertEquals(compareTwo(player1, player2, stack), 'tie')

    def test_war(self):
            player1 = [ 1, 2, 3, 4, 5, 5, 7, 8, 9, 10, 11, 11]
            player2 = [ 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
            self.assertEquals(war(player1, player2), 'player2')      
            player1 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            player2 = [ 13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
            self.assertEquals(war(player1, player2), 'tie') 
            player1 = [  10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            player2 = [   14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
            self.assertEquals(war(player1, player2), 'player1') 

            # 0 10 14           2 3   4  5   6  7   8  9  10 11  12 0 
            # 13               15 16  17 18  19 20  21 22 23 24  25 13