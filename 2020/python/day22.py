with open('../day_22.txt') as f:
    input1, input2 = f.read().split('\n\n')
    player1 = [int(line) for line in input1.splitlines()[1:]]
    player2 = [int(line) for line in input2.splitlines()[1:]]

def score_deck(deck):
    return sum((i+1) * card for i, card in enumerate(reversed(deck)))

deck1, deck2 = player1[:], player2[:]
while len(deck1) > 0 and len(deck2) > 0:
    card1, card2 = deck1.pop(0), deck2.pop(0)
    if card1 > card2:
        deck1 += [card1, card2]
    else:
        deck2 += [card2, card1]
print('part 1:', score_deck(deck1 if len(deck1) != 0 else deck2))


def recursive_combat(deck1, deck2):
    rounds = set()
    while len(deck1) > 0 and len(deck2) > 0:
        t = (tuple(deck1), tuple(deck2))
        if t in rounds:
            return 1
        rounds.add(t)

        card1, card2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner = recursive_combat(deck1[:card1], deck2[:card2])
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
    return 1 if len(deck1) != 0 else 2

deck1, deck2 = player1[:], player2[:]
winner = recursive_combat(deck1, deck2)
print('part 2:', score_deck(deck1 if winner == 1 else deck2))
