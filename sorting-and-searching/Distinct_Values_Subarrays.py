import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

seen = set()
left = 0
result = 0

for right in range(n):
    while arr[right] in seen:
        seen.remove(arr[left])
        left += 1
    seen.add(arr[right])
    result += right - left + 1

print(result)