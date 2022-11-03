import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

# dp[n] : n을 1,2,3의 합으로 나타내는 방법의 수
# 점화식 dp(n) = dp(n-1)+dp(n-2)+dp(n-3)

for i in range(4,11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in range(T):
    print(dp[int(input())])



