import math

votes = [720, 300, 480]
distribution = []
calc_tab = []
max_index = 0
num_committees = len(votes)
num_seats = 8


def totalVotes(votes):
    votes_count = 0
    for i in range(num_committees):
        votes_count += votes[i]
    return votes_count


def mandates(votes):
    mandates_count = 0
    votes_count = totalVotes(votes)
    calc_tab.clear()
    for i in range(num_committees):
        calc_tab.append((votes[i] * num_seats * 1.0) / votes_count)
        distribution.append(int(math.floor(calc_tab[i])))
        calc_tab[i] -= distribution[i]
        mandates_count += distribution[i]
    return mandates_count


def rest_mandates(votes):
    mandates_count = mandates(votes)
    while mandates_count < num_seats:
        max = -1
        for i in range(num_committees):
            if max < calc_tab[i]:
                max = calc_tab[i]
                max_index = i
        distribution[max_index] += 1
        mandates_count += 1
        calc_tab[max_index] = 0
    return distribution


def display(distribution):
    for i in range(num_committees):
        print("Committee", (i + 1), distribution[i])


display(rest_mandates(votes))
