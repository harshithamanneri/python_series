
arr = [10, 20, 30, 40, 50]
target = int(input("Enter element to search: "))

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        break
else:
    print("Element not found")
