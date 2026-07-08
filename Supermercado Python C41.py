import os


def limpiar():
    os.system("cls")


productos = []
carrito = []
total_recaudado = 0


def buscar(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def validar():
    while True:
        codigo = input("Ingrese el codigo: ")
        print("\n")
        if len(codigo) != 3 or not codigo.isdigit():
            print("El codigo debe tener exactamente 3 digitos\n")
            continue

        numero = int(codigo)

        if numero < 1 or numero > 100:
            print("El codigo debe estar entre 001 y 100\n")
            continue

        if buscar(codigo) is not None:
            print("Ese codigo ya existe\n")
            continue

        return codigo


def pedir_codigo():
    while True:
        codigo = input("Ingrese el codigo: ")
        print("\n")
        if len(codigo) != 3 or not codigo.isdigit():
            print("El codigo debe tener exactamente 3 digitos\n")
            continue

        numero = int(codigo)
        if numero < 1 or numero > 100:
            print("El codigo debe estar entre 001 y 100\n")
            continue

        return codigo


def reg_precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("El Precio es invalido")
            else:
                return precio
        except ValueError:
            print("Debe ingresar un numero no caracteres")


def reg_stock():
    while True:
        try:
            stock = int(input("Stock: "))
            if stock < 0:
                print("El stock es invalido.")
            else:
                return stock
        except ValueError:
            print("Debe ingresar un numero entero")


def registrar():
    if len(productos) >= 100:
        print("No se pueden registrar mas productos")
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
        "stock": stock,
        "vendidos": 0,
        "recaudado": 0
    }

    productos.append(producto)
    print("Su producto fue registrado correctamente")


def mostrar_prod():
    if len(productos) == 0:
        print("No hay productos")
        return
    print("\nLISTA DE PRODUCTOS\n")
    for producto in productos:
        print(
            f"Codigo: {producto['codigo']} | "
            f"Nombre: {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Stock: {producto['stock']}"
        )


def sig():
    input("\nPresione ENTER para continuar...")
    limpiar()


def cantidad_en_carrito(codigo):

    cantidad = 0

    for item in carrito:
        if item["codigo"] == codigo:
            cantidad += item["cantidad"]

    return cantidad


def agre_carri():
    codigo = pedir_codigo()
    produc_encontrado = buscar(codigo)
    if produc_encontrado is None:
        print("El Producto no existe\n")
        return

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
        except ValueError:
            print("Debe ingresar un numero entero\n")
            continue

        if cantidad <= 0:
            print("Debe elegir por lo menos una unidad\n")
            continue

        if cantidad + cantidad_en_carrito(codigo) > produc_encontrado["stock"]:
            print("No hay stock suficiente")
            break

        nuevo_item = {
            "codigo": produc_encontrado["codigo"],
            "nombre": produc_encontrado["nombre"],
            "cantidad": cantidad,
            "precio": produc_encontrado["precio"],
            "subtotal": produc_encontrado["precio"] * cantidad,
        }
        carrito.append(nuevo_item)
        produc_encontrado["stock"] -= cantidad
        break


def calcu_total():
    total = 0
    for item in carrito:
        total += item['subtotal']
    return total


def mostra_carri():
    while True:
        if not carrito:
            print("Su carrito esta vacio")
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
    global total_recaudado

    if not carrito:
        print("Su carrito esta vacio\n")
        return None

    print("------------------------------------------------\n")
    print("################################################")
    print("#                  TICKET                      #")
    print("################################################\n")

    total = calcu_total()

    for item in carrito:

        producto = buscar(item["codigo"])

        producto["vendidos"] += item["cantidad"]
        producto["recaudado"] += item["subtotal"]

        print(
            f"{item['nombre']} | x{item['cantidad']} | ${item['subtotal']}"
        )

    total_recaudado += total

    print("------------------------------------------------")
    print(f"Total a pagar: ${total}")

    carrito.clear()


def estadisticas():
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    total_unidades = 0

    mas_vendido = productos[0]

    for producto in productos:

        total_unidades += producto["vendidos"]

        if producto["vendidos"] > mas_vendido["vendidos"]:
            mas_vendido = producto

    print("\n========== ESTADISTICAS ==========\n")
    print(f"Productos registrados: {len(productos)}")
    print(f"Unidades vendidas: {total_unidades}")
    print(f"Dinero recaudado: ${total_recaudado}")
    print("\nProducto más vendido")
    print(f"Nombre: {mas_vendido['nombre']}")
    print(f"Codigo: {mas_vendido['codigo']}")
    print(f"Unidades vendidas: {mas_vendido['vendidos']}")
    print("\nTOP DE PRODUCTOS")

    copia = productos[:]

    for i in range(len(copia)-1):
        for j in range(i+1, len(copia)):
            if copia[j]["vendidos"] > copia[i]["vendidos"]:
                copia[i], copia[j] = copia[j], copia[i]

    limite = 3

    if len(copia) < 3:
        limite = len(copia)

    for i in range(limite):
        print(
            f"{i+1}. {copia[i]['nombre']} - {copia[i]['vendidos']} unidades"
        )


def menu():
    while True:
        print("----------------------------------------")
        print("     ###### SUPERMERCADO ######/n")
        print("       1. Registrar producto")
        print("       2. Mostrar productos")
        print("       3. Agregar al carrito")
        print("       4. Mostrar carrito")
        print("       5. Finalizar compra")
        print("       6. Estadísticas")
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

        elif opcion == "6":
            limpiar()
            estadisticas()
            sig()

        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida.")
            sig()


menu()