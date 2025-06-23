def ver_resumen(gastos, presupuestos):
    """Muestra un resumen detallado de los gastos y presupuestos por categoría."""
    print("\n--- Resumen Mensual ---")

    if not gastos and not presupuestos:
        print("No hay datos de gastos ni presupuestos registrados aún.")
        return

    total_gastos = 0.0
    total_presupuesto = 0.0

    # Iterar sobre todas las categorías que tienen gastos o presupuesto
    todas_categorias = set(gastos.keys()).union(set(presupuestos.keys()))

    for categoria in sorted(list(todas_categorias)): # Ordenar para una mejor visualización
        gasto_actual = gastos.get(categoria, 0.0)
        presupuesto_actual = presupuestos.get(categoria, 0.0)

        total_gastos += gasto_actual
        total_presupuesto += presupuesto_actual

        print(f"\nCategoría: {categoria.capitalize()}")
        print(f"  Presupuesto: ${presupuesto_actual:.2f}")
        print(f"  Gasto:       ${gasto_actual:.2f}")

        if presupuesto_actual > 0:
            saldo = presupuesto_actual - gasto_actual
            if saldo >= 0:
                print(f"  Saldo restante: ${saldo:.2f}")
            else:
                print(f"  Excedido por:   ${abs(saldo):.2f}")
        else:
            print("  No hay presupuesto establecido para esta categoría.")

    print("\n--- Totales ---")
    print(f"Presupuesto Total: ${total_presupuesto:.2f}")
    print(f"Gastos Totales:    ${total_gastos:.2f}")
    
    saldo_total = total_presupuesto - total_gastos
    if saldo_total >= 0:
        print(f"Balance General:   ${saldo_total:.2f} (Restante)")
    else:
        print(f"Balance General:   ${abs(saldo_total):.2f} (Excedido)")