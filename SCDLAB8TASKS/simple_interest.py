# simple_interest.py

def main():
    print("--- Simple Interest Calculator ---")
    try:
        # Take input from user
        p = float(input("Enter Principal amount: "))
        r = float(input("Enter Rate of interest (in %): "))
        t = float(input("Enter Time (in years): "))

        # Output the interest using formula: SI = (P * R * T) / 100
        si = (p * r * t) / 100
        print(f"\nThe Simple Interest is: {si:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

    # Added so the command window doesn't close immediately in the .exe
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()