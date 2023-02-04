from sys import stdin
# Sabrina 8965083
#punto1
def verificarDiagonales(matriz):
  resultado = True
  for i in range(len(matriz)): #ciclo que recorre la matriz
    if len(matriz[i])%2 == 0: #si la matriz es par puedo revisar todos sin problema
      if matriz[i][i] != matriz[i][-(i+1)]:
        resultado = False
    else: #si la matriz es impar debo de ignorar el numero de en medio ya que es el mismo en la diagonal principal y secundaria
      if i != (len(matriz[i])//2)+1:
        if matriz[i][i] != matriz[i][-(i+1)]:
          resultado = False
  return resultado
#mat = [[11, 23, 76, 34, 11],
#[14, 30, 92, 30, 101],
#[12, 45, 58, 92, 22],
#[74, 56, 49, 56, 100],
#[99, 5, 28, 47, 99]]
#verificarDiagonales(mat)
  
#punto2
#mismo analisis que en el punto anterior
def esCapicua(lista):
  resultado = True
  for i in range(len(lista)):
    if len(lista)%2 == 0:
      if lista[i] != lista[-(i+1)]:
        resultado = False
    else:
      if i != (len(lista)//2)+1:
        if lista[i] != lista[-(i+1)]:
          resultado = False
  return resultado
#print(esCapicua([42, 12, 90, 90, 12, 42]))
#print(esCapicua([42, 12, 90, 90, 12, 45]))

#punto3
#a
def diferenciaListas(lista1, lista2):
  i = 0
  while i < len(lista1): #reviso cada uno de los elementos de la lista1
    if lista1[i] in lista2: #si hay un elemento en la lista 1 que tambien se encuentre en la lista 2
      lista2.remove(lista1[i]) # lo retiro de la lista 2 
      lista1.remove(lista1[i]) # lo retiro de la lista 1
      i -= 1
    i +=1
  return lista1
#listaA = [40, 10, 22, 12, 33, 33, 33]
#listaB = [41, 22, 31, 15, 13, 12, 33, 19]
#print(diferenciaListas(listaB, listaA))

#b
def lecturaEImpresion():
  casos = int(input("")) #leo numero de casos
  for i in range(casos): #separo las entradas en la cantidad de casos
    listaA = stdin.readline().strip().split() #guardo la primera entrada del caso
    listaB = stdin.readline().strip().split() #guardo la segunda entrada del caso
    listaA = listaA[1:] #ignoro el primer elemento
    listaB = listaB[1:] #ignoro el primer elemento
    resultado = diferenciaListas(listaA, listaB) #llamo a la funcion anterior
    for j in range(len(resultado)): #print de los datos obtenidos
      if j+1 == len(resultado):
        print(resultado[j])
      else:
        print(resultado[j], end =", ")
#lecturaEImpresion()
def mostrarPrimos(limite):
  listaPrimos = [] #lista donde guardaremos los primos encontrados
  listaPrimos2 = [] #lista donde guardaremos los primos cuya suma de sus digitos dan un primo
  for i in range(2,limite): #reviso cada numero dentro del rango
    if i == 2: #ignoro el 2 y lo añado de una a la lista de primos
      listaPrimos.append(i)
    else:
      esPrimo = True #bandera para saber si es primo un numero o no
      for j in listaPrimos: #reviso la lista de primos
        if i % j == 0: #reviso si es divisible entre los primos anteriores a el
          esPrimo = False #si es divisible por alguno significa que no es primo
      if esPrimo == True:
        listaPrimos.append(i)
  print("Numeros primos entre 1 y ", limite)
  for i in listaPrimos:
    print("--> ", i , ",")
  print("Numeros entre 1 y ", limite, " con suma de digitos con valor primo:")
  # a continuacion revisamos si los numeros tienen más de un digito, los que tienen solo un digito los añado a la lista primos2 y los que tienen más de uno reviso si la suma de sus digitos es uno primo, convirtiendolos temporalmente en strings para separarlos y luego hacer la suma de sus digitos pasandolos a enteros de nuevo, en caso de ser cierto se guarda en listaPrimos2 , de lo contrario lo obviara
  for i in listaPrimos:
    if len(str(i)) > 1:
     listaPrimos2.append(i)
    else:
      temporal = str(i)
      suma = 0
      for j in range(len(temporal)):
        suma += int(temporal[j])
      if suma in listaPrimos:
        listaPrimos2.append(i)
  for i in range(len(listaPrimos2)):
    if i+1 == len(listaPrimos2):
      print(listaPrimos2[i])
    else:
      print(listaPrimos[i], end=", ")
#mostrarPrimos(100)

#punto5
def sumarValoresMatriz(mat , lista):
  suma = 0 #variable donde guardaré la suma
  for i in range(len(lista)): #reviso cada dupla de la lista
    if lista[i][0] in mat: #si X se ecnuentra en mat significa que existe una llave, de lo contrario se suma 0
      for j in range(len(mat[lista[i][0]])): #reviso cada elemento de la llave
        if lista[i][1] == mat[lista[i][0]][j][0]: #si encuentro el Y dentro de la primera posicion de alguna dupla sumamos la segunda posicion, de lo contrario sumamos 0
          suma += mat[lista[i][0]][j][1]
  return suma
#mat = {0 : [(0, 1), (5, 4), (7, 5)],
#1 : [(6, 4), (7, 7)],
#2 : [(0, 2), (1, 2), (4, 9), (6, 1)],
#4 : [(2, 8), (3, 1), (5, 7)],
#6 : [(0, 3), (5, 6), (7, 2)],
#7 : [(0, 4), (1, 4), (2, 7)],
#8 : [(1, 9), (3, 8), (5, 7), (7, 6)]}
#print(sumarValoresMatriz(mat,[(0, 0), (8, 3), (3, 5), (7, 2), (4, 3), (4,6)]))

