def establecer_presupuesto(presupuestos):
    """Permite al usuario establecer o actualizar el presupuesto para una categoría."""
    categoria = input("Ingresa la categoría para establecer el presupuesto (ej. comida, alquiler): ").strip().lower()
    if not categoria:
        print("El nombre de la categoría no puede estar vacío.")
        return

    try:
        monto = float(input(f"Ingresa el monto del presupuesto para '{categoria}': "))
        if monto < 0:
            print("El monto del presupuesto no puede ser negativo.")
            return
        presupuestos[categoria] = monto
        print(f"Presupuesto de ${monto:.2f} establecido para '{categoria}'.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido para el monto.")
