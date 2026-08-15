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

# ==============================================================================
# 6. ADVANCED LIST OPERATIONS & CLEAN CODE HEURISTICS
# ==============================================================================

# HEURISTIC: Use plural nouns for lists (e.g., 'prices', 'active_users').
product_prices = [10.5, 20.0, 15.75, 5.99]

# 6.1 Adding and removing elements
product_prices.append(30.0)      # Adds 30.0 to the end of the list
last_price = product_prices.pop() # Removes and returns the LAST element (useful for Stacks!)
product_prices.insert(0, 9.99)   # Inserts 9.99 at index 0 (the beginning)

# 6.2 Getting both INDEX and VALUE using enumerate()
# HEURISTIC: When you need the position of an item, use 'enumerate' instead of range(len()).
# It is much more readable and considered "Pythonic".
print("\n--- Product Prices ---")
for index, price in enumerate(product_prices):
    print(f"Item #{index}: ${price}")

# 6.3 List Comprehensions (Creating lists in one line)
# HEURISTIC: Use list comprehensions for simple filtering or math operations.
# Syntax: [expression for item in list if condition]

# Example: Create a new list with prices greater than $15
expensive_products = [price for price in product_prices if price > 15.0]


# ==============================================================================
# 7. ADVANCED DICTIONARY OPERATIONS
# ==============================================================================

# HEURISTIC: Use singular nouns for dictionaries representing ONE entity.
user_profile = {
    "username": "lausanfer31",
    "role": "Backend Engineer",
    "reputation_score": 98
}

# 7.1 Safely accessing values using .get()
# If you use user_profile["email"] and the key doesn't exist, the program crashes.
# If you use .get(), it returns 'None' (or a default value you set) instead of crashing.
user_email = user_profile.get("email", "No email provided") 
print(f"\nUser Email: {user_email}")

# 7.2 Iterating through a dictionary using .items()
# .items() gives you both the KEY and the VALUE at the same time.
print("\n--- User Profile Details ---")
for key, value in user_profile.items():
    print(f"{key.capitalize()}: {value}")


# ==============================================================================
# 8. ESSENTIAL BUILT-IN FUNCTIONS FOR ALGORITHMS
# ==============================================================================

daily_temperatures = [22.5, 25.0, 19.8, 30.1, 21.0]

# Math helpers
max_temp = max(daily_temperatures)  # Returns the highest number (30.1)
min_temp = min(daily_temperatures)  # Returns the lowest number (19.8)

# Sorting
# sorted() returns a NEW sorted list without modifying the original one.
sorted_temperatures = sorted(daily_temperatures) 
# To sort in descending order (highest to lowest):
descending_temperatures = sorted(daily_temperatures, reverse=True)

# Zip function
# Combines two lists index by index into pairs. Extremely useful!
student_names = ["Laura", "Carlos", "Ana"]
final_grades = [4.5, 3.2, 5.0]

print("\n--- Final Results ---")
for name, grade in zip(student_names, final_grades):
    print(f"{name} achieved a score of {grade}")


# ==============================================================================
# 9. ERROR HANDLING (TRY / EXCEPT)
# ==============================================================================
# HEURISTIC: Always anticipate things that can fail (like dividing by zero, 
# or reading a file that doesn't exist) so your program doesn't crash.

def calculate_division(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
        return 0
    except TypeError:
        print("Error: Please provide numbers, not text.")
        return 0

# ==============================================================================
# 10. BASICS OF CLASSES & OBJECTS (PREPARATION FOR DATA STRUCTURES)
# ==============================================================================
# HEURISTIC: Class names must use PascalCase (CapitalizeEveryWord).
# Methods inside a class must use snake_case.

class BankAccount:
    # The __init__ method is the "constructor". It runs when you create a new account.
    def __init__(self, owner_name, initial_balance):
        # 'self' refers to the specific object being created.
        self.owner_name = owner_name
        self.balance = initial_balance
        
        # HEURISTIC: Booleans should start with is_, has_, or can_.
        self.is_active = True 

    # A method inside the class
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

# Creating an object (Instance of the class)
my_account = BankAccount(owner_name="Laura Sanchez", initial_balance=1000)
my_account.deposit_money(500)