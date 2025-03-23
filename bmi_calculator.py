# BMI Calculator
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254


def calculate_body_mass_index(weight_pounds, height_inches):
    weight_kilograms = weight_pounds * \
        POUNDS_TO_KILOGRAMS  # Convert weight to kilograms
    height_meters = height_inches * INCHES_TO_METERS  # Convert height to meters
    body_mass_index = weight_kilograms / \
        (height_meters * height_meters)  # Calculate BMI
    return body_mass_index


def categorize_body_mass_index(body_mass_index):
    if body_mass_index < 18.5:
        return "underweight"
    elif 18.5 <= body_mass_index < 24.9:
        return "normal weight"
    elif 25 <= body_mass_index < 29.9:
        return "overweight"
    else:
        return "obese"


# user input
weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

# Calculate BMI
body_mass_index = calculate_body_mass_index(weight_pounds, height_inches)
category = categorize_body_mass_index(body_mass_index)

# the result
print(f"Your BMI is: {body_mass_index:.2f}")
print(f"You are in the {category} category.")
