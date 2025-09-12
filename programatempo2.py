segt = 86400

min = segt//60
segf =segt%60

print(segf)

minf = min%60
hora = min//60

print(minf)

horaf = hora%24
dia = hora//24

print(segt,"segundos equivale a:",dia,"dias",horaf,"horas",minf,"minutos e",segf,"segundos")
