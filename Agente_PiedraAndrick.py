def airConditioning_world():
#Costo inicial
    costo = 0
 #Definimos los estados iniciales de las habiaciones 
    estado_habitacion1 = input("Estado actual de la Habitacion 1 : ") #Ingreso del estado de la primera habitacion
    estado_habitacion2 = input("Estado actual de la Habitacion 2 : ") #Ingreso del estado de la segunda habitacion
    estado_habitacion3 = input("Estado actual de la Habitacion 3 : ") #Ingreso del estado de la tercera habitacion
     #Creamos una lista de los estados iniciales
    lista_habitaciones_estados_originales = [estado_habitacion1,estado_habitacion2,estado_habitacion3]
    
    #Definimos el estado global de las habitaciones, tomando los estados de las habitaciones ingresados.
    estado_global = {'Habitacion 1': estado_habitacion1 , 'Habitacion 2': estado_habitacion2,'Habitacion 3': estado_habitacion3}
    print("Estado Global:" + str(estado_global))

airConditioning_world()