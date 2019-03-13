import car
print(car.build_car('subaru','outback',color='blue', tow_package=True))

from car import build_car
print(build_car('subaru','outback',color='blue', tow_package=True))

from car import build_car as bc
print(bc('subaru','outback',color='blue', tow_package=True))

import car as c
print(c.build_car('subaru','outback',color='blue', tow_package=True))

from car import *
print(build_car('subaru','outback',color='blue', tow_package=True))
