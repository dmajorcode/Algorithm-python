import sys
from itertools import permutations

input = sys.stdin.readline

k = int(input())
signs = list(map(str,input().split()))

arr = [i for i in range(0,10)]

# maximum = 1e9
# minimum = -1e9
checkMaxMin = []

# (1,2,3) (1,2,4) ...
numParts = list(permutations(arr, k+1))

def check(numPart):
    global maximum
    global minimum
    # be careful for the range
    for i in range(k):
        if signs[i] == '>' and numPart[i] <= numPart[i+1]:
            break;
        if signs[i] == '<' and numPart[i] >= numPart[i+1]:
            break;
    else:
        partNum = ''.join(list(map(str,numPart))) 
        checkMaxMin.append(str(partNum))

for numPart in numParts:
    check(list(map(int,numPart)))

print(max(checkMaxMin))
print(min(checkMaxMin))
