#entrada
cadena = input("Introduce una cadena: ");

#salida
print(cadena);

print('----------------------');

#como formatear texto y variables en un print
nombre = "Marcos";
apellidos = "Rivera Gavilan";
correo = "reveragavilanmarcos@gmail.com"

print("Hola me llamo " + nombre + " " + apellidos + " y mi correo es " + correo);
print(f"Hola me llamo {nombre} {apellidos} y mi correo es {correo}");
print("Hola me llamo {} {} y mi correo es {}".format(nombre, apellidos, correo));