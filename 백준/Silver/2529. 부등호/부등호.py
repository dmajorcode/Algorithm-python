import sys
from itertools import permutations

input = sys.stdin.readline

k = int(input())
signs = list(map(str,input().split()))

visited = [0]*10
maxArr = ""
minArr = ""

def check(i,j,sign):
    if sign == '>':
        return i>j
    if sign == '<':
        return i<j
    
def solve(index, s):
    global maxArr, minArr
    # should print when
    if index == (k+1):
        if len(minArr) ==0:
            minArr = s
        else:
            maxArr = s
        return 
        
    for i in range(10):
        if visited[i]==0:
            # s[-1]인 이유는 아래의 재귀에서 s에 str을 계속 더해 나가기 때문이다.
            if index==0 or check(s[-1],str(i),signs[index-1]):
                visited[i] = True
                solve(index+1,s+str(i))
                visited[i] = False
    
    
solve(0,"")
print(maxArr)
print(minArr)