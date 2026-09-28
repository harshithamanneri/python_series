choice = input("Type 'C' to convert to Celsius or 'F' to convert to Fahrenheit: ").upper()
temp = float(input("Enter the temperature value: "))

if choice == 'C':
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted:.2f}°C")
elif choice == 'F':
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted:.2f}°F")
else:
    print("Invalid choice!")
