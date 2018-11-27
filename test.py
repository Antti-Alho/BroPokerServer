import random
from broPoker import *

def generatePokerHands(playerCount):
	deck = []
	for i in range(4):
		for j in range(14):
			card = [j+1,i+1]
			deck.append(card)
	random.shuffle(deck)
	hands = []
	for x in range (playerCount+1):
		first_hand, second_hand, third_hand = [], [], []
		for i in range(3):
			first_hand.append(deck.pop())
		for i in range(5):
			second_hand.append(deck.pop())
			third_hand.append(deck.pop())
		hand = [first_hand,second_hand,third_hand]
		hands.append(hand)
	return hands

def generateRoyalFlush():
	hand = [[13,4],[12,4],[11,4],[10,4],[14,4]]
	return hand

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
	cards = generateRoyalFlush()
	while False == royalFlush(cards):
		continue
	print("royalFlush:")
	print(cards)
	print("-----")

handRezocnitionTest()