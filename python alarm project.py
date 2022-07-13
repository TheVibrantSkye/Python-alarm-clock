from datetime import date
from datetime import datetime
import time
import threading


def main():
    print("Hi, welcome to my python alarm! \n")
    sx = user_time_type()
    while True:
        if sx == 12:
            localtime = time.localtime()
            result = time.strftime("\nIt is currently %I:%M:%S %p EST", localtime) # noqa
            print(result)
            time.sleep(60)
        else:
            result = time.strftime("\nIt is currently %H:%M:%S", localtime)
            print(result)
            time.sleep(60)


def user_time_type():
    '''This function is designed purely to get the time format a user wants,
    while also containing built-in input validation
    so I don't have to write it in main.'''
    placeholder_state = True
    while placeholder_state == True: # noqa
        user_time_type_choice = input("Would you like the clock to be in 12 hour or 24 hour format? \n\n") # noqa

        if user_time_type_choice == "12":
            while True:
                user_time_type_confirmation = input("Is 12 hour format correct? y/n \n") # noqa

                if user_time_type_confirmation == "y":
                    print("\n12 hour format selected!")
                    placeholder_state = False
                    user_time_selection = 12
                    return user_time_selection

                elif user_time_type_confirmation == "n":
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")

        elif user_time_type_choice == "24":
            while True:
                user_time_type_confirmation = input("Is 24 hour format okay? y/n \n") # noqa

                if user_time_type_confirmation == "y":
                    print("\n24 hour format selected!")
                    placeholder_state = False
                    user_time_selection = 24
                    return user_time_selection

                elif user_time_type_confirmation == "n":
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")


today = date.today()
now = datetime.now()

if __name__ == "__main__":
    main()
