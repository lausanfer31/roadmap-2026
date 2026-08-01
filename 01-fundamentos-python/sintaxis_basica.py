# ==========================================
# 1. VARIABLES Y TIPOS DE DATOS
# ==========================================
# En Python no necesitas declarar el tipo (es dinámico).

nombre = "Laura"             # String (texto)
edad = 19                    # Integer (entero)
promedio = 4.2               # Float (decimal)
es_estudiante = True         # Boolean (Verdadero/Falso)

# Imprimir en pantalla con f-strings (f"...")
print(f"Hola, soy {nombre} y tengo {edad} años.")


# ==========================================
# 2. ESTRUCTURAS DE DATOS BÁSICAS
# ==========================================

# A) Listas (List): Ordenadas, mutables (se pueden cambiar)
materias = ["Estructura de Lenguajes", "Ingeniería de Software II", "Estadística"]
materias.append("Bases de Datos II")  # Agregar al final
print(f"Primera materia: {materias[0]}")  # Los índices empiezan en 0

# B) Diccionarios (Dict): Clave - Valor (súper importante para bases de datos/JSON)
estudiante = {
    "nombre": "Laura",
    "carrera": "Ingeniería de Sistemas",
    "semestre": 6
}
print(f"Carrera: {estudiante['carrera']}")


# ==========================================
# 3. CONDICIONALES (CONTROL DE FLUJO)
# ==========================================
# ¡OJO! En Python NO hay llaves {}. La estructura se define por INDENTACIÓN (4 espacios/Tab).

nota = 3.8

if nota >= 4.0:
    print("Excelente desempeño")
elif nota >= 3.0:
    print("Materia aprobada")
else:
    print("Debes recuperar la materia")


# ==========================================
# 4. BUCLES (LOOPS)
# ==========================================

# Recorrer una lista con 'for'
print("\nMis materias este semestre:")
for m in materias:
    print(f"- {m}")

# Repetir N veces con range()
print("\nConteo de prueba:")
for i in range(1, 4):  # Del 1 al 3
    print(f"Número: {i}")


# ==========================================
# 5. FUNCIONES Y REUTILIZACIÓN
# ==========================================
# Se definen con la palabra reservada 'def'

def calcular_promedio(notas_lista):
    """Suma todas las notas y devuelve el promedio."""
    suma = sum(notas_lista)
    total_notas = len(notas_lista)
    return suma / total_notas

# Probar la función
mis_notas = [4.5, 3.8, 4.2, 5.0]
resultado = calcular_promedio(mis_notas)
print(f"\nTu promedio final es: {resultado}")

''' Una vez lo pruebes y veas la salida en pantalla, edita tu archivo al final y escribe tú sola una función 
que haga lo siguiente:

Crea una función llamada es_par(numero).

Que reciba un número entero como parámetro.

Si el número es par (pista: usa el operador módulo % 2 == 0), debe imprimir "El número es par".

Si no, debe imprimir "El número es impar".

Pruébala llamándola dos veces con números diferentes (ejemplo: es_par(8) y es_par(7)).'''

def es_par(numero):
    #dice si un numero es par o impar
    if numero % 2 == 0:
        print("numero es par")
    else:
        print("numero es impar")  
        
es_par(8)
es_par(7)