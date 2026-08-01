ids = []
nombres = []
categorias = []
fechas = []
montos = []
responsables = []
observaciones = []
#--------------------------------------------#
#--|menu_principal_afinador_de_presupuesto|--#
#--------------------------------------------#
while True:
    print("menu principal afinador de presupuesto")
    print("1) crear presupuesto")
    print("2) editar presupuesto")
    print("3) eliminar presupuesto")
    print("4) buscar presupuesto")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|crear_presupuesto|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_presupuesto = 1
        else:
            id_presupuesto = ids[-1] + 1
        nombre = input("nombre del presupuesto: ")
        categoria = input("categoría: ")
        fecha = input("fecha: ")
        monto = float(input("monto del presupuesto: "))
        responsable = input("responsable: ")
        observacion = input("observación: ")
        ids.append(id_presupuesto)
        nombres.append(nombre)
        categorias.append(categoria)
        fechas.append(fecha)
        montos.append(monto)
        responsables.append(responsable)
        observaciones.append(observacion)
        print("presupuesto registrado correctamente.")
        print("id:", id_presupuesto)
    #------------------------#
    #--|editar_presupuesto|--#
    #------------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar presupuesto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {fechas[i]} | {montos[i]} | {responsables[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {montos[posicion]} | {responsables[posicion]} | {observaciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del presupuesto: ")
                categorias[posicion] = input("nueva categoría: ")
                fechas[posicion] = input("nueva fecha: ")
                montos[posicion] = float(input("nuevo monto: "))
                responsables[posicion] = input("nuevo responsable: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|eliminar_presupuesto|--#
    #--------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar presupuesto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {fechas[i]} | {montos[i]} | {responsables[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {montos[posicion]} | {responsables[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    fechas.pop(posicion)
                    montos.pop(posicion)
                    responsables.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------------#
    #--|buscar_presupuesto|--#
    #------------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar presupuesto")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {fechas[posicion]} | {montos[posicion]} | {responsables[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = montos[0]
            menor = montos[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {fechas[i]} | {montos[i]} | {responsables[i]} | {observaciones[i]}")
                suma += montos[i]
                if montos[i] > mayor:
                    mayor = montos[i]
                if montos[i] < menor:
                    menor = montos[i]
            promedio = suma / len(ids)
            print("estadísticas afinador de presupuesto")
            print("cantidad de registros:", len(ids))
            print("presupuesto acumulado: $", round(suma, 2))
            print("presupuesto promedio: $", round(promedio, 2))
            print("mayor presupuesto: $", round(mayor, 2))
            print("menor presupuesto: $", round(menor, 2))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")