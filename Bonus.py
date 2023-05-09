'''Temperature Converter
Description: In this exercise, you will practice using Python exceptions by creating a simple temperature converter that accepts
 user input and converts temperatures between Celsius and Fahrenheit.
You will handle various exceptions that might arise during the conversion process.

Instructions:
*Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument and returns the equivalent
temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.

*Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument and returns 
the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.

Write a main function that: 
*a. Prompts the user for input, asking them to enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit),
 separated by a space (e.g., "25 C" or "77 F"). 
*b. Splits the input string into a temperature value and its unit. 
*c. Tries to convert the input temperature to its opposite unit using the appropriate function 
(e.g., if the user enters a Celsius temperature, convert it to Fahrenheit). 
*d. Handles the following exceptions: - ValueError: If the user enters an invalid temperature value,
 display an error message and prompt the user to try again. 
 *- TypeError: If the user enters an invalid unit, display an error message and prompt the user to try again. 
 e. If the conversion is successful, print the converted temperature and its unit.

Call the main function to run the program. The user should be able to enter temperatures repeatedly until they enter a valid input.

Example Output:

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100 F
Temperature in Celsius: 37.78 C

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 50 C
Temperature in Fahrenheit: 122.0 F

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 25 X
Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.

Enter a temperature and its unit (e.g., "25 C" or "77 F"): 100.5 F
Temperature in Celsius: 38.06 C'''

def celsius_to_fahrenheit(cel:float)->float:
    fahrenheit = (cel * 9/5) + 32
    return round(fahrenheit,2)

def fahrenheit_to_celsius(fahr:float)->float:
    celsius = (fahr - 32) * 5/9
    return round(celsius,2)

def main():

    '''ValueError: If the user enters an invalid temperature value,
    display an error message and prompt the user to try again. '''
    try:
        temp = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"):')
        print()

        #Splits the input string into a temperature value and its unit
        unit = temp[-1].upper()
        temp_value = float(temp[0:temp.find(' ')])

        checkUnit(unit)

        #Tries to convert the input temperature to its opposite unit using the appropriate function
        if unit == 'C':
            print(f'Temperature in Fahrenheit:{celsius_to_fahrenheit(temp_value)} F')
            print()
        elif unit == 'F':
            print(f'Temperature in Celsius:{fahrenheit_to_celsius(temp_value)} C')
            print()

    except ValueError:
        print('You entered an invalid value!! Please enter the temprature value as an integer number!')
        print()
        main()

    except TypeError as e:
        print(e)
        print()
        main()

    else:

         print('the conversion is successful')

def  checkUnit(char:str):
    if char != 'C' and char != 'F':
        raise TypeError('You entered an invalid unit!! Please enter the temprature unit as C or c for celsius , F or f for Fahrenheit !')

main()

    


