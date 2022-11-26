import sys
from itertools import permutations

input = sys.stdin.readline

N =int(input())
A = list(map(int, input().split()))

arrs = permutations(A,N)

# 주어진 점화식 함수
def absNumFormat(arr):
    absNum = 0
    for i in range(0,N-1):
        absNum += abs(arr[i]-arr[i+1])
    return absNum

maxNum = 0
for arr in arrs:
    absNum = absNumFormat(arr)
    maxNum = max(maxNum,absNum)

print(maxNum)



# permutations 하고 주어진 점화식에 넣기