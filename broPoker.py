import cv2 as cv
import random
from randomHand import generatePokerHands
from matplotlib import pyplot as plt

player_count = 4
poker_card_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_name = {
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
suits_name = {
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

def pair(hand):
	values = []
	for card in hand:
		values.append(card[0])
	values.sort()
	x = 0
	for i in values:
		if x == i:
			return True
		x = i	
	return False

def twoPairs(hand):
	values = set()
	for card in hand:
		values.add(card[0])
	if len(values) == 3 and False == threeOfKind(hand):
		return True
	return False

def threeOfKind(hand):
	values = []
	for card in hand:
		values.append(card[0])
	values.sort()
	x,y = 0,0
	for i in values:
		if x == i and y == i:
			return True
		y = x
		x = i
	return False

def straight(hand):
	values = []
	for card in hand:
		values.append(card[0])
	values.sort()
	values.append(0)
	for i in values:
		if i == list[i+1]+1:
			continue
		else:
			return False
	return True

def flush(hand):
	suits = set([])
	for card in hand:
		suits.add(card[1])
	if len(set) == 1:
		return True
	return False

def fullHouse(hand):
	return True

def fourOfKind(hand):
	return True

def straightFlush(hand):
	return True

def royalFlush(hand):
	return True

def scoreFrontHand(hand):
	return 0

def scoreMiddleHand(hand):
	return 0

def scoreBackHand(hand):
	return 2*scoreMiddleHand(hand)

def scoop(fullHand):
	if scoreFrontHand(fullHand[0]) > scoreMiddleHand(fullHand[1]) or scoreFrontHand(fullHand[0]) > scoreBackHand(fullHand[2]) or scoreMiddleHand(fullHand[1]) > scoreBackHand(fullHand[2]):
		return True
	return False

def countScore(fullHand):
	if (scoop(fullHand)):
		return -2*player_count
	return 0

def generatePokerHands(playerCount):
	deck = []
	for i in range(4):
		for j in range(13):
			card = [j,i+1]
			deck.append(card)
	random.shuffle(deck)
	hands = []
	for x in range (playerCount):
		first_hand, second_hand, third_hand = [], [], []
		for i in range(3):
			first_hand.append(deck.pop())
		for i in range(5):
			second_hand.append(deck.pop())
			third_hand.append(deck.pop())
		hand = [first_hand,second_hand,third_hand]
		hands.append(hand)
	return hands

# generates hands till 
def handRezocnitionTest():
	print("generates hands and calls hand recognition functions till they return True")
	print("then prints the function name and the hand that returned True")
	print("-----test-----")
	hands = generatePokerHands(1)
	hand = hands[0]
	cards = hand[2]

	while False == pair(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("pair:")
	print(cards)
	print("-----")
	while False == twoPairs(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("twoPairs:")
	print(cards)
	print("-----")
	while False == threeOfKind(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("threeOfKind:")
	print(cards)
	print("-----")
	while False == straight(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("straight:")
	print(cards)
	print("-----")
	while False == flush(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("flush:")
	print(cards)
	print("-----")
	while False == fullHouse(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("fullHouse:")
	print(cards)
	print("-----")
	while False == fourOfKind(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("fourOfKind:")
	print(cards)
	print("-----")
	while False == straightFlush(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("straightFlush:")
	print(cards)
	print("-----")
	while False == royalFlush(cards):
		hands = generatePokerHands(1)
		hand = hands[0]
		cards = hand[2]
	print("royalFlush:")
	print(cards)
	print("-----")



pokerHands = generatePokerHands(player_count)
score = []
#print(pokerHands)
for i in range(len(pokerHands)):
	score.append(countScore(pokerHands[i]))
#print(score)
handRezocnitionTest()