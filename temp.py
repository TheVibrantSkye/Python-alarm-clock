import time


def alarm_timer():
    '''The purpose of this is to take the time in minutes until the user
    wants the alarm to go off. For example alarm_timer() 15,
    so 15 minutes then have the alarm go off'''
    time_placeholder_state = True
    while time_placeholder_state == True: # noqa
        alarm_duration = input("How many minutes before the alarm?\n")

        user_quit(alarm_duration)

        try:
            if alarm_duration == "exit":
                print("The alarm will now exit.")
                break
            alarm_duration_fixed = int(alarm_duration)
            alarm_duration_fixed = (alarm_duration_fixed * 60)
            print(f"I will wait for {alarm_duration} minute(s)")
            time.sleep(alarm_duration_fixed)
            print("Ding ding ding! Alarm!")
        except Exception:
            print("There was an error somewhere!")
            pass
            print(f"I will wait for {alarm_duration} minute(s)")
            time.sleep(alarm_duration_fixed)
            print("Ding ding ding! Alarm!")


def user_quit(user_input):
    if user_input == "quit":
        print("The program will now quit. Thank you!!")
        quit()


alarm_timer()
