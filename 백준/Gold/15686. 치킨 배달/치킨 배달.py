'''
(계획) 12:50~1:30
(실제) 12:50~1:38
'''

# (오답노트) house, chicken position이 실제와 다르게 들어갔다.

'''
1. get chicken distance for every house
2. add minimum value and it will be chicken distance of the city

housedistance : [] and chicken distance for every house > changed into number and save by comparing
citydistance : (number) and sum of minimum of housedistance for all the house
'''

import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())

# graph of city
# graph = []

# house position [(1,3),(2,5)]
house = []

# chicken position [(2,3),(3,3)]
chicken = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
    # (틀린 부분)
    # for j in line:
        if line[j] == 1:

            house.append((i+1, j+1))
        elif line[j] == 2:

            chicken.append((i+1, j+1))
        else:
            pass

citydist = []

# all possibility of chicken house
# [[(1,2),(2,3),(3,4)],[(1,2),(3,4)(4,5)]]
chickenposition = list(combinations(chicken,m))

# chickenposition별로 걸리는 거리를 저장한다.
chickendist=[0 for _ in range(len(chickenposition))]


for x, y in house:
    t=0
    # check all chicken store
    for c in chickenposition:
        housedist = 1e9
        for i, j in c:

            dist = abs(x-i) + abs(y-j)
            housedist = min(dist, housedist)

        chickendist[t] += housedist
        t+=1


print(min(chickendist))
    








