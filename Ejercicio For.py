
tabla = int(input("Ingresa el número para ver su tabla de multiplicar: "))
print(f"\nTabla de multiplicar del {tabla}:")
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")
