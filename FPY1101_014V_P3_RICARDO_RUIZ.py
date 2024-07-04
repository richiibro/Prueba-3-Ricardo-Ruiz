import os
os.system("cls")

personas = []

def grabar_datos():
    nombre = str(input("Ingrese su nombre y apellido: "))
    while not nombre:
        print("No se registro su Nombre, try again")
        nombre=str(input("Ingrese su nombre y apellido: "))
    
    edad = int(input("Ingrese su edad: "))
    while not edad:
        print("No se registro su edad, try again")
        edad = int(input("Ingrese su edad: "))
    
    fnacimiento = str(input("Ingrese su fecha de nacimiento, EJM: 05 de marzo de 2002: "))
    while not fnacimiento:
        print("Fecha de nacimiento no valida, try again")
        fnacimiento = str(input("Ingrese su fecha de nacimiento, EJM: 05 de marzo de 2002: "))
        
    pertenencia = str(input("De donde proviene? españa/union europea: "))
    while not pertenencia:
        print("Su pertenencia no es valida, try again")
        pertenencia = str(input("De donde proviene? españa/union europea: "))
        
    estadoc = str(input("Ingrese su estado civil: "))
    while not estadoc:
        print("Estado civil no valido, try again")
        estadoc = str(input("Ingrese su estado civil: "))
        
    nif = (input("Ingrese su Nif, sin guion y debe tener 11 caracteres: ")).strip
    while not nif:
        print("Nif no valido, try again")
        nif = (input("Ingrese su Nif, sin guion y debe tener 11 caracteres: ")).strip
    
    datos = {
        "nombre" : nombre,
        "edad"   : edad,
        "fnacimiento" : fnacimiento,
        "pertenencia" : pertenencia,
        "estadoc" : estadoc,
        "nif"   : nif
        }
    
    personas.append(datos)
    
def buscar_por_nif():
    buscar = (input("Ingrese NIF a buscar: "))
    for datos in personas:
        if datos ["nif"]==buscar:
            print(f"""
                  nombre:{datos["nombre"]}
                  edad:{datos["edad"]}
                  fnacimiento:{datos["fnacimiento"]}
                  pertenencia:{datos["pertenencia"]}
                  estadoc:{datos["estadoc"]}
                  nif:{datos["nif"]}
                  """)

def imprimir_certificado():
    for datos in personas:
        print(f"""
                  nombre: {datos["nombre"]}
                  fnacimiento: {datos["fnacimiento"]}
                  estadoc: {datos["estadoc"]}
                  pertenencia: {datos["pertenencia"]}
                  """)  

        
def salir_programa():
    print("Saliendo, gracias por visitar la version 1.0 de Ricardo Ruiz") 
    exit()
    
opcion = ""

while True:
    os.system("cls")
    opcion=str(input("""
                     ======MENU======
                     1. Guardar datos:
                     2. Buscar por NIF:
                     3. Imprimir certificados:
                     4. Salir:
                     Ingrese una opcion:
                     """))
    
    if opcion == "1":
        os.system("cls")
        grabar_datos()
        os.system("pause")
    
    elif opcion == "2":
        os.system("cls")
        buscar_por_nif()
        os.system("pause")
    
    elif opcion == "3":
        os.system("cls")
        imprimir_certificado()
        os.system("pause")
    
    elif opcion == "4":
        os.system("cls")
        salir_programa()
        os.system("pause")
    
    else:
        print("Opcion ingresada no es valida")