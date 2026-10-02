arr = [0, 1, 0, 3, 12]

result = []

for x in arr:
    if x != 0:
        result.append(x)

zero_count = len(arr) - len(result)

result += [0] * zero_count

print(result)