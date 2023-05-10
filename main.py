#-------------- LAB_EXCEPTIONS --------------
print("----- LAB_EXCEPTIONS -----")
def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + b )
    except NameError:
        print("There is an invalid entry!!!")
    finally:
        print("The operation is successful")

additoin(10, 20)

#-------------- Bonus --------------


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9