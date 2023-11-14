from torpy import TorClient
from urllib.parse import urlparse

url = input("Ingresa tu URL: ")

parsed_url = urlparse(url)

if parsed_url.scheme != 'http':
    print("Error: Solo se admiten URLs con el esquema 'http'.")
else:

    # Extraer el hostname del URL
    hostname = parsed_url.netloc
    # Se define el puerto para el servicio http
    port = 80

    with TorClient() as tor:
        # Elegir un nodo de entrada aleatorio y crea un circuito de 3 saltos
        with tor.create_circuit(3) as circuit:
            # Crear un flujo Tor hacia el host
            with circuit.create_stream((hostname, port)) as stream:
                # Consulta "GET" por medio de Tor
                stream.send(f'GET {parsed_url.path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n'.encode())
                recv = stream.recv(1024)

    print(recv.decode())
