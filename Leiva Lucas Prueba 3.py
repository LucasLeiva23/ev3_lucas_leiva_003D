
import random as r
import os
import time
import msvcrt as m

clientes=[]
cliente=[]

def limpia_pantalla(seg):
   time.sleep(seg)
   os.system("cls")

def lista_clientes():
    for lista in clientes:
        for cliente in lista:
            print(cliente)

def menu():
    print("--------[IMMO Ltda]--------")
    print("[1.- Registrar Cliente    ]")
    print("[2.- Buscar Rut           ]")
    print("[3.- Reporte              ]")
    print("[0.- Salir                ]")
    print("---------------------------")
    op=int(input("Ingrese una opcion:\t"))
    return op

def registrar():
    while True:
        rut_cliente=input("Ingrese su Rut(Solo numeros):\t")
        if len(rut_cliente)==9 and rut_cliente.isdigit:
            break
        else:
            print("Ingrese un Rut valido")
    while True:
        nombre_cliente=input("Ingrese su Nombre:\t")
        if len(nombre_cliente)<1:
            print("Ingrese un nombre valido")
        else:
            break
    while True:   
        reg=int(input("Seleccione una opcion:\n1.- VS(vive santiago\n2.- VF(vive la florida\n3.- VN(vive ñuñoa\n"))
        if reg==1:
            print("Ha Seleccionado Santiago")
            proyecto="VS"
            break
        elif reg==2:
            print("Ha seleccionado la Florida")
            proyecto="VF"
            break
        elif reg==3:
            print("Ha seleccionado Ñuñoa")
            proyecto="VN"
            break
    renta_men=r.randrange(300000,10000000)
    cliente=[rut_cliente,nombre_cliente,proyecto,renta_men]
    clientes.append(cliente)
    print("REGISTRADO CON EXITO!")
    limpia_pantalla(2)


def busca(rut_cliente):
    i=1
    for lista in clientes:
        if lista[0]==rut_cliente:
            print(f"Rut Cliente: {lista[0]}")
            print(f"Nombre Cliente: {lista[1]}")
            if lista[2]=="VS":
                print("Proyecto: VS(Vive Santiago")
            elif lista[2]=="VF":
                print("Proyecto: VF(Vive la Florida")
            elif lista[2]=="VN":
                print("Proyecto: VN(Vive Ñuñoa) ")
            i=0
    if i==1:
        print("No se a encontrado cliente Registrado!")
        limpia_pantalla(2)
    print("Presione cualquier tecla para poder continuar:\t")
    m.getch()
    limpia_pantalla(2)
    
def reporte_renta():
    cont=0
    print("--------REPORTE--------")
    for lista in clientes:
        if lista[3] >= 900000:
            cont+=1
            print(f"Sr/a {lista[1]}")
            print(f"Rut {lista[0]}\n")
            print(f"Con su renta Mensual: {lista[3]}")
            print(f"En el Proyecto: {lista[2]}")
            print(f"Puede acceder a un Departamento de UF: {r.randrange(2500,3700)}")
            print("---------------------------------------------")
            




while True:
    try:
        opcion=menu()
        if opcion==1:
            registrar()
        elif opcion==2:
            rut=input("Ingrese el Rut que desea Buscar:\t")
            if (len(rut)==5) and rut.isdigit:
                busca(rut)
        elif opcion==3:
            reporte_renta()
        elif opcion==0:
            limpia_pantalla(0)
            print(f"Fecha de registro: {time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year}")
            print("Saliendo del Sistema...")
            limpia_pantalla(3)
            for i in range (3,0,-1):
                print(f"Saliendo en {i}")
                limpia_pantalla(1)
            break
        else:
            limpia_pantalla(0)
            print("Opcion Incorrecta")
            limpia_pantalla(2)
            print("Cargando sistema...")
            limpia_pantalla(1)
    except:
        print("Ha ocurrido un error inesperado")
        
