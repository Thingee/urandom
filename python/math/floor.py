import math
import time

value = int(10)
unit = 60
capacity = unit
now = time.time()
water_level = 0
request_value = float(capacity) / float(value)
last_request = None

#-----------------------------------

if last_request is None:
    last_request = now

leak_value = now - last_request

water_level -= leak_value
water_level = max(water_level, 0)
water_level += request_value

difference = water_level - capacity

last_request = now

if difference > 0:
    water_level -= request_value
    next_request = now + difference

cap = capacity
water = water_level
val = value

remaining = math.floor(((cap - water) / cap) * val)
print remaining
