
from math import hypot
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente'))
h = hypot(co, ca)
print('o cateto adjacente é {} e o cateto oposto é {}, logo a hipotenuza é {:.2f}'.format(ca, co, h))
