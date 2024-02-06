import machine, neopixel
import time


LED_POWER = machine.Pin(17, mode = machine.Pin.OUT, value = 1)

np = neopixel.NeoPixel(machine.Pin(18), 1)

while True:
  np[0] = (255,255,255)
  np.write()
  time.sleep(0.3)
  np[0] = (0,0,0)
  np.write()
  time.sleep(0.3)
