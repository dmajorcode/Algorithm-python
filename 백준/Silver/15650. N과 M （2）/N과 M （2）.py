import sys
input=sys.stdin.readline

N, M = list(map(int, input().split()))

arr = []

def dfs(start):
  if len(arr) == M:
    print(' '.join(map(str,arr)))
    return
  for i in range(start,N+1):
    arr.append(i)
    dfs(i+1)
    arr.pop()

dfs(1)
