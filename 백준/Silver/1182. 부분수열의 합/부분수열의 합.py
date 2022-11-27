import sys
from itertools import combinations
input = sys.stdin.readline

# comination하고 더하기가 0인 것은 ++한다.

N,S = list(map(int,input().split()))
arr = list(map(int, input().split()))

count = 0

def getComb(i):
    global count
# combinations are tuples like (-7,-3) (-7,-2)
    picked = list(combinations(arr,i))
    for pick in picked:
        pickList = list(pick)
        if sum(pickList)==S:
            count+=1
        
for i in range(1,N+1):
    getComb(i)

print(count)