from funciones import validador

apellido = input("cual es tu apellido ")
año = int(input("cual es tu año de nacimiento "))
altura = float(input("tu altura "))

persona = [apellido, año, altura]

resultado = validador(persona)

if resultado[0]:
    print("Nacido en 2010 o mas")

if resultado[1]:
    print("Cumple con la altura")