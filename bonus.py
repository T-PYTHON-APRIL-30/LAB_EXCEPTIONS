
# Temperature Converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
            temperature, unit = user_input.split()
            temperature = float(temperature)
            if unit.upper() == "C":
                convert = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {convert} F")
            elif unit.upper() == "F":
                convert = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {convert} C")
            else:
                raise TypeError
            break
        except ValueError:
            print("invalid temperature, please try again")
        except TypeError:
            print("invalid unit, please try again")

# call the main to start
main()