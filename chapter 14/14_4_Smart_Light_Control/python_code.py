
from phue import Bridge
b = Bridge('192.168.1.50')   # replace with bridge IP
b.connect()                  # press Hue bridge button once
lights = b.lights
print([l.name for l in lights])

def good_morning():
    for l in lights:
        l.brightness = 254
        l.hue = 8000       # warm
        l.saturation = 130
