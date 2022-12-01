import sys
from itertools import permutations

input = sys.stdin.readline

# both input as string
A,B = list(input().split())

aList = list(A)

# (1234,1243,1324,1342 and so on )
pers = permutations(aList, len(A))

arr=[]

for per in pers:
    
    perInt = int("".join(per))
    if perInt < int(B) and int(per[0])!=0:
        arr.append(perInt)

if len(arr) == 0:
    print(-1)
else:
    print(max(arr))