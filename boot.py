import machine, neopixel
import time

LED_POWER = Pin(19, mode = Pin.OUT, value = 1)

np = neopixel.NeoPixel(machine.Pin(18), 1)

while True:
  np[0] = (255,255,255)
  np.write()
  time.sleep(1)
  np[0] = (0,0,0)
  np.write()
  time.sleep(1)
