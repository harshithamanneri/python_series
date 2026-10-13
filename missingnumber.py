arr = list(map(int, input().split()))
n = len(arr) + 1

total = n * (n + 1) // 2
missing = total - sum(arr)

print(missing)