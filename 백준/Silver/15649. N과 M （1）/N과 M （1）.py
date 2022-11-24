N,M=map(int, input().split())
ans = []
visited = [False]*(N+1)
def dfs():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(1,N+1):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        dfs()
        ans.pop()
        visited[i] = False
dfs()