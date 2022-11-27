import sys
from itertools import combinations
input = sys.stdin.readline

# comination하고 더하기가 0인 것은 ++한다.

N,S = list(map(int,input().split()))
arr = list(map(int, input().split()))

visited = [False]*(N)
count = 0

def getComb(idx, sumPart):
    global count
    
    if idx >= N:
        return

    sumPart+=arr[idx]
    
    if sumPart == S:
        count+=1
    
    # 현재 arr[idx]를 선택한 경우
    getComb(idx+1,sumPart)
    # 현재 arr[idx]를 선택하지 않은 경우
    getComb(idx+1,sumPart-arr[idx])
            
getComb(0,0)
print(count)