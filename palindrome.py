def is_palindrome(text):

    s = str(text)
    return s == s[::-1]

print(is_palindrome("racecar"))  
print(is_palindrome(12321))      
print(is_palindrome("hello"))    
