import socket
PORT = 8080
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


def process_client(clientsocket):
    print(clientsocket)
    while True:
        mensaje_cliente = clientsocket.recv(2048).decode("utf-8").split(",")
        print("El cliente ha elegido la opcion", mensaje_cliente[0], "con los numeros", mensaje_cliente[1], "y", mensaje_cliente[2])

        if mensaje_cliente[0] == "0":
            print("Cerrando la calculadora...")
            mensaje_servidor = "Se ha cerrado la calculadora."
            enviar_mensaje = str.encode(mensaje_servidor)
            clientsocket.send(enviar_mensaje)
            clientsocket.close()
            break

        elif mensaje_cliente[0] == "1":
            suma = int(mensaje_cliente[1]) + int(mensaje_cliente[2])
            send_bytes = str.encode(str(suma))
            clientsocket.send(send_bytes)

        elif mensaje_cliente[0] == "2":
            multiplica = int(mensaje_cliente[1]) * int(mensaje_cliente[2])
            send_bytes = str.encode(str(multiplica))
            clientsocket.send(send_bytes)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP

try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Esperando conexión con %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
except KeyboardInterrupt:
    print("\n Se ha cerrado la conexión.")
except IndexError:
    print("Se deben introducir 3 números separados por comas.")
