import math
hoekgraden =75
lengte =10
hoekrad = (math.pi * hoekgraden) / 180

hoogte = lengte * math.sin(hoekrad)

print(hoogte)