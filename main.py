def calculate_bmi(weight, height):
    """Calculate BMI and return the category."""
    try:
        height_m = height / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        return round(bmi, 2), category
    except ZeroDivisionError:
        return None, "Height cannot be zero."

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        bmi, category = calculate_bmi(weight, height)
        if bmi:
            print(f"Your BMI is {bmi}, which is categorized as: {category}.")
        else:
            print(category)
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
