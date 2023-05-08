'''
Find what type of exception is raised.
Hanlde the exception in try..except
If operation successful , print "the operation is successful"
if operation fails, handle the specific exception that is raised , and print a relevant message.
'''

def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError as e:
        print("An error occurred:", e)
    else:
        print("The operation is successful")

additoin(10, 30)
