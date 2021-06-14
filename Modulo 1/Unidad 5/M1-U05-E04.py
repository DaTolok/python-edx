# Ejemplo 4
import urllib.request
url = 'https://www.google.com'
 
# response almacena la respuesta a la solicitud hecha a la URL
response = urllib.request.urlopen(url)
print("response: ")
print(type(response))
print()
 
# Lectura de la respuesta obtenida 
print("read(): ")
print(response.read())
print()
 
# HTTP Status
print("getcode(): ")
print(response.getcode())
print()
 
# Verificación de la URL actual
print("geturl()")
print(response.geturl())
print()
 
# Obtención de encabezados HTTP
print("getheaders()")
print(response.getheaders())
print()
 
# Obtención del encabezado específico ‘content type’
print("getheader()")
print(response.getheader("Content-Type"))