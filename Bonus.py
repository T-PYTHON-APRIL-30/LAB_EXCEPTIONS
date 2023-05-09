def celsius_to_fahrenheit(celsius) -> list:
    temp_to_fahrenheit = (celsius * 9/5) + 32

    return (f"temperature in fahrenheit is:{temp_to_fahrenheit}")

print(celsius_to_fahrenheit(float(input("Enter a temperature in celsius:"))))

def fahrenheit_to_celsius(fahrenheit) -> list:
    temp_to_celsius = (fahrenheit - 32) * 5/9

    return (f"temperature in celsius is:{temp_to_celsius}")

print(fahrenheit_to_celsius(float(input("Enter a temperature in fahrenheit:"))))