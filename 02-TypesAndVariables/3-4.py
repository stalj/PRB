###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = float(input('Enter speed in km/h: '))
#because 1 km = 1000 m and 1 h = 3600 s so 1 km/h = 1000/3600 m/s = 5/18 m/s
speed_ms = speed_kmh * (5/18)
print(speed_kmh, "km/h = ", speed_ms, "m/s")
