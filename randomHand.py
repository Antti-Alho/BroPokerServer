import random

def generatePokerhands(player_count):
	deck = []
	for i in range(4):
		for j in range(13):
			card = [j,i+1]
			deck.append(card)

	random.shuffle(deck)

	hands = []

	for x in range (player_count):

		first_hand, second_hand, third_hand = [], [], []

		for i in range(3):
			first_hand.append(deck.pop())

		for i in range(5):
			second_hand.append(deck.pop())
			third_hand.append(deck.pop())

		hand = [first_hand,second_hand,third_hand]
		hands.append(hand)
	
	return hands