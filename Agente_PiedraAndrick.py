def airConditioning_world():
#Costo inicial
    costo = 0
 #Definimos los estados iniciales de las habiaciones 
    estado_habitacion1 = input("Estado actual de la Habitacion 1 : ") #Ingreso del estado de la primera habitacion
    estado_habitacion2 = input("Estado actual de la Habitacion 2 : ") #Ingreso del estado de la segunda habitacion
    estado_habitacion3 = input("Estado actual de la Habitacion 3 : ") #Ingreso del estado de la tercera habitacion

    #Definimos los estados finales de las habiaciones
    estadoActual_habitacion1 = input("Actualizar estado de habitacion 1: ") #Ingreso del estado requerido para la habitacion
    estadoActual_habitacion2 = input("Actualizar estado de habitacion 2 : ") #Ingreso del estado requerido para la habitacion
    estadoActual_habitacion3 = input("Actualizar estado de habitacion 3 : ") #Ingreso del estado requerido para la habitacion
    
    #Creamos la lista de los estados a los cuales se debe actualizar
    lista_habitaciones_estados_actalizar = [estadoActual_habitacion1,estadoActual_habitacion2,estadoActual_habitacion3]

#Bucle FOR que recorre la lista de las habitaciones de los estados originales
    # y se compara con los estados actualizados 
    print("*****ACONDICIONANDO HABITACIONES*****")
    for i in range(0,len(lista_habitaciones_estados_originales)):
        
        #si la habitacion se encuentra en estado 0(caliente) entonces
        if lista_habitaciones_estados_originales[i] == '0':
            # Habitacion esta Caliente     
          print("Habitacion "+ str(i)+" caliente")
          
          # si la habitacion se encuentra ya en estado caliente, entonces no suma costo
          if lista_habitaciones_estados_actalizar[i] == '0':
              print("Habitacion "+ str(i)+" ya esta calida")
          #si se encuentra en estado frio, entonces realiza la accion y suma 1 costo    
          else:
              print("Enfriando Habitacion "+ str(i))
              estado_global['Habitacion '+str(i+1)] = '1' 
              costo += 1
        #si la habitacion se encuentra en estado 1(fria) entonces
        else: 
          #Habitacion esta fria
          print("Habitacion "+ str(i)+" fria")  
          #si se requiere que la habitacion quede fria entonces no suma costo
          if lista_habitaciones_estados_actalizar[i] == '1':  
              print("Habitacion "+ str(i)+" ya esta fria")
          #si la habitacion esta caliente, entonces realiza la accion y suma 1 costo    
          else:
              print("Calentando Habitacion "+ str(i))
              estado_global['Habitacion '+str(i+1)] = '0' 
              costo += 1
     # Terminando
    print("GOAL STATE: ")
    print(estado_global)
    print("Performance Measurement: " + str(costo))

airConditioning_world()