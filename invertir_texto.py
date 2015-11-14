def invertir_texto(cadena):
    nueva_cadena=""
    for posicion in cadena:
        nueva_cadena = posicion+nueva_cadena
    return nueva_cadena

texto_original=input("Escribe un texto, por favor: ")
print("El texto invertido es "+invertir_texto(texto_original))
