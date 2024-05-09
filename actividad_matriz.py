print("Empresa automotriz")
listak = []


#Funcion lectura de revision estado del vehiclo dependiendo de las horas.
def horas_funcionamiento(horas, vehiculo):
    print("-" * 30)
    #Condicional para la clasificacion de mantenimiento
    if horas >= 300:
        print(f"El veiculo {vehiculo} necesita mantenimiento.")
    elif horas < 300:
        print(f"El vehiciulo {vehiculo} esta en buen estado.")
    #Fin de las condicionales.
#Fin de la funcion.


#Funcion lectura de revision de datos de aceites.
def revision_aceite(aceite, vehiculo):
    print("-" * 30)
    #Condicional para la clasificacion del aceite.
    if aceite < 100:
        print(f" El vehiulo {vehiculo} neceseita cambio de aceite.")
    elif aceite == 100:
        print(f"El aceite de {vehiculo} esta en condiciones.")
    #Fin de las condicionales.
#Fin de la funcion.


#Funcion estado de neumaticos
def revision_neumaticos(neumatico, vehiculo):
    print("-" * 30)
    #Condicional para el cambio de neumaticos
    if neumatico < 30 or neumatico > 33:
        print(f" El ehiculo {vehiculo} requiere cambio de neumaticos.")
    else:
        print(f"El vehiculo {vehiculo} no presenta fallas. ")
    #Fin de las condicionales.
#Fin de la funcion.


#Funcion estado de motor
def revision_motor(motor, vehiculo):
    print("-" * 30)
    #Condicional para la clasificacion del motor.
    if motor > 95:
        print(f" El motor del vehiculo {vehiculo} presenta fallas.")
    elif motor >= 85 and motor<=95:
        print(f" El motor del vehiculo {vehiculo} esta en optimas condiciones.")
    elif motor < 85:
        print(f" El motor del vehiculo {vehiculo} esta apagado o presenta fallas.")
    else:
        print("Error") 
    #Fin de las condicionales.
#Fin de la funcion.

#matriz de datos obtenidos
matriz = [[1, 150000, 80, 300, 32, 90],
          [2, 20000, 75, 550, 30, 120],
          [3, 11000, 40, 400, 25, 90],
          [4, 16800, 100, 100, 32, 30], 
          [5, 17650, 90, 250, 32, 100]]



#Inicio de codigo.
print("Empresa automotriz")

for i in matriz:
     print(i)
print("\n\n")
#Bucle para recorrer la matriz y usar cada dato en la funciones para clasificarlos
for i in matriz :
    horas_funcionamiento(i[3], i[0])
    listak.append(i[1])
    revision_aceite(i[2], i[0])
    revision_motor(i[5], i[0])
    revision_neumaticos(i[4], i[0])
    print("\n\n")
#Fin de bucle

#Operacion para obtener el promedio de kilometros    
promedio=sum(listak)/len(listak)
print("El promedio de kilometraje de todos los automoviles es:", promedio)