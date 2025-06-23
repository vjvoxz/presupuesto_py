def registrar_gasto(gastos, presupuestos):
    """Permite al usuario registrar un gasto en una categoría existente o nueva."""
    categoria = input("Ingresa la categoría del gasto (ej. comida, transporte): ").strip().lower()
    if not categoria:
        print("El nombre de la categoría no puede estar vacío.")
        return

    try:
        monto = float(input(f"Ingresa el monto gastado en '{categoria}': "))
        if monto <= 0:
            print("El monto del gasto debe ser un número positivo.")
            return

        # Si la categoría no existe en gastos, la inicializamos
        if categoria not in gastos:
            gastos[categoria] = 0.0

        gastos[categoria] += monto
        print(f"Gasto de ${monto:.2f} registrado en '{categoria}'.")

        # Mensaje opcional si la categoría tiene presupuesto y se excede
        if categoria in presupuestos:
            restante = presupuestos[categoria] - gastos[categoria]
            if restante < 0:
                print(f"¡Advertencia! Has excedido el presupuesto para '{categoria}' por ${abs(restante):.2f}.")
            else:
                print(f"Quedan ${restante:.2f} en el presupuesto de '{categoria}'.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido para el monto.")
