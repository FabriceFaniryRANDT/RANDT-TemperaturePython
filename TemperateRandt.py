print()
zone = input("Entrer le nom du région : ")
P = float(input("Precipitation = "))
T = float(input("Temperature = "))
print()

def Affichage(climat):
  print("==================================================\n\n")
  print('>>>',zone,'se trouve dans la',climat,'\n\t','- une température = ',T,'ºC','\n\t','- une précipitation = ',P,'mm . \n\n')
  print("==================================================\n")

if (T<10) & (P<500):
  climat = 'Zone extrêmement polaire'
  Affichage(climat)
  
elif (T<20) & (P<1000):
  climat = 'Zone polaire'
  Affichage(climat)
  
elif (T>20) & (P<1000):
  climat = 'Zone tempérée 1'
  Affichage(climat)
  
elif (T<20) & (P>1000):
  climat = 'Zone tempérée 2'
  Affichage(climat)
  
elif (T>20) & (P>1000):
  climat = 'Zone tropical chaud et pluvieux'
  Affichage(climat)
  
else:
  print('Les données entrées sont invalides ...')
  
  