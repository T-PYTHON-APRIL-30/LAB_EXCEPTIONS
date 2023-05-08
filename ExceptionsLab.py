'''Below you have a code that raises an exception , using what you learned do the following:
*Find what type of exception is raised.
*Handle the exception in try..except
*If operation successful , print "the operation is successful"
if operation fails, handle the specific exception that is raised , and print a relevant message.
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)'''

def additoin(x, y):
    x = 10
    y = 20

    try:
        print("Addition:", x + b)
    
    except Exception as e:
        print("something went wrong. Try again later.")
        print("save to file:", e)

    
    else:
        
        print('the operation is successful')



additoin(10, 20)