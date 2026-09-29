# coleta para dados alfabéticos
n = input(' digite algo')
print(' qual é o tipo do valor que eu digitei?', type(n))
print(' o valor que eu digitei é numerico', n.isnumeric())
print(' o valor que eu digitei é alfabetico?', n.isalpha())
print('o valor que eu digitei é capitalizado?', n.istitle())
print(' o valor que eu digitei é maiúsculo?', n.isupper())

# coleta para dados numericos
if n.isnumeric():
    n = int(num)
    a = num - 1
    s = num + 1
    d = num // 2
    p = num ** 2
    r = num ** (1/2)
    print(' o antecessor do valor {} é o digito {}  e o sucessor é {}' .format(num, a, s))
    print(' o divisor é {}, apotência é {} e raiz quadrada é{}' .format(d, p, r))

# se a caso o cliente não digitar um numero
else:
    print('você não digitou um numero')

