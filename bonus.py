def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        answer=input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
        list1=answer.split(" ",1)
        try:
            temp_value=float(list1[0])
            unit=list1[1]
            if unit=="C":
                print("Temperature in Fahrenheit: ",celsius_to_fahrenheit(round(temp_value,2)))
                break
            elif unit=="F":
                print("Temperature in Celsius: ",fahrenheit_to_celsius(round(temp_value,2)))
                break
            else:
                raise TypeError()
        except ValueError:
            print("this is invalid number please try again,or don't start with whiteSpace ,or check the syntax")
            main()
        except TypeError:
            print("this is invalid unit please try use 'C' for Celsius or 'F' for Fahrenheit.")
            main()
        




main()

            

      

       




    
