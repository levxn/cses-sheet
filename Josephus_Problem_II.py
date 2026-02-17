import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

order = []
q = deque([i for i in range(1, n + 1)])

while q:
    if n>k:
        if n%k != 0:
            for _ in range(n//k):
                q.append(q.popleft())
            order.append(q.popleft())
        else:
            for _ in range(k%n):
                q.append(q.popleft())
            order.append(q.popleft())

print(" ".join(map(str, order)))