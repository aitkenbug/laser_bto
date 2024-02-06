import ugit
import machine, neopixel
import time

LED_POWER = machine.Pin(17, mode = machine.Pin.OUT, value = 1)

np = neopixel.NeoPixel(machine.Pin(18), 1)

#Start pulling from the repository


np[0] = (0,0,255)
np.write()
time.sleep(1)
np[0] = (0,0,0)
np.write()
time.sleep(0.5)
np[0] = (0,255,0)
np.write()

ugit.pull_all()

np[0] = (255,115,0)
np.write()
time.sleep(0.5)
np[0] = (0,0,0)
np.write()
time.sleep(0.2)
np[0] = (255,115,0)
np.write()
time.sleep(0.2)
np[0] = (0,0,0)
np.write()
time.sleep(0.2)
np[0] = (255,115,0)
np.write()
time.sleep(0.2)
np[0] = (0,0,0)
np.write()