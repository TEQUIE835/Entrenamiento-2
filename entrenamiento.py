import sys

def trytrue():
    while True:
        try:
            trytrue=int(input("\nIngrese una nota del 1 al 100: \n"))
            if 0<=trytrue<=100:
                return trytrue
            else:
                print("\nIngrese un numero valido")
        except ValueError:
            print("\nIngrese un numero valido")

while True:
    try:
        n=int(input("Cuantas notas desea ingresar?\n"))
        if n>0:
            break
        else:
            print("\nIngrese una cantidad valida\n")
    except ValueError:
        print("\nIngrese una cantidad valida\n")

notas = []
for i in range(n):
    a=i+1
    while True:
        try:
            nota= int(input(f"\nIngrese nota {a} (1-100)\n"))
            if 0<=nota<=100:
                break
            else:
                print("\nIngrese un numero valido")
        except:
            print("\nIngrese una nota valida")
    notas.append(nota)


#verificar si aprobo

def aprobado():

    notapr=trytrue()
    
    if 100>=notapr>=60:
        print("\nFelicidades, has aprobado")
    elif 60>notapr>=0:
        print("\nNo has aprobado, esfuerzate mas")


#Calcular promedio

def promedio():
    prom = 0
    for i in range(len(notas)):
        prom+= notas[1]
    prom = prom/n
    print(f"\nTu promedio es: {prom}")
    if prom>= 60:
        print("Has aprobado")
    elif prom < 60:
        print("No has aprobado")
    else:
        print("que tocaste we")
        


#Contar numeros mayores
def mayores():
    notam=trytrue()
    cont=0
    for i in range(len(notas)):
        if notam<notas[i]:
            cont += 1
    
    print(f"\nHay {cont} notas mayores")

#Verificacion de cuantas veces se repite la nota
def verificacion():
    notav=trytrue()
    cont2=0
    for i in range(len(notas)):
        if notav==notas[i]:
            cont2 += 1
    print(f"\nLa nota {notav} se repite {cont2} veces")

def salir():
    print("\nNos vemos...")
    sys.exit()


def mostrarmenu():
    print("\nQue quieres hacer?")
    print("1. Verificar aprobacion")
    print("2. Calcular promedio")
    print("3. Contar numeros mayores")
    print("4. Mostrar notas")
    print("5. Verificar cuantas veces esta la nota")
    print("6. Salir")


while True:
    mostrarmenu()
    while True:
        try:
            opc=int(input("\nIngrese su opcion: "))
            if 1<=opc<=6:
                break
            else:
                print("Ingrese una opcion valida")
        except ValueError:
            print("Ingrese una opcion valida")
    match opc:
        case 1:
            aprobado()
        case 2:
            promedio()
        case 3:
            mayores()
        case 4:
            print("\nTus notas son: ")
            for i in range(len(notas)):
                print(notas[i])
        case 5:
            verificacion()
        case 6:
            salir()
        case _:
            print("Hubo un error")
