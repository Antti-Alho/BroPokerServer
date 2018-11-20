import cv2 as cv
from randomHand import generatePokerhands
print(cv.__version__)
from matplotlib import pyplot as plt

img = cv.imread('wizard.jpg',0)

poker_card_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
poker_card_name = {
	1: 'Ace',
	2: 'Two',
	3: 'Three',
	4: 'Four',
	5: 'Five',
	6: 'Six',
	7: 'Seven',
	8: 'Eight',
	9: 'Nine',
	10: 'Ten',
	11: 'Jack',
	12: 'Queen',
	13: 'King',
}

poker_suit_types = [1, 2, 3, 4]
poker_card_suits = {
	1: 'Heart',
	2: 'Spade',
	3: 'Diamond',
	4: 'Club',
}

poker_hand_types = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
hand_name = {
    0: 'Nothing in hand',
    1: 'One pair',
    2: 'Two pairs',
    3: 'Three of a kind',
    4: 'Straight',
    5: 'Flush',
    6: 'Full house',
    7: 'Four of a kind',
    8: 'Straight flush',
    9: 'Royal flush',
}

pokerHands = generatePokerhands(4)
print(pokerHands)
