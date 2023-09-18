numero_entero = 1 #int
print(type(numero_entero));

cadena = "Hello World" #str
print(type(cadena));

booleano = True #bool
print(type(booleano));

coma_flotante = 3.14 #float
print(type(coma_flotante));

numero_complejo = 1j #complex
print(type(numero_complejo));

lista = [1, 3.3, "python"] #list es una lista de datos
print(type(lista));

tupla = (1,3.3, "python"); #tuple es una lista constante
print(type(tupla));

conjunto = {1, 3.3, "python"}; #set coleccion de datos unicos desordenada
print(type(conjunto));

diccionario = {1:"python", "key":3.3, 4.4:"a"} #dict coleccion de pares clave-valor, tambien denominado 'tabla-hash'
print(type(diccionario));

#Como recorrer una coleccion

l = [numero_entero, cadena, booleano, coma_flotante, numero_complejo, lista, tupla, conjunto, diccionario]
print('-------------');
#podemos usar un indice j
for j in range(len(l)):
    elemento = l[j];
    print(type(elemento))
    
#podemos recorrer directamente la lista
for elemento in l:
    print(type(elemento));
        





