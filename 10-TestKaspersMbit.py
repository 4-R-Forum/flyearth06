import time

from kaspersmicrobit import KaspersMicrobit

def accelerometer_data(data: ()):
    print(f"Accelerometer data: {data}")


with KaspersMicrobit.find_one_microbit() as microbit:
    # read the current accelerometer data / lees de huidige accelerometer gegevens
    print(f"Current accelerometer reading: {microbit.accelerometer.read()}")

    # check how often accelerometer updates will occur if you listen to them with notify
    # / lees hoe vaak accelerometer updates doorgestuurd worden wanneer je er naar luistert met notify
    print(f"Current period: {microbit.accelerometer.read_period()}")

    # listen for accelerometer data updates / luister naar updates van de accelerometer gegevens
    microbit.accelerometer.notify(accelerometer_data)

    time.sleep(5)

    # change the update interval / pas het update interval aan
    print("Now slow down updates to 160 milliseconds")
    microbit.accelerometer.set_period(160)

    print(f"Accelerometer updates will now occur every {microbit.accelerometer.read_period()} milliseconds")

    time.sleep(5)