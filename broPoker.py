import random
import configparser

config = configparser.ConfigParser()
config.read('conf.ini')
print(config.sections())
player_count = config['general']['player_count']
poker_card_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
poker_suit_types = [1, 2, 3, 4]
poker_hand_types = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
    x,y = -1,-1
    for i in values:
        if x == i and y == i:
            return True
        y = x
        x = i
    return False

def straight(hand):
    values = set()
    hand.sort()
    x = 0
    for card in hand:
        values.add(card[0]-x)
        x = x+1
    if len(values) == 1:
        return True
    return False

def flush(hand):
    suits = set()
    for card in hand:
        suits.add(card[1])
    if len(suits) == 1:
        return True
    return False

def fullHouse(hand):
    values = set()
    for card in hand:
        values.add(card[0])
    if len(values) == 2:
        return True
    return False

def fourOfKind(hand):
    values = []
    for card in hand:
        values.append(card[0])
    values.sort()
    a,b,c = -1,-1,-1
    for value in values:
        if value == a and value == b and value == c:
            return True
        c = b
        b = a
        a = value
    return False

def straightFlush(hand):
    if straight(hand) == True and flush(hand) == True:
        return True
    return False

def royalFlush(hand):
    hand.sort()
    card = hand[4]
    if straightFlush(hand) == True and card[0] == 14:
        return True
    return False

def scoreFrontHand(hand):
    hand.sort()
    if threeOfKind(hand):
        return 9 + hand[0]
    if pair(hand):
        if hand[2] >= 5:
            return 1 + hand[0]
        else:
            return 1
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
        for j in range(14):
            card = [j+1,i+1]
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

def main():
    pokerHands = generatePokerHands(player_count)
    score = []
    print(pokerHands)
    for i in range(len(pokerHands)):
        score.append(countScore(pokerHands[i]))
    print(score)
    