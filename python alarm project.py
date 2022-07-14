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
                user_time_type_confirmation = input("Is 12 hour format correct? y/n \n").lower() # noqa

                if user_time_type_confirmation == "y".lower():
                    print("\n12 hour format selected!")
                    placeholder_state = False
                    user_time_selection = 12
                    return user_time_selection

                elif user_time_type_confirmation == "n".lower():
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")

        elif user_time_type_choice == "24":
            while True:
                user_time_type_confirmation = input("Is 24 hour format okay? y/n \n").lower() # noqa

                if user_time_type_confirmation == "y".lower():
                    print("\n24 hour format selected!")
                    placeholder_state = False
                    user_time_selection = 24
                    return user_time_selection

                elif user_time_type_confirmation == "n".lower():
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")


def alarm_timer():
    '''The purpose of this is to take the time in minutes until the user
    wants the alarm to go off. For example alarm_timer() 15,
    so 15 minutes then have the alarm go off'''
    alarm_duration = int(input("How many minutes before the alarm?\n"))
    # Python handles sleep in seconds, need to make time conversion.
    alarm_duration_fixed = (alarm_duration * 60)
    print(f"I will wait for {alarm_duration} minute(s)")
    # Figure out event.wait and how to use wait, because wait is better than sleep. # noqa
    event.wait(alarm_duration_fixed)
    print("Ding ding ding! Alarm!")
    pass


today = date.today()
now = datetime.now()
event = threading.Event()
alarm_timer()
# if __name__ == "__main__":
#    main()
