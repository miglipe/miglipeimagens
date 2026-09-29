salario = float(input('qual o seu salario'))
reajuste = salario + (salario * 15/100)
print('quem ganha RS{} e teve reajuste de 15% vai receber RS{:.2f}'.format(salario, reajuste))
