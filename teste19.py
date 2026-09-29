import random
n1 = input('digite alguém:')
n2 = input('digite alguém:')
n3 = input('digite alguém:')
n4 = input('digite alguém:')
lista = [n1, n2, n3, n4]
escolhido =  random.choice(lista)
print('o escolhido foi{}'.format(escolhido))
