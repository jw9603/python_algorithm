# 백준 2164. 카드2
# https://www.acmicpc.net/problem/2164
import sys
from collections import deque
N = int(sys.stdin.readline().strip())
def sol(N):
    q = deque()
    for i in range(1, N + 1):
        q.append(i)
    while len(q) > 1:
        q.popleft()
        data = q.popleft()
        q.append(data)
    print(*q)
sol(N=N)
        
        