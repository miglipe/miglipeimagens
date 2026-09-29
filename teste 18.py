import math
ângulo = float(input('qual é o angulo?'))
seno = math.sin(math.radians(ângulo))
print('o seno do angulo de {}º é {:.2f}'.format(ângulo, seno))
co = math.cos(ângulo)
print('o seu cosceno é {:.2f}'.format(co))
ta = math.tan(math.radians(ângulo))
print(' e a sua tangente é {:.2f}'.format(ta))

