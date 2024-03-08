def calculate_bmi(weight_lb, height_ft, height_in):
    # Convert height to inches
    height_total_in = height_ft * 12 + height_in
    # Convert weight to kilograms
    weight_kg = weight_lb * 0.45
    # Convert height to meters
    height_m = height_total_in * 0.025
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    # Get user input
    weight_lb = float(input("Enter your weight in pounds: "))
    height_ft = int(input("Enter your height in feet: "))
    height_in = int(input("Enter your height in inches: "))

    # Calculate BMI
    bmi = calculate_bmi(weight_lb, height_ft, height_in)

    # Get BMI category
    category = get_bmi_category(bmi)

    # Print result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are {category}.")

if __name__ == "__main__":
    main()
