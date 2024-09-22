# Esto es un comentario... 
print("Hola Mundo!")
print("Hola Python!")

nombre = input("Ingrese su nombre: ")

print("Hola " + nombre)

numero1 = 20
numero2 = 43

promedio = (numero1 + numero2) / 2

print("El promedio es: " , promedio)

costo_servicio  = 1000
# me falta calcular los impuestos...
# iva 21%
costo_servicio_iva = costo_servicio * 0.21
# PAIS 8%
costo_servicio_pais = costo_servicio * 0.08
#Ganancias 30%
costo_servicio_ganancias = costo_servicio * 0.30
# IIBB CABA 2%
costo_servicio_iibb = costo_servicio * 0.02

valor_final = costo_servicio + costo_servicio_iva
print("El valor final a pagar es: ", valor_final)
