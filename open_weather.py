
import pyowm

owm = pyowm.OWM('d8e83ef8bead56b56c530e10fbfb15ac')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

w.get_wind()
w.get_humidity()


print(w.get_wind())
print(w.get_humidity())
