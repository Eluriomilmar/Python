from time import sleep

hours = -1
minutes = -1
seconds = -1
while hours < 0:
    hours = int(input("How many hours should the countdown last: "))
while minutes < 0:
    minutes = int(input("How many minutes should the countdown last: "))
while seconds < 0:
    seconds = int(input("How many seconds should the countdown last: "))

while seconds > 0 or minutes > 0 or hours > 0:
    if seconds == 0:
        if minutes == 0:
            hours -= 1
            minutes += 59
            seconds += 60
        else:
            minutes -= 1
            seconds += 60
    seconds -= 1
    sleep(1)
    print(f"There's {hours} hours, {minutes} minutes and {seconds} seconds left")

print("Countdown ended")

