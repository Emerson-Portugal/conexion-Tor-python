import requests

url = input("Ingresa tu URL: ")

try:
    response = requests.get(url, allow_redirects=True)
    # Lanza una excepción para errores HTTP
    response.raise_for_status()  

    # Imprimir la respuesta
    print(f"HTTP/1.0 {response.status_code} {response.reason}")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")
