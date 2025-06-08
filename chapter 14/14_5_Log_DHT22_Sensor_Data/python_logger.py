
import board, adafruit_dht, csv, datetime as dt, time
dht = adafruit_dht.DHT22(board.D24, use_pulseio=False)

with open("/home/pi/dht_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    while True:
        try:
            t = dht.temperature
            h = dht.humidity
            now = dt.datetime.now().isoformat(timespec="seconds")
            writer.writerow([now, t, h])
            f.flush()
            print(now, t, h)
        except RuntimeError:
            pass  # sensor read glitch; ignore
        time.sleep(300)  # 5 min
