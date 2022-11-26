import sys
from itertools import combinations
from itertools import permutations
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int,input().split())))
    
nums = [i for i in range(1,N+1)]

# (1) 팀을 나누는 combinations    
# (1,2) (1,3) (1,4) (2,3) (2,4) (3,4)
splittedTeams = list(combinations(nums,int(N/2)))
length = len(splittedTeams)

# (1,2) (1,3) (1,4)
firstHalf = splittedTeams[:int(length/2)]

minDiff = 1e9
    
def getScore(indexes):
    score = 0
    # (2) 능력치 index의 permutations with 2
    combs = list(permutations(indexes,2))
    
    for comb in combs:
        combList = list(comb)
        index1 =combList[0]
        index2 =combList[1]
        
        score+=S[index1-1][index2-1]

    return score

# 짝인 조합을 찾는다.
def getRestHalf(indexes):
    arr=[]
    for i in range(1,N+1):
        if i not in list(indexes):
            arr.append(i)
    return arr

for indexes in firstHalf:
    firstScore = getScore(indexes)
    restHalf = getRestHalf(indexes)
    lastScore = getScore(restHalf)
    diff = abs(firstScore - lastScore)
    minDiff = min(minDiff,diff)

print(minDiff)