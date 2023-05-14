def addition(x, y):
    try:
        result = x + b
        print("Addition:", result)
        print("The operation is successful")
    except NameError:
        print("Error: Invalid variable name. Please check your code.")
        print("Operation failed.")


addition(10, 20)
