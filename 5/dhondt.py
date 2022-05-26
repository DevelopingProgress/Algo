AV = 0
BV = 0
CV = 0
DV = 0
EV = 0
FV = 0
GV = 0
HV = 0
IV = 0
JV = 0

AS = 0
BS = 0
CS = 0
DS = 0
ES = 0
FS = 0
GS = 0
HS = 0
IS = 0
JS = 0

names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
parties = [AV, BV, CV, DV, EV, FV, GV, HV, IV, JV]
points = [AV, BV, CV, DV, EV, FV, GV, HV, IV, JV]
seats = [AS, BS, CS, DS, ES, FS, GS, HS, IS, JS]

for i in range(0, 10):
    parties[i] = int(input("Votes to party " + names[i] + ":"))
    points[i] = parties[i]
    if parties[i] == 0:
        break
seatsToDistribution = int(input("\nAmount os seats that are going to be distributed: "))


def giveASeat():
    biggest = max(points)
    index = points.index(biggest)
    seats[index] += 1
    points[index] = parties[index] / (seats[index] + 1)


for i in range(0, seatsToDistribution):
    giveASeat()

print("")
for i in range(0, 10):
    if parties[i] == 0:
        break
    print("Seats to party " + names[i] + ": " + str(seats[i]))
