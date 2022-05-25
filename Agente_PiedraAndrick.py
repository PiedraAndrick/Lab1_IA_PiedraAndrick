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

    #Definimos los estados finales de las habiaciones
    estadoActual_habitacion1 = input("Actualizar estado de habitacion 1: ") #Ingreso del estado requerido para la habitacion
    estadoActual_habitacion2 = input("Actualizar estado de habitacion 2 : ") #Ingreso del estado requerido para la habitacion
    estadoActual_habitacion3 = input("Actualizar estado de habitacion 3 : ") #Ingreso del estado requerido para la habitacion
    
    #Creamos la lista de los estados a los cuales se debe actualizar
    lista_habitaciones_estados_actalizar = [estadoActual_habitacion1,estadoActual_habitacion2,estadoActual_habitacion3]

    #HABITACION 1
    if estado_habitacion1 == '0':
        # Habitacion esta Caliente     
      print("Habitacion 1 caliente")
      
      # si la habitacion se encuentra ya en estado caliente, entonces no suma costo
      if estadoActual_habitacion1 == '0':
          print("Habitacion ya esta calida")
      #si se encuentra en estado frio, entonces realiza la accion y suma 1 costo    
      else:
          print("Enfriando Habitacion ")
          estado_global['Habitacion 1'] = '1' 
          costo += 1
    #si la habitacion se encuentra en estado 1(fria) entonces
    else: 
      #Habitacion esta fria
      print("Habitacion esta fria")  
      #si se requiere que la habitacion quede fria entonces no suma costo
      if estadoActual_habitacion1 == '1':  
          print("Habitacion  ya esta fria")
      #si la habitacion esta caliente, entonces realiza la accion y suma 1 costo    
      else:
          print("Calentando Habitacion 1")
          estado_global['Habitacion 1'] = '0' 
          costo += 1
          
      #HABITACION 2
      if estado_habitacion2 == '0':
          # Habitacion esta Caliente     
        print("Habitacion 2 caliente")
        
        # si la habitacion se encuentra ya en estado caliente, entonces no suma costo
        if estadoActual_habitacion2 == '0':
            print("Habitacion ya esta calida")
        #si se encuentra en estado frio, entonces realiza la accion y suma 1 costo    
        else:
            print("Enfriando Habitacion ")
            estado_global['Habitacion 2'] = '1' 
            costo += 1
      #si la habitacion se encuentra en estado 1(fria) entonces
      else: 
        #Habitacion esta fria
        print("Habitacion esta fria")  
        #si se requiere que la habitacion quede fria entonces no suma costo
        if estadoActual_habitacion2 == '1':  
            print("Habitacion  ya esta fria")
        #si la habitacion esta caliente, entonces realiza la accion y suma 1 costo    
        else:
            print("Calentando Habitacion 2")
            estado_global['Habitacion 2'] = '0' 
            costo += 1
            
        #HABITACION 3
        if estado_habitacion3 == '0':
            # Habitacion esta Caliente     
          print("Habitacion 3 caliente")
          
          # si la habitacion se encuentra ya en estado caliente, entonces no suma costo
          if estadoActual_habitacion3 == '0':
              print("Habitacion ya esta calida")
          #si se encuentra en estado frio, entonces realiza la accion y suma 1 costo    
          else:
              print("Enfriando Habitacion ")
              estado_global['Habitacion 3'] = '1' 
              costo += 1
        #si la habitacion se encuentra en estado 1(fria) entonces
        else: 
          #Habitacion esta fria
          print("Habitacion esta fria")  
          #si se requiere que la habitacion quede fria entonces no suma costo
          if estadoActual_habitacion3 == '1':  
              print("Habitacion  ya esta fria")
          #si la habitacion esta caliente, entonces realiza la accion y suma 1 costo    
          else:
              print("Calentando Habitacion 3")
              estado_global['Habitacion 3'] = '0' 
              costo += 1
    

airConditioning_world()