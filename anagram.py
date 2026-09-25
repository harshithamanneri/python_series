from collections import Counter

def is_anagram(str1, str2):
   
    return Counter(str1.lower()) == Counter(str2.lower())

print(is_anagram("Listen", "Silent")) 
print(is_anagram("Hello", "World"))    
