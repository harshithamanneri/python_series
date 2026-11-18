import math

n = int(input())
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += math.factorial(digit)
    temp //= 10

if total == n:
    print("Strong Number")
else:
    print("Not Strong")