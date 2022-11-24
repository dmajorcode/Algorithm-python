from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# target list in range N
narr = [str(i) for i in range(1,N+1)]

target = combinations(narr, M)

for t in list(target):
    print(' '.join(list(t)))