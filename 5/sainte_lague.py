def normalize(values):
    total = sum(values)
    return [1.0 * value / total for value in values]


def sainte_lague(votes, seats):
    votes = normalize(votes)
    seats = normalize(seats)
    return sum(1.0 / v * (v - s) ** 2 for v, s in zip(votes, seats))


votes = [750, 150, 50, 50]
seats = [80, 16, 2, 2]
print(sainte_lague(votes, seats))
