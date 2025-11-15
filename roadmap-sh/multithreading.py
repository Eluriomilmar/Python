# multithreading = Used to perform multiple tasks concurrently (multitasking)
#               Good for I/O bound tasks like reading files of fetching data from APIs
#                threading.Thread(target=my_function)

import threading, time, random



def walk_dog(fname, sname):
    print(f"You start walking {fname} {sname}")
    time.sleep(random.randint(0,10))
    print(f"You finish walking {fname} {sname}")


def take_out_trash():
    print("You start taking out the trash")
    time.sleep(random.randint(0,10))
    print("You take out the trash")


def get_mail():
    print("You start looking at the mail")
    time.sleep(random.randint(0,10))
    print("You get the mail")

thread1 = threading.Thread(target=walk_dog, args=("Piolho", "Pimpolho"))
thread1.start()
thread2 = threading.Thread(target=take_out_trash)
thread2.start()
thread3 = threading.Thread(target=get_mail)
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("All chores are complete!")