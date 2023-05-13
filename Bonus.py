'''Bonus
Temperature Converter
Description: In this exercise, you will practice using Python exceptions by creating a simple temperature
converter that accepts user input and
converts temperatures between Celsius and Fahrenheit. You will handle various exceptions that might arise during the conversion process.

Instructions:

Write a main function that:
a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit),
separated by a space (e.g., "25 C" or "77 F").

b. Splits the input string into a temperature value and its unit.

c. Tries to convert the input temperature to its opposite unit using the appropriate function (e.g., if the user enters a Celsius temperature, convert it to Fahrenheit).
d. Handles the following exceptions: 
- ValueError: If the user enters an invalid temperature value, display an error message and prompt the user to try again. 
- TypeError: If the user enters an invalid unit, display an error message and prompt the user to try again. e. If the conversion is successful, print the converted temperature and its unit.

Call the main function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.'''


#Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and 
# returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return str(round(fahrenheit,2))

#Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and
# returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return str(round(celsius,2))

def split_phrase(phrase:str):
    pass


def main_function():
    while True:
        try:
            user_input= input('Enter a temperature and its unit (e.g., "25 C" or "77 F"):')
            updated_input=user_input.replace(" ","")
        
            number= updated_input[:-1]
            unit= updated_input[-1]

            
            if number.isdigit():
                if unit.upper() == "F":
                    result_convert_toCelsius= fahrenheit_to_celsius(int(number))
                    print(f"Temperature in Celsius: {result_convert_toCelsius} C\n")
                    break
                elif unit.upper() == "C":
                    result_convert_toFahrenhait=celsius_to_fahrenheit(int(number))
                    print(f"Temperature in Fahrenheit: {result_convert_toFahrenhait} F\n")
                    break
                else:
                    raise TypeError
                
            else:
                raise ValueError
        except TypeError:
             print(("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.\n"))
             continue
        except ValueError:
            print("You must provide a valid temperature value")
            continue
        else:
            break

main_function()
    
