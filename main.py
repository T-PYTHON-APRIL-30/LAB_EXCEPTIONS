
# hanlde the exception in try..except 
# if successful: "the operation is successful".
# if fails: handle the specific exception and print a relevant message.

try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b)

    additoin(10, 20)

# find what type of exception is raised.
# NameError: name 'b' is not defined
except NameError:
    print("please define variable b")
else:
    print("the operation is successful")