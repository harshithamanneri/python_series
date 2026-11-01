arr = [1, 2, 4, 6, 8, 10]
target = 5

floor = -1

for num in arr:
    if num <= target:
        floor = num

print("Floor:", floor)