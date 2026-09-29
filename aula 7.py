# aqui é onde você digita um valor
n = (input('digite um valor:'))

# resultado alfabetico
print('o valor que eu digitei  é do tipo', type(n))
print(' o valor que eu digitei é numerico?', n.isnumeric())
print('o valor que eu digitei é alfabetico?', n.isalpha())
print(' o valor que eu digitei é maiúculo?', n.isupper())
print('o valor que eu digitei é minúsculo', n.islower())

#numerais
if n.isnumeric():
    num = int(n)
    a = num - 1
    s = num + 1
    print(' o antecessor de {} é {}, e o sucessor é {}'.format(n, a, s))
else:
    print('não foi possivel calcular o antecessor e sucessor do que você digitou')
