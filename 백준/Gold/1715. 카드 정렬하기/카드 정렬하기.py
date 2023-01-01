'''
(계획) 5:31~6:01
(실제) 5:31~6:01
'''

# (오답노트) list시 시간초과났음. heapq로 변경 필요

import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
result = 0
    
while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    sumnum = one + two
    result += sumnum
    heapq.heappush(heap, sumnum)
    
print(result)