peso = int(input("Dime tu peso: "))
altura = int(input("¿Y tu altura? "))
               
altura_al_cuadrado = altura * altura
IMC = peso / altura_al_cuadrado
print("IMC:")
print(IMC)



#Un índice de 18,5 o menos se considera bajo peso
#Un índice entre 18,5 y 24,9 se considera saludable
#Un índice entre 25 y 29,9 se considera sobrepeso
#Un índice de 30 o más se considera obesidad
