"""El Reto: Analizador de Notas de EstudiantesEscribe una función llamada 
analizar_estudiantes(lista_estudiantes) que reciba una lista de diccionarios. 
Cada diccionario representa a un estudiante con su nombre y una lista de notas.
Entrada de prueba que puedes usar:Pythonestudiantes = [
    {"nombre": "Laura", "notas": [4.5, 3.8, 4.2]},
    {"nombre": "Carlos", "notas": [2.5, 3.0, 2.8]},
    {"nombre": "Ana", "notas": [4.0, 4.8, 5.0]}
]
Lo que debe hacer tu función:Recorrer la lista con un bucle for.
Calcular el promedio de notas de cada estudiante.Imprimir el nombre del estudiante y
su promedio redondeado a un decimal (puedes usar round(promedio, 1)).
Retornar una nueva lista que contenga únicamente los nombres de los estudiantes que 
aprobaron (promedio $\ge 3.0$)."""

# ==============================================================================
# DATA STRUCTURE: A List of Dictionaries
# 'students' is a LIST containing 3 DICTIONARIES.
# Each Dictionary has keys: "name" (String) and "grades" (List of Floats).
# ==============================================================================
students = [
    {"name": "Laura", "grades": [4.5, 3.8, 4.2]},
    {"name": "Carlos", "grades": [2.5, 3.0, 2.8]},
    {"name": "Ana", "grades": [4.0, 4.8, 5.0]}
]

def analyze_students(student_list):
    # STEP 1: Initialize an empty list to store the names of students who pass
    passed_students = []
    
    # STEP 2: Loop through the list 'student_list'. 
    # In each iteration, 'student' is a single DICTIONARY representing one person.
    for student in student_list:
        
        # STEP 3: Access the "grades" key inside the current student's dictionary.
        # 'grades' becomes a LIST of numbers (e.g., [4.5, 3.8, 4.2]).
        grades = student["grades"]
        
        # STEP 4: Calculate the average using sum() and len().
        average = sum(grades) / len(grades)
        
        # STEP 5: Round the result to 1 decimal place.
        rounded_average = round(average, 1)
        
        # STEP 6: Condition - If the student's average is >= 3.0,
        # extract their "name" from the dictionary and add (.append) it to 'passed_students'.
        if rounded_average >= 3.0:
            passed_students.append(student["name"])
            
    # STEP 7: Return the final list containing only the names ["Laura", "Ana"].
    # NOTE: 'return' is placed OUTSIDE the for-loop (same indentation as 'for').
    return passed_students


# ==============================================================================
# FUNCTION EXECUTION
# We call analyze_students() passing 'students' as the argument.
# ==============================================================================
result = analyze_students(students)

# Prints: passed students: ['Laura', 'Ana']
print(f"passed students: {result}")