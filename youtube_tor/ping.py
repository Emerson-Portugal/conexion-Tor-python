from ping3 import ping, verbose_ping

# Ejemplo de uso de la función ping para enviar un único paquete de ping
ip = "45.60.22.126"  # Cambia esta dirección IP por la que deseas hacer ping
response_time = ping(ip)
if response_time is not None:
    print(f"Respuesta desde {ip}: tiempo = {response_time} ms")
else:
    print(f"Sin respuesta de {ip}")

# Ejemplo de uso de la función verbose_ping para enviar múltiples paquetes de ping y mostrar información detallada
ip = "8.8.8.8"  # Cambia esta dirección IP por la que deseas hacer ping
verbose_ping(ip, count=4)  # Envia 4 paquetes de ping a la dirección IP especificada
