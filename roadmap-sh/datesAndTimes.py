import datetime

date = datetime.date(2025, 1 ,2)
today = datetime.date.today()
time = datetime.datetime.now()

time = time.strftime("%H:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2025, 11, 14, 16, 30, 0)
current_datetime = datetime.datetime.now()
if current_datetime > target_datetime:
    print("Target date has passed!")
else:
    print("Target date has not passed!")