import sys
from itertools import combinations

input = sys.stdin.readline

brr = []
while True:
    arrSK = list(map(int, input().split()))
    if arrSK[0] == 0:
        break;
    else:
        brr.append(arrSK)
    
for j in brr:
    s = j[0]
    com = combinations(j[1:],6)
    for i in com:
        print(' '.join(list(map(str,i))))
    print()

