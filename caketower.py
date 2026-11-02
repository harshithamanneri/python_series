n = int(input())
cakes = list(map(int, input().split()))

cakes.sort(reverse=True)

height = 0
for cake in cakes:
    height += cake

print(height)