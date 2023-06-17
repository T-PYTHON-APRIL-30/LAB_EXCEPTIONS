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
def celsius_to_fahrenheit(celsius : str):
    celsius = int(celsius)
    return (celsius * 9/5) + 32, "F"

def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = int(fahrenheit)
    return (fahrenheit - 32) * 5/9, "C"

def main():
    temperature : tuple = tuple(input("please enter a temperature and its unit as (25 C or 77 F): ").split(" "))
    tempValue, tempUnit = temperature
    print(tempValue, tempUnit)
    try:

        if tempUnit.upper() == "C":
            tempValue, tempUnit = celsius_to_fahrenheit(tempValue)
        elif tempUnit.upper() == "F":
            tempValue, tempUnit = fahrenheit_to_celsius(tempValue)
        else:
            raise TypeError
        print(tempValue, tempUnit)
    except ValueError:
        print("the input invalid please enter number")
    except TypeError:
        print("the unit is uncorrect")

