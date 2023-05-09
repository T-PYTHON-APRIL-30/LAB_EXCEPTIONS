'''Temperature Converter
Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts user input and converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

Instructions:
Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.

Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.

Write a main function that: a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F"). b. Splits the input string into a temperature value and its unit. c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit). d. Handles the following exceptions: - ValueError: If the user enters an invalid temperature value, display an error message and prompt the user to try again. - TypeError: If the user enters an invalid unit, display an error message and prompt the user to try again. e. If the conversion is successful, print the converted temperature and its unit.

Call the main function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)

def main():
    ''''''
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            degree = float(user_input[:-1])
            char = user_input[-1]
            if char == "F":
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(degree)} C")
            elif char == "C":
                print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(degree)} F")
                break
            else:
                raise TypeError

        except:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.\n")

    

main()