'''
(계획) 3:08~3:28
'''

'''
-국어, 영어, -수학, 이름(아스키코드), 이름(문자)
'''

import sys
input = sys.stdin.readline

n = int(input())

score = []

for i in range(n):
    name, kor, eng, math = input().split()
    score.append([-int(kor), int(eng), -int(math), name])
    
score.sort()

for i in range(n):
    print(score[i][3])
