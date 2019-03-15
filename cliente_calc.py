import socket
IP = '127.0.0.1'
PUERTO = 8080
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP, PUERTO))
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Bienvenido a la calculadora')
    print("Seleccione una opción:")
    print("0: Cerrar calculadora.")
    print("1: Sumar.")
    print("2: Multiplicar.")
    print("ATENCIÓN: Introduzca la opcíon seguido de los dos números")

    c_abierta = True
    while c_abierta:

        msg1 = input(":")
        msg1 = str.encode(msg1)
        cliente.send(msg1)

        resultado = (cliente.recv(1000).decode('utf-8'))
        if resultado == "Cerrando la calculadora...":
            print(resultado)
            cliente.close()
        else:
            print("El resultado es: ", resultado)

except KeyboardInterrupt:
    cliente.close()
    print('Cerrando la calculadora...')
