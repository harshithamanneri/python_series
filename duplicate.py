# duplicate.py - Finds duplicate elements in a list

def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)

# Example Usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 2, 4, 5, 6, 5]
    print(f"Original List: {numbers}")
    
    result = find_duplicates(numbers)
    print(f"Duplicate Items: {result}")
