'''
(계획) 7:24~7:54
'''

'''
풀이) dp[n] : n을 선택할 때 최대가 되는 경우
    dp테이블을 어떻게 해야 할지 정해야 한다. 이차원? 일차원? 규칙성을 보고 판단해야 겠다.
    그냥 이차원 테이블을 구현하고, 값이 없는 경우에는 0으로 둬야 할 것 같다.
    dp 값을 업데이트 하는 형식으로 진행. 순서대로기 때문에 순차적으로 갱신된다.
출력) 마지막 줄의 최댓값을 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]

# 실제 값을 업데이트한다.
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        dp[i][j] = a[j]
        
# 점화식 dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j] (있는지 범위 확인 필요함)
# dp[0][0]은 초기값으로 검사하지 않아야 함

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]

maximum = 0

for i in range(n):
    maximum = max(dp[n-1][i], maximum)
        
print(maximum)