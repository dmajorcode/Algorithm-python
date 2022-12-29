'''
(계획) 5:52~6:52
(실제) 5:52~6:52
'''

# (오답노트) int가 아닌데 int로 글자를 넣으려 했음. 가령, graph[i] = list(graph(int, input().split()))라 잘못함.
# obstacle 위치를.. 잘못 저장했다.. O인데 0으로 저장했다.if graph[i][j] == '0':
# True가 한 번이라도 나오면 answer가 True이다.
# 위의 경우 return으로 핸들이 어려우면 global 변수 값 변경으로 출력하면 된다.

'''
0. DFS 풀이
1. 하나의 좌표가 같고 T보다 S가 크면, O가 T보다 크고 S보다 작은 곳에 있다.
2. 3개의 장애물을 설치한다.
3. 감시를 피할 수 있는 지 함수를 통해서 확인한다.
4. 결과물을 출력한다. 'YES', 'NO'
'''

import sys
input = sys.stdin.readline

n = int(input())

graph = [[]for _ in range(n)]
map = [['X']*(n)for _ in range(n)]

for i in range(n):
    graph[i] = list(input().split())


# 감시를 피할 수 있다면 True 없다면 False
def escape(map):
    teacher = []
    student = []
    obstacle = []
    for i in range(n):
        for j in range(n):
            if map[i][j] == 'T':
                teacher.append((i,j))
            if map[i][j] == 'S':
                student.append((i,j))
            if map[i][j] == 'O':
                obstacle.append((i,j))

    for x, y in teacher:
        for a, b in student:
            if x == a:
                for i in range(min(y,b), max(y,b)):
                    if map[x][i] == 'O':
                        break
                else:    
                    return False
            if y == b:
                for i in range(min(x,a), max(x,a)):
                    if map[i][y] == 'O':
                        break
                else:
                    return False
    return True
    
answer = 'NO'    

# w는 wall count로 2일때까지 한다.
# map은 graph에 대한 개별 관리를 하는 것이다.
def dfs(w, graph):
    global answer

    if w == 3:
        # 감시를 피할 수 있는지 여부를 출력한다.
        if escape(graph):
            answer = 'YES'
            return
        return
        
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                w += 1
                dfs(w, graph)
                # 벽 없던 상태로 돌려둔다.
                w -= 1
                graph[i][j] = 'X'
            else:
                continue
                
    return 'NO'    

    
dfs(0, graph)
print(answer)
