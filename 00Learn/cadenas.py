# Podemos usar comillas dobles ("") o simples ('')
# para definir cadenas
mi_texto = '"Taller"' # Podemos usar las comillas de distinto tipo dentro
                      # de la cadena sin que interfieran
mi_texto2 = "de \"Python\"" # El \ actúa como "carácter de escape"
                            # Hace que se ignore el carácter siguiente
                            # para que no cierre comillas

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\n " + mi_texto2 #Salto de línea
print(texto_unido)

texto_unido = mi_texto + "\t " + mi_texto2 # Tabulación
print(texto_unido)

texto_unido = mi_texto + "\r " + mi_texto2 # Borra lo anterior
print(texto_unido)