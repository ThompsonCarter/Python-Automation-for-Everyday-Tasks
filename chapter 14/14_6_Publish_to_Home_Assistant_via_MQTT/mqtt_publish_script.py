
import paho.mqtt.publish as publish, json, time, board, adafruit_dht
dht = adafruit_dht.DHT22(board.D24, use_pulseio=False)
while True:
    payload = json.dumps({"temp": dht.temperature, "hum": dht.humidity})
    publish.single("home/sensors/dht22", payload, hostname="localhost")
    time.sleep(60)
