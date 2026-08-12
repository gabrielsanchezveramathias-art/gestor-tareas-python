while True:
    print("================================")
    print("       GESTOR DE TAREAS")
    print("================================")
    print()
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    print()

    if opcion == "1":
        print("Tareas:")
        # Aquí iría la lógica para mostrar las tareas
    elif opcion == "2":
        tarea = input("Ingrese la descripción de la tarea: ")
        # Aquí iría la lógica para añadir la tarea
        print(f"Tarea '{tarea}' añadida.")
    elif opcion == "3":
        # Aquí iría la lógica para completar la tarea
        print("Tarea completada.")
    elif opcion == "4":
        # Aquí iría la lógica para eliminar la tarea
        print("Tarea eliminada.")
    elif opcion == "5":
        print("Saliendo del gestor de tareas.")
        break
    else:
        print("Opción no válida.")

    print()