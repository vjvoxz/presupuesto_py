def reiniciar_datos(gastos, presupuestos):
    """Reinicia todos los datos de gastos y presupuestos."""
    confirmacion = input("¿Estás seguro de que quieres reiniciar todos los datos? (s/n): ").strip().lower()
    if confirmacion == 's':
        gastos.clear() # Vacía el diccionario de gastos
        presupuestos.clear() # Vacía el diccionario de presupuestos
        print("Todos los datos de gastos y presupuestos han sido reiniciados.")
    else:
        print("Operación de reinicio cancelada.")