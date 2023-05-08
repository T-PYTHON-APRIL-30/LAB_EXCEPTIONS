'''
Find what type of exception is raised.
Hanlde the exception in try..except
If operation successful , print "the operation is successful"
if operation fails, handle the specific exception that is raised
 , and print a relevant message.
'''
try:
    def additoin(x, y):
        x = 10
        y = 20
        print("Addition:", x + b)


    additoin(10, 20)
except NameError:
    print("The operation is unsuccessful, check your code numbers in lane 15.")
else:
    print("The operation is successful")

