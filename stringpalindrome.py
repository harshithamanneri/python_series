
s = input().lower().replace(" ", "")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
