import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N,M = list(map(int, input().split()))

arr = [i for i in range(1, N+1)]

ans = combinations_with_replacement(arr,M)

for i in ans:
    print(' '.join(list(map(str,i))))
