import math
#Ejecicio de Mecánica de fluidos
#Caso de estudio:
"""Determinar el ángulo que la superficie libre del agua forma con la horizontal 
   cuando viaja en un recipiente colocado sobre un remolque que se mueve sobre 
   una carretera empinada."""

#Unidades
#Aceleración [m/s^2]
#Ángulos [°]
#Aceleración de la gravedad [m/s^2]

#Declaración de Variables
flag=0
while flag==0:
 a=int(input('Ingrese el valor de la aceleración del remolque en [m/s^2]: ' ))
 alfa=int(input('Ingrese el valor del ángulo de empinación de la carretera en grados: ' ))
 g=9.81; 
 if  a>0 and 0<alfa<90:
 
   flag=1 

#Cálculo de las componentes de la aceleración en el eje x, y
   a_x=a*math.cos(math.radians(alfa))
   a_z=a*math.sin(math.radians(alfa))
#Cálculo del ángulo que la superficie libre del agua forma con la horizontal
   gamma=math.degrees((math.atan(a_x/(g+a_z))))
#Resultado
   print('El ángulo que forma la superficie del agua con la horizontal en grados es: ')
   print(gamma)

 else:
  print()   
  print('Digite una aceleración positiva y un ángulo de inclinacion mayor a 0 y menor a 90 grados')

 

