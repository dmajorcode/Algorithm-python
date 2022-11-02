import heapq
import sys
input = sys.stdin.readline
arr=[]

for i in range(int(input())):
    X = int(input())
    if X!=0:
        heapq.heappush(arr,-X)
    elif len(arr) == 0:
        print(0)
    else:
        print(-1*heapq.heappop(arr))