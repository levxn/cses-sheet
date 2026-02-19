import sys
input = sys.stdin.readline

n = int(input())
ranges = []

for i in range(n):
    x, y = map(int, input().split())
    ranges.append((x, y, i))


ranges.sort(key = lambda x: (x[0], -x[1]))

contains = [0]*n
contained = [0]*n

max_y = 0
for x, y, idx in ranges:
    if y<=max_y:
        contained[idx] = 1
    max_y = max(max_y, y)

min_y = float('inf')
for x, y, idx in reversed(ranges):
    if y>=min_y:
        contains[idx] = 1
    min_y = min(min_y, y)

print(*contains)
print(*contained)