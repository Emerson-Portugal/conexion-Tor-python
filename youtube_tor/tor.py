from ping3 import ping, verbose_ping
from torpy.http.requests import TorRequests

# Inicializar la conexión Tor
print("hola")
with TorRequests() as tor_requests:
    with tor_requests.get_session() as sess:
        # Hacer ping a una dirección IP específica
        ip = "192.168.1.1"  # Cambia esta dirección IP por la que deseas hacer ping
        response_time = ping(ip)
        if response_time is not None:
            print(f"Respuesta desde {ip}: tiempo = {response_time} ms")
        else:
            print(f"Sin respuesta de {ip}")

        # Hacer ping a una dirección IP específica y mostrar información detallada
        ip = "8.8.8.8"  # Cambia esta dirección IP por la que deseas hacer ping
        verbose_ping(ip, count=4)

        # Hacer una solicitud HTTP a través de Tor
        print(sess.get("http://ip-api.com/json").json())
