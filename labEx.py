#Q1
def addtoin(x,y):
    try:
        x = 10
        y = 20
        print("Addtion:", x + b)
    except NameError:
        print("there are some variable that are not defined, please revise")
    else:
        print("opeeration is successful")
    finally:
        print("...")

addtoin(10,20)

#Q2



def celsius_to_farenheit(celsius) -> float:
    farenheit = (float(celsius) * 9/5) + 32
    return farenheit

def farenheit_to_celsius(farenheit) -> float:
    celsius = float((farenheit - 32) * 5/9)
    return celsius

'''
these are testing number for the float with decimal area 
stri = "101.1F"    
modInn = (float(''.join(filter(lambda stri:stri.isdigit(),stri))))
print(modInn)
print(farenheit_to_celsius(modInn))
print(type(modInn))


num = 100.5
nums = "100.5"
newn = float(nums)
print(farenheit_to_celsius(newn))
'''

def main():
    flag = True
    while flag:
        try:
            UserInput = input("Please enter your tempature for conversion: ")
            if not (UserInput.endswith("F")  or UserInput.endswith("C")):
                raise TypeError("Please enter either C or F....")
            modIn = float(''.join(filter(lambda UserInput:UserInput.isdigit(), UserInput)))
            if UserInput.endswith("F"):
                print(f"The conversion between {UserInput} to celsius is :", round(farenheit_to_celsius(modIn),3),"C")
                flag = False
            if UserInput.endswith("C"):
                print(f"The conversion from {UserInput} to farenheit is: ", round(celsius_to_farenheit(modIn),3),"F")
                flag = False
        except ValueError:
            print("please enter a valid number for conversion")
        except TypeError:
             print(("Please enter either C or F...."))
        else:   
            print("Operation success here's the origianl input: ", UserInput)
        finally:
            print("---")

main()

