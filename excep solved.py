#Below you have a code that raises an exception , using what you learned do the following:
#Find what type of exception is raised.
#Hanlde the exception in try..except
#If operation successful , print "the operation is successful"
#if operation fails, handle the specific exception that is raised , and print a relevant message.
#def additoin(x, y):
# x = 10 y = 20
#print("Addition:", x + b) additoin(10, 20)

def addition(x, y):
    x = 10 
    y = 20
    print("Addition:", x+y)

try:
    addition(10, 20)
    print("The operation is successful.")
except NameError:
    print("variable is not defined.")





#"Bonus"
#Temperature Converter 
#Description: In this exercise, you will practice using Python exceptions by creating a simple temperature 
# converter that accepts user input 
# and converts temperatures between Celsius and Fahrenheit. 
# You will handle various exceptions that might arise during the conversion process.

#Instructions:
#Write a function celsius_to_fahrenheit(celsius) that takes a Celsius temperature as an argument
#  and returns the equivalent temperature in Fahrenheit. Use the formula fahrenheit = (celsius * 9/5) + 32.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit

#Write a function fahrenheit_to_celsius(fahrenheit) that takes a Fahrenheit temperature as an argument 
# and returns the equivalent temperature in Celsius. Use the formula celsius = (fahrenheit - 32) * 5/9.

def fahrenheit_to_celsius(fahrenheit):
    celsiue = (fahrenheit - 32) * 5/9
    return celsius


#Write a main function that: a. Prompts the user for input, asking them to enter a temperature
# and its unit (either "C" for Celsius or "F" for Fahrenheit), separated by a space (e.g., "25 C" or "77 F"). b.
# Splits the input string into a temperature value and its unit. c. Tries to convert the input temperature to its 
# and prompt the user to try again. e. If the conversion is successful, print the converted temperature and its unit.

def main ():
    while True:
        try:
            input_str = input ("Enter a temperture and its unit "(e.g., '25C' or '77 F'):")
                               temp, unit = input_str.split()
                               temp = float(temp)
                               if unit == "C":
                               converd_temp = celsius_to_fahrenheit(temp)
                                       print(f"{temp} C is {converted_temp}F")
         elif unit == "F":
         converted_temp = fahrenheit_to_celsius(temp)
         print(f"{temp}F is converted_temp}C")
         else:
         raiseTypeError("Invalid unit Please enter 'C' or 'F'.")
         except ValueError:
         print("Invalid temperture value. please try again")
         except TypeError as e:
         print(e)
         else:
            break




#Call the main function to run the program. The user should be able to enter temperatures repeatedly
#  until they enter a valid input.

if__name__=="__main__":
   main ()