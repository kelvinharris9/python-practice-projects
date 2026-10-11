# Initialize global variables
miles = 0.0
km = 0.0
feet = 0.0
meters = 0.0
lbs = 0.0
kg = 0.0
oz = 0.0
grams = 0.0
degrees_f = 0.0 # degrees Fahrenheit
degrees_c = 0.0 # degrees Celsius

# Define miles to kilometers conversion function
def miles_to_km():
    # Allow this function to modify global variable km
    global km
    # Perform conversion
    km = miles * 1.609344
    print(f"{miles:.2f} mi = {km:.2f} km\n")
# Define miles to kilometers conversion function
def km_to_miles():
    # Allow this function to modify global variable miles
    global miles
    # Perform conversion
    miles = km / 1.609344
    print(f"{km:.2f} km = {miles:.2f} mi\n")
# Define feet to meters conversion function
def feet_to_meters():
    # Allow this function to modify global variable meters
    global meters
    # Perform conversion
    meters = feet * .3048
    print(f"{feet:.2f} ft = {meters:.2f} m\n")
# Define meters to feet conversion function
def meters_to_feet():
    # Allow this function to modify global variable feet
    global feet
    # Perform conversion
    feet = meters * 3.28084
    print(f"{meters:.2f} m = {feet:.2f} ft\n")
# Define lbs to kg conversion function
def lbs_to_kg():
    # Allow this function to modify global variable kg
    global kg
    # Perform conversion
    kg = lbs * .45359237
    print(f"{lbs:.2f} lbs = {kg:.2f} kg\n")
# Define kg to lbs conversion function
def kg_to_lbs():
    # Allow this function to modify global variable lbs
    global lbs
    # Perform conversion
    lbs = kg * 2.20462
    print(f"{kg:.2f} kg = {lbs:.2f} lbs\n")
# Define oz to grams conversion function
def oz_to_grams():
    # Allow this function to modify global variable grams
    global grams
    # Perform conversion
    grams = oz * 28.349523125
    print(f"{oz:.2f} oz = {grams:.2f} g\n")
# Define grams to oz conversion function
def grams_to_oz():
    # Allow this function to modify global variable oz
    global oz
    # Perform conversion
    oz = grams / 28.349523125
    print(f"{grams:.2f} g = {oz:.2f} oz\n")
# Define Fahrenheit to Celsius conversion function
def fahrenheit_to_celsius():
    # Allows this function to modify global variable degrees_c
    global degrees_c
    # Perform conversion
    degrees_c = round((degrees_f - 32.0) * (5.0 / 9.0), 2)
    print(f"{degrees_f}°F = {degrees_c}°C\n")
# Define Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit():
    # Allows this function to modify global variable degrees_f
    global degrees_f
    # Perform conversion
    degrees_f = round((degrees_c * (9.0 / 5.0)) + 32.0, 2)
    print(f"{degrees_c}°C = {degrees_f}°F\n")
# Define user_menu function for user to interact with
def user_menu():
    global miles, km, feet, meters, lbs, kg, oz, grams
    global degrees_f, degrees_c
    # Prompt user to select a category
    print("Enter a number to select a category:")
    print("1) Distance\n2) Weight\n3) Temperature\n")
    # Read in user input
    category = int(input("Type here -> "))
    print()

    if category == 1:
        print("Enter a number to select a distance conversion:\n"
              "1) Miles to Kilometers\n"
              "2) Kilometers to Miles\n"
              "3) Feet to Meters\n"
              "4) Meters to Feet\n")
        conversion = int(input("Type here -> "))
        print()
        if conversion == 1:
            miles = float(input("Enter distance in miles: "))
            miles_to_km()
        elif conversion == 2:
            km = float(input("Enter distance in kilometers: "))
            km_to_miles()
        elif conversion == 3:
            feet = float(input("Enter distance in feet: "))
            feet_to_meters()
        elif conversion == 4:
            meters = float(input("Enter distance in meters: "))
            meters_to_feet()

    elif category == 2:
        print("Enter a number to select a weight conversion:\n"
              "1) Pounds to Kilograms\n"
              "2) Kilograms to Pounds\n"
              "3) Ounces to Grams\n"
              "4) Grams to Ounces\n")
        conversion = int(input("Type here -> "))
        print()
        if conversion == 1:
            lbs = float(input("Enter weight in pounds: "))
            lbs_to_kg()
        elif conversion == 2:
            kg = float(input("Enter weight in kilograms: "))
            kg_to_lbs()
        elif conversion == 3:
            oz = float(input("Enter weight in ounces: "))
            oz_to_grams()
        elif conversion == 4:
            grams = float(input("Enter weight in grams: "))
            grams_to_oz()
    elif category == 3:
        print("Enter a number to select a temperature conversion:\n"
              "1) Fahrenheit to Celsius\n"
              "2) Celsius to Fahrenheit\n")
        conversion = int(input("Type here -> "))
        print()
        if conversion == 1:
            degrees_f = float(input("Enter temperature in degrees Fahrenheit: "))
            fahrenheit_to_celsius()
        elif conversion == 2:
            degrees_c = float(input("Enter temperature in degrees Celsius: "))
            celsius_to_fahrenheit()

# Define main function
def main():
    user_menu()


if __name__ == "__main__":
    main()
