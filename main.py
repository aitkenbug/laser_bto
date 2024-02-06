import machine, neopixel
import time
import network
from secrets import secrets


sta_if = network.WLAN(network.AP_IF)
sta_if.active(True)
sta_if.connect(secrets['ssid'], secrets['password'])
while ap.active() == False:
  pass



LED_POWER = machine.Pin(17, mode = machine.Pin.OUT, value = 1)

np = neopixel.NeoPixel(machine.Pin(18), 1)

while True:
  np[0] = (255,255,255)
  np.write()
  time.sleep(1)
  np[0] = (0,0,0)
  np.write()
  time.sleep(1)
