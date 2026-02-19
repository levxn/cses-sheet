import sys
from collections import defaultdict
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
MOD = 10**9 + 7
freq = defaultdict(int)

for i in range(n):
    freq[arr[i]] += 1

res = 1
for f in freq.values():
    res = (res * (f + 1)) % MOD

print((res-1)%MOD)