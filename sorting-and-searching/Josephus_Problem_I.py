import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n + 1)])

order = []

while q:
    q.append(q.popleft())
    order.append(q.popleft())

print(" ".join(map(str, order)))