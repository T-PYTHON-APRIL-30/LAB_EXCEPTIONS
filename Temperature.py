'''
Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

Instructions:
Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.

Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.

Write a main function that: a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F"). b. Splits the input string into a temperature value and its unit. c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit). d. Handles the following exceptions: - ValueError: If the user enters an invalid temperature value, display an error message and prompt the user to try again. - TypeError: If the user enters an invalid unit, display an error message and prompt the user to try again. e. If the conversion is successful, print the converted temperature and its unit.

Call the main function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            temp_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temp_value, temp_unit = temp_input.split()

            if temp_unit.upper() == 'C':
                celsius = float(temp_value)
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"Temperature in Fahrenheit: {fahrenheit} F")
                break
            elif temp_unit.upper() == 'F':
                fahrenheit = float(temp_value)
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"Temperature in Celsius: {celsius:.2f} C")
                break
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value. Please enter a valid number.")
        except TypeError as e:
            print(e)

main()
