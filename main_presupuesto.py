# Programa 3: Calculadora de Gastos y Presupuesto Mensual
# Enunciado del Problema:
# Crea un programa que ayude al usuario a gestionar sus gastos mensuales y establecer un presupuesto. El usuario podrá 
# añadir diferentes categorías de gastos (ej. alquiler, comida, transporte, entretenimiento) y registrar montos 
# gastados en cada una. El programa permitirá establecer un presupuesto para cada categoría y mostrará cuánto queda 
# disponible o cuánto se ha excedido. Deberá ofrecer un resumen total de gastos y presupuesto, y la opción de reiniciar 
# los datos.

from menu_principal import mostrar_menu
from presupuesto import establecer_presupuesto
from gasto import registrar_gasto
from resumen import ver_resumen
from reinicio import reiniciar_datos

gastos = {}         # Diccionario para almacenar los gastos por categoría
presupuestos = {}   # Diccionario para almacenar los presupuestos por categoría

while True: # Bucle principal que mantiene el programa en ejecución
    mostrar_menu()
    try:
        opcion = input("Elige una opción: ").strip() # Elimina espacios en blanco
        
        if opcion == '1':
            establecer_presupuesto(presupuestos)
        elif opcion == '2':
            registrar_gasto(gastos, presupuestos)
        elif opcion == '3':
            ver_resumen(gastos, presupuestos)
        elif opcion == '4':
            reiniciar_datos(gastos, presupuestos)
        elif opcion == '5':
            print("Saliendo de la Calculadora de Gastos. ¡Hasta luego!")
            break # Sale del bucle while principal
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            continue # Vuelve al inicio del bucle para mostrar el menú de nuevo
    except Exception as e: # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}. Por favor, inténtalo de nuevo.")
    print("-" * 60) # Separador visual