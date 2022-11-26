from itertools import permutations
import sys

input = sys.stdin.readline

N, M = list(map(int,input().split()))
arr = list(map(int,input().split()))

# pick M amount of numbers from arr

arr.sort()

per = permutations(arr,M)

for i in per:
    print(' '.join(list(map(str, i))))