import random

cards = []
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

for suit in suits:
  for rank in ranks:
    cards.append([suit, rank])

def shuffle():
  random.shuffle(cards)

def deal(num):
  hand = []
  i = 0
  while i < num:
    card = cards.pop()
    i += 1
    hand.append(card)
  return hand

shuffle()
dealtCards = deal(2)
print(dealtCards)  