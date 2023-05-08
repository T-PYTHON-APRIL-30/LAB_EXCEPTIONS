# # Bonus
# ##  Temperature Converter

# Description: In this exercise, you will practice using Python exceptions by creating a simple 
# temperature converter that accepts user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

# #### Instructions:

# 1. Write a function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an
# argument and returns the equivalent temperature in Fahrenheit. 
# Use the formula `fahrenheit = (celsius * 9/5) + 32`.

def celsius_to_fahrenheit(celsius,unit_c):
    unit_c="C"
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit,unit_c

# print ("Enter the temprature degree to conver it to_fahrenheit ",round(celsius_to_fahrenheit(40),1))

# 2. Write a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an 
# argument and returns the equivalent temperature in Celsius.
#  Use the formula `celsius = (fahrenheit - 32) * 5/9`.
def fahrenheit_to_celsius(fahrenheit,unit_f):
    unit_f="F"
    celsius = (fahrenheit - 32) * 5/9
   
    return celsius,unit_f

# print ("Enter the temprature degree to conver it to celsius ",round (fahrenheit_to_celsius(110),1))


# 3. Write a `main` function that:
#     a. Prompts the user for input, asking them to enter a temperature and its unit
#  (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
#     b. Splits the input string into a temperature value and its unit.
#     c. Tries to convert the input temperature to its opposite unit using the appropriate function 
# (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
#     d. Handles the following exceptions:
#         - `ValueError`: If the user enters an invalid temperature value, display an 
#           error message and prompt the user to try again.
#         - `TypeError`: If the user enters an invalid unit, display an error message and prompt the
#           user to try again.
#     e. If the conversion is successful, print the converted temperature and its unit.





def main(temp,unit):
    if unit == 'C' or unit == 'c' :
        newTemp =(celsius_to_fahrenheit(temp,unit))
        print(f"The temperature in Fahrenheit ={newTemp}")
    elif unit == 'F' or unit == 'f' :
        newTemp = (fahrenheit_to_celsius(temp,unit))
        print(f"The temperature in Celsius = {newTemp}")
    return temp,unit


# 4. Call the `main` function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

try:
    temp = float(input("Enter Temperature: "))
    unit = str(input("Enter unit('C' for Celsius or 'F' for Fahrenheit): "))
except ValueError:
    print("invalid value,Please enter an integer value")
except TypeError:
    print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("The converted temperature and its unit:")

main(temp,unit)
