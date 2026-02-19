import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

tree = [0]*(n+1)

def update(i, delta):
    while i<=n:
        tree[i] += delta
        i += i&(-i)

def query():
    s = 0
    while i>0:
        s += tree[i]
        i -= i&(-i)
    return s

def find(k):
    cur = 0
    bit_mask = 1<<(n.bit_length())
    while bit_mask:
        nxt = cur + bit_mask
        if nxt <= n and tree[nxt] < k:
            k -= tree[nxt]
            cur = nxt
        bit_mask >>= 1
    return cur+1

for i in range(1, n+1):
    update(i, 1)

res = []
pos = 0
remaining = n
for i in range(n):
    pos = (pos + k) % remaining
    kth = pos + 1
    
    idx = find(kth)
    res.append(str(idx))
    
    update(idx, -1)  # remove
    remaining -= 1

print(" ".join(res))