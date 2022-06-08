def rps(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


p1 = input('Informe sua jogada: ')
p2 = input('Informe sua jogada: ')
print(rps(p1, p2))
