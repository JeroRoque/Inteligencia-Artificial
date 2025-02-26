import datetime
import random

# Datos de la tienda
nombre_tienda = "Coppel"
folio = random.randint(1000, 9999)  # Genera un número de folio único aleatorio
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora actual

# Solicitar datos al usuario
nombre = input("Ingresa tu nombre: ")
producto = input("Ingresa el nombre del producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))

# Aplicar descuento si corresponde
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
else:
    descuento = 0
    total_final = total_compra

# Impricket de compmir tira con formato
print("\n" + "="*40 + " TICKET DE COMPRA " + "="*40)
print(f"Tienda: {nombre_tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print("-"*80)
print(f"Cliente: {nombre}")
print(f"Producto: {producto}")
print(f"Total de la compra: ${total_compra:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
print("-"*80)
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("="*80)
