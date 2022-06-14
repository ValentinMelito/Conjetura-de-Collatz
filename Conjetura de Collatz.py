# Conjetura de Collatz
# Se agarra un numero entero(positivo) y:
# Si el número es par, se divide entre 2.
# Si el número es impar, se multiplica por 3 y se suma 1.
# La conjetura dice que siempre alcanzaremos el 1.


vueltas = 0
resultado =int (input("ingrese un numero: ") )
resto=resultado
pasos=[resultado]
while (resultado > 1):
  resto=resultado
  #print ("pasos ", resto)
  #verifico si el numero es par o impar en base a si hay resto si lo divido por 2
  if (resto % 2 > 0):
    resultado = (resultado *3)+1
    #print ("pasos que vienen de un impar: ", resultado)
    vueltas+=1
    pasos.append(resultado)
  #si es par pasa directo a la division 
  resultado = int(resultado/2)
  pasos.append(resultado)
  vueltas+=1 
print("se siguio el siguiente orden: ",pasos)
print ("dio: ", vueltas, " vueltas")
