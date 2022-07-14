import threading
import time

start = time.perf_counter()
finish = time.perf_counter()


def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done sleeping")


def ask_question():
    print("Asking a question")
    test_input = input("How are you today?")
    print(f"Ah, so you are doing {test_input}.. I see")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
# t3 = threading.Thread(target=ask_question)

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()


# t3.start()
# t3.join()

print(f"Finished in {round(finish-start, 2)} second(s)")
