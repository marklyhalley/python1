dia = 1
hora = 3
min = 46
seg1 = 40

hora = hora+dia*24
print (hora)
min =min+hora*60
print (min)
seg=seg1+60*min
print(seg)
print ("O resultado em segundos é", seg)
segundostotais1=seg
hora= seg//(60*60)
print('seg',seg)
resthora = seg%(60*60)
print('hr',hora)
print('rest',resthora)
min = resthora//60
restmin= resthora%60
print(min)
print(restmin)
print(segundostotais1, "são",hora,"horas",min,"Minutos e",restmin,"segundos")
dia=hora//24
restdia=hora%24

print(segundostotais1, "são",dia,"dias",restdia,"horas",min,"Minutos e",restmin,"segundos")


