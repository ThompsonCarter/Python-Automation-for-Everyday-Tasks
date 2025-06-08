
# 1. Flash Raspberry Pi OS Lite with Raspberry Pi Imager
# 2. Enable SSH: add empty file named 'ssh' to boot partition
# 3. Boot, then:
sudo raspi-config  # set locale + enable I2C if needed
sudo apt update && sudo apt install -y python3-pip
pip install --upgrade pip adafruit-circuitpython-dht paho-mqtt requests
        