def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """Calcula cuántas unidades deben pedirse según el stock actual y el mínimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_reporte_reabastecimiento(inventario):
    """Imprime el nombre de cada artículo y la cantidad exacta a pedir."""
    print("=== REPORTE DE REABASTECIMIENTO ===")
    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")


def main():
    # Matriz con al menos 5 artículos: [Código, Nombre, Stock actual, Stock mínimo]
    inventario = [
        ["A01", "Teclado mecánico", 4, 10],
        ["A02", "Mouse inalámbrico", 15, 10],
        ["A03", "Cable HDMI", 2, 8],
        ["A04", "Base refrigerante", 6, 6],
        ["A05", "Memoria USB 64GB", 3, 12],
        ["A06", "Audífonos USB", 9, 5],
    ]
    mostrar_reporte_reabastecimiento(inventario)


if __name__ == "__main__":
    main()
