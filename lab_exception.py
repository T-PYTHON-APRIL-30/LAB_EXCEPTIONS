# LAB_EXCEPTIONS

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError:
    print("the variable used is not defind try to check if you have the right variable")
else:
    print("the operation is successful")


# Bonus
# Temperature Converter


def celsius_to_fahrenheit(celsius: float):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    print()
    temperature_value, unit = input(
        "Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"): ").split(' ')
    float_value = float(temperature_value)
    while unit != "C" and unit != "F":
        print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        temperature_value, unit = input(
            "Enter a temperature and its unit (e.g., \"25 C\" or \"77 F\"): ").split(' ')
        float_value = float(temperature_value)

    else:

        if unit == "C":
            print(
                f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(float_value),2)} F")

        if unit == "F":
            print(
                f"Temperature in Celsius: {round(fahrenheit_to_celsius(float_value),2)} C")
            print(temperature_value, unit)


try:
    main()
except ValueError:
    print("invalid temperature value")
    main()
