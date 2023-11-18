import time

import math

from kaspersmicrobit import KaspersMicrobit

def accelerometer_data(data: ()):
    print(f"Accelerometer data: {data}")

def pressed(button):
    print(f"button {button} pressed")

def get_roll(x,y,z):
  return  math.atan(x/math.sqrt(math.pow(y,2) + math.pow(z,2))) * -180 / math.pi
def get_pitch(x,y,z):
   return math.atan(y/math.sqrt(math.pow(x,2) + math.pow(z,2))) *  180 / math.pi
def get_pitch_roll(microbit):
  accel = microbit.accelerometer.read()
  x = accel.x
  y = accel.y
  z = accel.z
  return [ get_pitch(x,y,z) , get_roll(x,y,z) ] 

with KaspersMicrobit.find_one_microbit() as microbit:
    # read the current accelerometer data / lees de huidige accelerometer gegevens
    for i in range(10):
      '''
        accel = microbit.accelerometer.read()
        x = accel.x
        y = accel.y
        z = accel.z
        pitch = get_pitch(x,y,z)
        roll = get_roll(x,y,z)
        print(f"Current pitch: {roll}")
        #print(f"Current roll: {roll}")
      '''
      res = get_pitch_roll(microbit)
      print(f"{res}")
      #microbit.buttons.on_button_a(press=pressed)
      a = microbit.buttons.read_button_a()
      b = microbit.buttons.read_button_b()
      m = "No button"
      if a > 0 and b == 0:
        m = "Go up"
      if a == 0 and b > 0:
        m = "Go down"
      if a > 0 and b > 0:
        m = "Stop Flying"

      print(f"{m}")

      time.sleep(2)
    # check how often accelerometer updates will occur if you listen to them with notify
    # / lees hoe vaak accelerometer updates doorgestuurd worden wanneer je er naar luistert met notify
    #print(f"Current period: {microbit.accelerometer.read_period()}")

    # listen for accelerometer data updates / luister naar updates van de accelerometer gegevens
    #microbit.accelerometer.notify(accelerometer_data)

    #time.sleep(5)

    # change the update interval / pas het update interval aan
    #print("Now slow down updates to 160 milliseconds")
    #microbit.accelerometer.set_period(160)

    #print(f"Accelerometer updates will now occur every {microbit.accelerometer.read_period()} milliseconds")

    #time.sleep(5)