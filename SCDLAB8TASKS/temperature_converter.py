# temperature_converter.py

def main():
    print("--- Temperature Converter ---")
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit type (C for Celsius, F for Fahrenheit): ").strip().upper()

        # Convert accordingly
        if unit == 'C':
            converted = (temp * 9/5) + 32
            print(f"{temp} °C is equal to {converted:.2f} °F")
        elif unit == 'F':
            converted = (temp - 32) * 5/9
            print(f"{temp} °F is equal to {converted:.2f} °C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a number.")

    # Added so the command window doesn't close immediately in the .exe
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()