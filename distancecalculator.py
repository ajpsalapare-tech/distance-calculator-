# Constant for converting kilometers to miles
KM_TO_MILES_FACTOR = 0.621371

def convert_km_to_miles(kilometers: float) -> float:
    """Calculates and returns the conversion of kilometers to miles."""
    return kilometers * KM_TO_MILES_FACTOR

def main():
    print("=== Distance Calculator Program ===")
    
    while True:
        try:
            # 1. Get input from user and convert to a decimal number
            kilometers = float(input("\nEnter distance in kilometers: "))
            
            # 2. Calculate and display result
            miles = convert_km_to_miles(kilometers)
            print(f"Distance in miles: {miles:.6f}")
            
        except ValueError:
            print("Error: Please enter a valid numerical value.")
            continue
        
        # 3. Ask user if they wish to perform another conversion
        user_choice = input("Do you want to convert another distance? (yes/no): ").strip().lower()
        
        if user_choice != "yes":
            print("Program ended. Goodbye!")
            break

if __name__ == "__main__":
    main()
