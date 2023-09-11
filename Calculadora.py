def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "No se puede dividir por cero"
    return n1 / n2

while True:
    print("=="*70)
    print("Operaciones disponibles:")
    print("Menú\n 1. Suma\n 2.Resta\n 3.Multiplicacion\n 4. Division\n 5. Regresar al Menu\n 6. Salir\n")

    a = input("Seleccione una de las opciones disponibles en el menú: \n")

    if a == "6":
        print("Ha salido del programa")
        print("=="*70)
        break
    elif a not in ["1", "2", "3", "4", "5"]:
        print("Selecciona un numero valido")
        continue

    if a == "5":
        continue

    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    if a == "1":
        print("El resultado de la suma es: ", suma(n1, n2))
    elif a == "2":
        print("El resultado de la resta es: ", resta(n1, n2))
    elif a == "3":
        print("El resultado de la multiplicacion es: ", multiplicacion(n1, n2))
    elif a == "4":
        r = division(n1, n2)
        if isinstance(r, str):
            print(r)
        else:
            print("El resultado de la division es: ", r)