import math

votes = [720, 300, 480]
distribution = []
calc_tab = []
max_index = 0
num_committees = len(votes)
num_seats = 8

def calculate(votes, number_seats):
    return (votes * 1.0) / (2 * number_seats + 1.0)

def sainte_lague(votes):
    calc_tab.clear()
    for i in range(num_committees):
        distribution.append(0)

    for i in range(num_committees):
        calc_tab.append(votes[i])

    for i in range(num_seats):
        max = -1
        for j in range(num_committees):
            if max < calc_tab[j]:
                max = calc_tab[j]
                max_index = j
        distribution[max_index] += 1
        calc_tab[max_index] = calculate(votes[max_index], distribution[max_index])
    return distribution


def display(distribution):
    for i in range(num_committees):
        print("Committee", (i + 1), distribution[i])


display(sainte_lague(votes))
