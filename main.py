#-------------- LAB_EXCEPTIONS --------------
print("----- LAB_EXCEPTIONS -----")
def additoin(x, y):
    x = 10
    y = 20
    try:
        print("Addition:", x + y)
    except NameError:
        print("There is an invalid entry!!!")
    finally:
        print("The operation is successful")

additoin(10, 20)