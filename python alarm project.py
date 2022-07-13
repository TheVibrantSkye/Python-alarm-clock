from datetime import date
from datetime import datetime


def main():
    print("Hi, welcome to my python alarm! \n")
    user_time_type()
    if user_time_type == 12:
        print("Yes!")
    else:
        print("no!")


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
                    break

                elif user_time_type_confirmation == "n":
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")


def twelve_hour_clock():
    if user_time_type == 12:
        print(now.strftime("It is currently %I:%M:%S PM EST"))


def twenty_four_hour_clock():
    if user_time_type == 24:
        print(now.strftime("It is currently %H:%M:%S"))


today = date.today()
d2 = today.strftime("Today's date is %B %d, %Y")
print(d2)

now = datetime.now()
time_test_12_hour = now.strftime("It is currently %I:%M:%S PM EST")
print(time_test_12_hour)

time_test_24_hour = now.strftime("It is currently %H:%M:%S")
print(time_test_24_hour)

if __name__ == "__main__":
    main()