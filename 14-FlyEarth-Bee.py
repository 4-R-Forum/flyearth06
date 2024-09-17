import sys
import datetime
import time
import math
#import selenium
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# import Kasper
from kaspersmicrobit import KaspersMicrobit
# Kasper mbit functions
def get_roll(x,y,z):
  return  math.atan(x/math.sqrt(math.pow(y,2) + math.pow(z,2))) * 180 / math.pi # +ve go right
def get_pitch(x,y,z):
   return math.atan(y/math.sqrt(math.pow(x,2) + math.pow(z,2))) * 180 / math.pi # +ve go up
def get_pitch_roll(microbit):
  accel = microbit.accelerometer.read()
  x = accel.x
  y = accel.y
  z = accel.z
  return [ get_pitch(x,y,z) , get_roll(x,y,z) ] 
# global variables
global cmd_string # commands from microbit via serial, 'buttonA/B,pitch,roll'
global port, button, pitch, roll, k, rk # for flying
global i, e, l, n, m # message for logging
global t1, t2 # thresholds for actions
i = 0 # set initial value
t1 = 20 # threshold 1
t2 = 40 # threshold 2

# create selenium objects
# $By = [OpenQA.Selenium.By]
driver = webdriver.Chrome()
# action accumulates keystrokes which are applied at the next perform()
# and the chain is emptied
action = ActionChains(driver)

# functions for keys
def kd(key):
  action.key_down(key)
def ku(key):
  action.key_up(key)
# variables for keys
ctrl = Keys.CONTROL
sh =   Keys.SHIFT
alt =  Keys.ALT
au =   Keys.ARROW_UP
ad =   Keys.ARROW_DOWN
al =   Keys.ARROW_LEFT
ar =   Keys.ARROW_RIGHT
pu =   Keys.PAGE_UP
pd =   Keys.PAGE_DOWN

# start Earth in Chrome
driver.get  ("https://earth.google.com/")
# Confirm you are ready to fly
# input("Click through New Look popup") # no longer needed
# press ctrl-i to select .kml file for starting point, from dialog
kd(ctrl)
action.send_keys("i")
ku(ctrl)
action.perform()
action.send_keys("O")
action.perform()

input("Press shift and arrow multiple times to show horizon at top of screen")
"""

#press shift arrow_down 28 times to start 3D view and show horizon at top of screen
kd(sh)
for i in range(28):
  kd(ad)
  ku(ad)
  action.perform()
ku(sh)
"""

with KaspersMicrobit.find_one_microbit() as microbit:
  i = 0
  l = datetime.datetime.now()

  run = True
  debug = False
  #test_cmds = ("0,0,0","0,30,0","0,30,-30","0,30,30","0,-30,0")
  #             level     up        left     right      down
  test = 0
  while run :
    try:
      if debug == False :
        # request new data from mbit
        res = get_pitch_roll(microbit)
        pitch = res[0]
        roll  = res[1]
        #microbit.buttons.on_button_a(press=pressed)
        a = microbit.buttons.read_button_a()
        b = microbit.buttons.read_button_b()
        button = 0
        if a > 0 and b == 0:
          button = 1 # look up
        if a == 0 and b > 0:
          button = -1 # look down
        if a == 1 and b == 1:
          button = 99 # stop Flying"
        cmd_string = f"{button},{pitch},{roll}" # simulates prior serial string
    except Exception as e:
      sys.stdout.write(str(e))
      break
    else:
      if button == 99:
        # Stop flying
        exit
      # start process
      m = ""
      i += 1
      n = datetime.datetime.now()
      e = n - l 
      l = n
    
    # start of bee control
    """
      Strategy:
      to minimize jerkiness keep keys down until pitch/roll changes
      this will fly fast until hover is reached, and all keys up
      each go comment will need appropriate key up and down
      roll takes priority, left right turn, supersedes pitch
      if no roll forward/back or up/down
    """
    # start of roll
    if roll > t2:
      # go up
      # go forward
      print("turn right, go right")
    elif roll > t1 :
        print("go right")
    elif roll < -t2 :
      # go down
      # go back
      print("turn left, go left")
    elif roll < -t1 :
      # go back
      print("go left")
    else :
      # hover
      print("no roll")
      # start of pitch
      if pitch > t2:
        # go up
        # go forward 1
        print("go up, forward")
      elif pitch > t1 :
          print("forward")
      elif pitch < -t2 :
        # go down
        # go back 1
        print("go down, back")
      elif pitch < -t1 :
        # go back 1
        print("back")
      else :
        # stay
        print("no forward/back")
      # end of pitch  
    time.sleep(1)
    # end of process
    # end of try get data from mbit
  # end of while loop
  input("Press Enter to stop flying")
  # end of flight
# end of microbit

