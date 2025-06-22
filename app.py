# TP 6 - Estructuras de Datos Complejas - UTN A Distancia
# Alumno: [Tu Nombre]

# 1. Agregar frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2. Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario actualizado:", precios_frutas)

# 3. Lista solo con nombres de frutas
solo_frutas = list(precios_frutas.keys())
print("Solo frutas:", solo_frutas)

# 4. Agenda telefónica simple
agenda = {}
for _ in range(5):
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    agenda[nombre] = telefono

consulta = input("¿Qué contacto querés consultar?: ")
if consulta in agenda:
    print("Número:", agenda[consulta])
else:
    print("Ese contacto no está en la agenda.")

# 5. Análisis de frase con set y diccionario
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", conteo)

# 6. Promedio de notas de 3 alumnos
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} tiene un promedio de {promedio:.2f}")

# 7. Sets de aprobados en Parcial 1 y 2
parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {3, 4, 6, 7}

ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8. Stock de productos
stock = {
    "arroz": 10,
    "fideos": 5,
    "azúcar": 8
}

producto = input("Producto a consultar o agregar: ")

if producto in stock:
    cantidad = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += cantidad
else:
    nuevo_stock = int(input("Producto nuevo, ¿cuántas unidades tiene?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# 9. Agenda con tuplas como claves
agenda_eventos = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de Python",
    ("Viernes", "20:00"): "Cena"
}

dia = input("Ingresá el día: ").capitalize()
hora = input("Ingresá la hora (formato HH:MM): ")

evento = agenda_eventos.get((dia, hora), "No hay evento agendado.")
print(f"Evento para {dia} a las {hora}: {evento}")

# 10. Invertir diccionario de países y capitales
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago"
}

capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
