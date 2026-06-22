import time
import board
import adafruit_dht
dht_sensor = adafruit_dht.DHT11(board.D4)
f = open("log.txt", 'w')
while True:
	try: 
		nhiet_do = dht_sensor.temperature
		do_am = dht_sensor.humidity
		if nhiet_do is not None and do_am is not None:
			print(f"Nhiet do: {nhiet_do:.1f}C | Do am: {do_am:.1f}%")
			data = f"
			f.write(data)
			time.sleep(1.0) 
	except RuntimeError: 
			time.sleep(2.0) 
			continue
	except Exception as error: 
			dht_sensor.exit()
			raise error
		
	
	
