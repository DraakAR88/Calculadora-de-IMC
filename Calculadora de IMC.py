print("Bienvenido aqui podras calcular tu indice de masa corporal(IMC)")
while True:
    nombre=input("Ingresa tu nombre: ").strip()
    if nombre.isalpha(): # Verifica si la cadena NO está vacía o si tiene algun numero
        break # Sale del bucle si es correcto
    else:
        print("\nError! El campo no puede estar en blanco y/o no debe incluir numeros.\n")   
while True:
    apellido_p=input("Ingresa tu apellido paterno: ").strip()
    if apellido_p.isalpha(): # Verifica si la cadena NO está vacía o si tiene algun numero
        break # Sale del bucle si es correcto
    else:
        print("\nError! El campo no puede estar en blanco y/o no debe incluir numeros.\n")
while True:
    apellido_m=input("Ingresa tu apellido materno: ").strip()
    if apellido_m.isalpha(): # Verifica si la cadena NO está vacía o si tiene algun numero
        break # Sale del bucle si es correcto
    else:
        print("\nError! El campo no puede estar en blanco y/o no debe incluir numeros.\n")
while True:
    ed=input("Ingresa tu edad: ").strip()
    if ed.isdigit(): # Verifica si la cadena NO está vacía o si tiene alguna letra
        edad=int(ed)
        break # Sale del bucle si es correcto
    else:
        print("\nError! El campo no puede estar en blanco y/o no debe incluir letras.\n")
while True:
    ent1=input("Ingresa tu peso en kilogramos: ").strip()
    try:
        peso=float(ent1)  # Intenta convertir la entrada a número flotante
        break # Sale del bucle si es correcto
    except ValueError:
        print("\nError! El campo no puede estar en blanco y/o no debe incluir letras.\n")
while True:
    ent2=input("Ingresa tu estatura en metros: ").strip()
    try:
        estatura=float(ent2)  # Intenta convertir la entrada a número flotante
        break # Sale del bucle si es correcto
    except ValueError:
        print("\nError! El campo no puede estar en blanco y/o no debe incluir letras.\n")

if (edad>19):
    print(nombre,apellido_p,apellido_m)
    print(f"Quien tiene {edad} años")
    print(f"Pesa {peso:.2f}Kg  y mide {estatura:.2f}m")
    imc=peso/estatura**2
    print(f"El IMC de esta persona es de: {imc:.2f}")
    if imc<=18.49:
        print("Usted tiene peso bajo")
    elif imc>=18.5 and imc<=24.99:
        print("Usted tiene peso normal")
    elif imc>=25 and imc<=29.99:
        print("Usted tiene sobrepeso")
    elif imc>=30 and imc<=34.99:
        print("Usted tiene obesidad leve")
    elif imc>=35 and imc<=39.99:
        print("Usted tiene obesidad media")
    elif imc>=40:
        print("Usted tiene obesidad mórbida")
else:
    print("Esta calculadora es para adultos apartir de los 20 Años")