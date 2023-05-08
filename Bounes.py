"""
 Bonus
##  Temperature Converter

Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

#### Instructions:

1. Write a function `celsius_to_fahrenheit(celsius)` that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula `fahrenheit = (celsius * 9/5) + 32`.

2. Write a function `fahrenheit_to_celsius(fahrenheit)` that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula `celsius = (fahrenheit - 32) * 5/9`.

3. Write a `main` function that:
    a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F").
    b. Splits the input string into a temperature value and its unit.
    c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
    d. Handles the following exceptions:
        - `ValueError`: If the user enters an invalid temperature value, display an error message and prompt the user to try again.
        - `TypeError`: If the user enters an invalid unit, display an error message and prompt the user to try again.
    e. If the conversion is successful, print the converted temperature and its unit.

4. Call the `main` function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

Example Output:

```
Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C
```
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
try:
    temperature=input("enter a temperature and its unit separated by a space (e.g., '25 C' or '77 F'):")

    temperature_number , temperature_unit = temperature.split()
    temperature_number=float(temperature_number)

     
    if temperature_unit.upper() == "C":
        converted_temp = celsius_to_fahrenheit(temperature_number)
        print(f"Temperature in Fahrenheit: {converted_temp:.1f} F")
    elif temperature_unit.upper() == "F":
        converted_temp = fahrenheit_to_celsius(temperature_number)
        print(f"Temperature in Celsius: {converted_temp:.2f} C")
    else:
        raise TypeError
except ValueError:
    print("Invalid temperature value. Please try again.")
except TypeError:
    print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit")
        

