dias = int(input('por quantos dias você alugou?'))
km = float(input('quantos kilometros você rodou?'))
preço = (dias*60) + (km*0.15)
print('o total a pagar é {}'.format(preço))
