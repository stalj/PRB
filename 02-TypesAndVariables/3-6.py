import math
h = float(input('Enter the height of observer while standing on the beach (m): '))
h1 = float(input('Enter the height of observer while looking out of a hotel window located by the sea (m): '))
d = 3.757 * math.sqrt(h)
d1 = 3.757 * math.sqrt(h1)
print('Distance to horizon1 (m): ', d)
print('Distance to horizon2 (km): ', d1)