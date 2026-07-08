import os


def limpiar():
    os.system("cls")


productos = []
carrito = []


def buscar(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def validar():
    while True:
        codigo = input("Ingrese codigo: ")
        print("\n")
        if len(codigo) != 3 or not codigo.isdigit():
            print("El código debe tener exactamente 3 dígitos. \n")
            continue

        numero = int(codigo)
        if numero < 1 or numero > 100:
            print("El código debe estar entre 001 y 100. \n")
            continue
        return codigo


def reg_precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("Precio inválido.")
            else:
                return precio
        except ValueError:
            print("Ingrese un número.")


def reg_stock():
    while True:
        try:
            stock = int(input("Stock: "))
            if stock < 0:
                print("Stock inválido.")
            else:
                return stock
        except ValueError:
            print("Ingrese un número entero.")


def registrar():
    if len(productos) >= 100:
        print("No se pueden registrar más productos.")
        return

    print("\n------------- REGISTRAR PRODUCTO -------------")
    codigo = validar()
    nombre = input("Nombre: ")
    precio = reg_precio()
    stock = reg_stock()

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)
    print("Producto registrado correctamente.")


def mostrar_prod():
    if len(productos) == 0:
        print("No hay productos.")
        return
    print("\nLISTA DE PRODUCTOS\n")
    for producto in productos:
        print(
            f"Código: {producto['codigo']} | "
            f"Nombre: {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Stock: {producto['stock']}"
        )


def sig():
    input("\nPresione ENTER para continuar...")
    limpiar()


def agre_carri():
    codigo = validar()
    producto_encontrado = buscar(codigo)
    if producto_encontrado is None:
        print("El Producto no existe.\n")
        return

    while True:
        try:
            cantidad = int(input("Ingrese Cantidad: "))
        except ValueError:
            print("Debe ingresar un número entero.\n")
            continue

        if cantidad <= 0:
            print("Debe elegir por lo menos una unidad.\n")
            continue

        if cantidad > producto_encontrado["stock"]:
            print("No hay stock suficiente.\n")
            continue

        producto_encontrado["stock"] -= cantidad
        nuevo_item = {
            "codigo": producto_encontrado["codigo"],
            "nombre": producto_encontrado["nombre"],
            "cantidad": cantidad,
            "precio": producto_encontrado["precio"],
            "subtotal": producto_encontrado["precio"] * cantidad,
        }
        carrito.append(nuevo_item)
        break


def calcu_total():
    total = 0
    for item in carrito:
        total += item['subtotal']
    return total


def mostra_carri():
    while True:
        if not carrito:
            print("El carrito está vacio.")
            return None

        print("----------------------------------------")
        print("######### CARRITO DE COMPRAS ##########")
        print("Producto | Cantidad | Precio | Subtotal \n")

        for item in carrito:
            print(
                item['nombre'], "|",
                item['cantidad'], "|",
                item['precio'], "|",
                item['subtotal']
            )

        total = calcu_total()

        print("----------------------------------------")
        print(f"Total a pagar: {total}")
        break


def finalizar():
    if not carrito:
        print("Error: El carrito se encuentra vacio \n")
        return None

    print("----------------------------------------\n")
    print("########################\n")
    print("       TICKET     ")
    print("########################\n")
    print()

    for item in carrito:
        print(f"{item['nombre']} | x{item['cantidad']} | {item['subtotal']}")
        print()

    total = calcu_total()

    print("----------------------------------------\n")
    print(f"Total a pagar: {total}")
    carrito.clear()
    return None

def venta():
    for item in carrito:
        producto = buscar(item["codigo"])
        producto["vendidos"] += item["cantidad"]


def menu():
    while True:
        print("----------------------------------------")
        print("     ###### SUPERMERCADO ######/n")
        print("       1. Registrar producto")
        print("       2. Mostrar productos")
        print("       3. Agregar al carrito")
        print("       4. Mostrar carrito")
        print("       5. Finalizar compra")
        print("       0. Salir del programa")
        print("----------------------------------------")

        opcion = input("Opcion: ")

        if opcion == "1":
            limpiar()
            registrar()
            sig()

        elif opcion == "2":
            limpiar()
            mostrar_prod()
            sig()

        elif opcion == "3":
            limpiar()
            agre_carri()
            sig()

        elif opcion == "4":
            limpiar()
            mostra_carri()
            sig()

        elif opcion == "5":
            limpiar()
            finalizar()
            sig()

        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida.")
            sig()


menu()