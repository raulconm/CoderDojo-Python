nueva_cadena_a = ""                            # PASO 1: Inicializo acumulador
nueva_cadena_b = ""

frase = "Esta es una frase de prueba"          # PASO 2: la frase

for letra in frase:                            # PASO 3: recorro la frase
    nueva_cadena_a = nueva_cadena_a + letra    # PASO 4: acumulo letras
    nueva_cadena_b = letra + nueva_cadena_b
    
print("La cadena a es: ",nueva_cadena_a)       # PASO 5: imprimo el resultado
print("La cadena b es: ",nueva_cadena_b)  
