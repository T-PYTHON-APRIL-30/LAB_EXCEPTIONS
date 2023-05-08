def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9


def main():
    while True:
        try:
            temperature_value, unit = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ').split()
            
            unit_convert = unit.upper()
            value_convert = float(temperature_value)

            if unit_convert == "C" :
                converted_temperature = celsius_to_fahrenheit(value_convert)
                print(f"Temperature in Fahrenheit: {round(converted_temperature, 2)} F")
                break
            elif unit_convert == "F":
                converted_temperature = fahrenheit_to_celsius(value_convert)
                print(f"Temperature in Celsius: {round(converted_temperature, 2)} C")
                break
            else:
                raise TypeError
        except ValueError:
            print("Invalid value. Please try again...\n")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.\n")


main()