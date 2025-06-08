
from lifxlan import LifxLAN
bulb = LifxLAN().get_lights()[0]
bulb.set_color([35000, 65535, 65535, 3500, 400])
