import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# 1. Crear un dataset de ejemplo
data = {
    'task': [
        'Enviar correo al jefe',
        'Comprar suministros de oficina',
        'Revisar el reporte mensual',
        'Asistir a reunión del equipo',
        'Actualizar el software del sistema',
        'Preparar la presentación del proyecto',
        'Pagar las facturas',
        'Revisar contratos legales',
        'Planificar el evento anual',
        'Llamar al cliente importante'
    ],
    'priority': ['baja', 'baja', 'media', 'alta', 'media', 'alta', 'baja', 'media', 'media', 'alta']
}

df = pd.DataFrame(data)

# 2. Crear un diccionario de palabras clave y prioridades
keywords = {
    'asistir': 'alta',
    'revisar': 'media',
    'enviar': 'baja',
    'comprar': 'baja',
    'actualizar': 'media',
    'preparar': 'alta',
    'pagar': 'baja',
    'planificar': 'media',
    'llamar': 'alta'
}

# 3. Crear una función para asignar prioridad basada en palabras clave
def assign_priority(task):
    global keywords
    task_lower = task.lower()
    for word, priority in keywords.items():
        if word in task_lower:
            return priority

    # Si no encuentra una palabra clave, preguntar al usuario
    print(f"No se encontró una palabra clave en la tarea: '{task}'")
    new_priority = input("Por favor, asigna una prioridad ('baja', 'media', 'alta') para esta tarea: ").strip().lower()
    while new_priority not in ['baja', 'media', 'alta']:
        new_priority = input("Entrada no válida. Por favor, asigna una prioridad válida ('baja', 'media', 'alta'): ").strip().lower()

    # Agregar nueva palabra clave al diccionario
    new_word = input("Por favor, introduce la palabra clave que representa esta tarea: ").strip().lower()
    keywords[new_word] = new_priority
    print(f"Se ha añadido la palabra clave '{new_word}' con prioridad '{new_priority}' al sistema.")
    return new_priority

# 4. Asignar prioridad usando la función
df['priority'] = df['task'].apply(assign_priority)

# 5. Convertir las etiquetas de prioridad en valores numéricos
df['priority_label'] = df['priority'].map({'baja': 0, 'media': 1, 'alta': 2})

# 6. Probar con entradas dinámicas del usuario
def predict_priority(task):
    priority = assign_priority(task)
    return priority

while True:
    user_task = input("Introduce una actividad (o escribe 'salir' para terminar): ").strip()
    if user_task.lower() == 'salir':
        print("Saliendo del programa. ¡Adiós!")
        break
    print(f"La prioridad de la tarea '{user_task}' es: {predict_priority(user_task)}")
