import random

def printCards(cards):
    for c in cards:
        print(f"Card {c}")
        for r, (b, i, n, g, o) in enumerate(cards[c]):
            print(f"{b}\t{i}\t{n}\t{g}\t{o}")
        print()

def genCards(num):
    cards = {}
    for i in range(num):
        bank = genBank()
        card = []
        for j in range(5):
            row = random.sample(bank, 5)
            bank = [item for item in bank if item not in row]
            card.append(row)
        card[2][2] = "free"
        cards[i] = card
    return cards

def numCards(num):
    cards = {}
    index = 0
    for i in range(num):
        cards[i] = []
        for j in range(5):
            list = []
            for k in range(5):
                list.append(index)
                index += 1
            cards[i].append(list)
    return cards

def genBank():
    list = []
    for i in range(1, 91):
        list.append(i)
    return list

cards = genCards(8)
printCards(cards)