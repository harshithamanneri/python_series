arr = [2, 2, 1, 2, 3, 2, 2]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in freq:
    if freq[num] > len(arr) // 2:
        print(num)
        break