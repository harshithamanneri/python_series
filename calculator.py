def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers, with division-by-zero protection."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("=== Welcome to the Python Calculator ===")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        # Check if user wants to exit
        if choice == '5':
            print("Goodbye! Thanks for using the calculator.")
            break
            
        # Validate operation choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please choose a valid option (1-5).")
            continue
            
        # Gather numeric inputs with error handling for non-numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")
            continue
            
        # Perform calculation based on user choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

# Run the program
if __name__ == "__main__":
    calculator()
