# Initialize global variables
from_unit = ""
to_unit = ""
user_temp = 0.0
converted_temp = 0.0

# Define function to read in from unit and to unit
def get_units():
    # Allows this function to modify global from_unit and to_unit variables
    global from_unit
    global to_unit
    # Prompt user to enter from unit
    print("Enter the unit of measurement you want to convert from.")
    # Read in from unit from user input
    from_unit = input("From: ").capitalize().strip()
    # Print blank line
    print()
    # Prompt user to enter to unit
    print("Enter the unit of measurement you want to convert to.")
    # Read in to unit from user input
    to_unit = input("To: ").capitalize().strip()
    # Print blank line
    print()

# Define function to read in temperature to be converted
def get_temp():
    # Allows this function to modify global user_temp variable
    global user_temp
    # Prompt user to enter temperature
    print("Enter the temperature to be converted.")
    # Read in temperature from user input
    user_temp = round(float(input("Temp: ")), 2)
    # Print blank line
    print()

# Define function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    # Allows this function to modify global converted_temp variable
    global converted_temp
    # Calculate Celsius to Fahrenheit conversion
    converted_temp = round((user_temp * (9.0 / 5.0)) + 32.0, 2)
    # Display conversion results
    print(f"{user_temp} °C is equal to {converted_temp} °F.")

# Define function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    # Allows this function to modify global converted_temp variable
    global converted_temp
    # Calculate Fahrenheit to Celsius conversion
    converted_temp = round((user_temp - 32.0) * (5.0 / 9.0), 2)
    # Display conversion results
    print(f"{user_temp} °F is equal to {converted_temp} °C.")

# Define function to convert Celsius to Kelvin
def celsius_to_kelvin():
    # Allows this function to modify global converted_temp variable
    global converted_temp
    # Calculate Celsius to Kelvin conversion
    converted_temp = round(user_temp + 273.15, 2)
    # Display conversion results
    print(f"{user_temp} °C is equal to {converted_temp} K.")

# Define function to convert Kelvin to Celsius
def kelvin_to_celsius():
    # Allows this function to modify global converted_temp variable
    global converted_temp
    # Calculate Kelvin to Celsius conversion
    converted_temp = round(user_temp - 273.15, 2)
    # Display conversion results
    print(f"{user_temp} K is equal to {converted_temp} °C.")

# Define function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin():
    # Allows this function to modify global converted_temp variable
    global converted_temp
    # Calculate Fahrenheit to Kelvin conversion
    converted_temp = round((user_temp - 32.0) * (5.0 / 9.0) + 273.15, 2)
    # Display conversion results
    print(f"{user_temp} °F is equal to {converted_temp} K.")

# Define function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit():
    # Allows this function to modify global converted_temp variable
    global converted_temp
    # Calculate Fahrenheit to Kelvin conversion
    converted_temp = round((user_temp - 273.15) * (9.0 / 5.0) + 32.0, 2)
    # Display conversion results
    print(f"{user_temp} K is equal to {converted_temp} °F.")

# Define function to determine wha units to convert from and to
# based on user input
def determine_conversion():
    if from_unit == "C" and to_unit == "F":
        celsius_to_fahrenheit()
    elif from_unit == "F" and to_unit == "C":
        fahrenheit_to_celsius()
    elif from_unit == "C" and to_unit == "K":
        celsius_to_kelvin()
    elif from_unit == "K" and to_unit == "C":
        kelvin_to_celsius()
    elif from_unit == "F" and to_unit == "K":
        fahrenheit_to_kelvin()
    elif from_unit == "K" and to_unit == "F":
        kelvin_to_fahrenheit()

# Define main function
def main():
    get_units()
    get_temp()
    determine_conversion()

# Run the program only if this file is executed directly, not imported as a module
if __name__ == "__main__":
    main()