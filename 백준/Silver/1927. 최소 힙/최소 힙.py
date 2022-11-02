import sys
import heapq
input = sys.stdin.readline
arr=[]

N=int(input())
for i in range(N):
    b = int(input())
    if b !=0:
        heapq.heappush(arr,b)
    elif len(arr) == 0:
        print(0)
    else:
        print(heapq.heappop(arr))