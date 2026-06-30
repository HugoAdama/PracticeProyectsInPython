#ENUNCIADO DEL EXAMEN DE PYTHON 1
#En el contexto del desarrollo de un juego de rol, se te ha asignado la tarea de manipular y gestionar una base de datos de personajes. 
# Esta base de datos está organizada como una lista de tuplas, 
# donde cada tupla representa un personaje y contiene los siguientes datos: 
# Nombre, Edad, Clase, Raza, Nivel, y un booleano que indica si el personaje está en el equipo.
#A continuación, se te exige que implementes una serie de funciones que permitan realizar distintas operaciones con esta base de datos.
#Considera que los niveles empezarán por 1.
#Nota revisar bien la indexacion del codigo para que no exista errores de sintaxis.
#Se podra agregar funciones adicionales para complementar a la comodidad del estudiante
#Tiempo de duracion 1h y 30 min
#Enviar la solucion por la plataforma y adjuntar un video explicativo
"""
Ejercicio 1: Calcular el nivel medio del equipo (1 Punto)
Escribe una función que calcule el nivel medio del equipo, devolviendo la parte entera.
Ejercicio 2: Filtrar personajes en el equipo (1 Punto)
Escribe una función que devuelva una lista con los personajes que actualmente están en el equipo.
Ejercicio 3: Conjunto de clases únicas (1 Punto)
Escribe una función para crear una estructura con todas las clases únicas de los personajes, no puede haber elementos repetidos.
Ejercicio 4: Conteo de Personajes por Raza (1 Punto)
Escribe una función que cuente cuántos personajes hay de cada raza y devuelva esta información en forma de diccionario.
Ejercicio 5: Verificación de Existencia de Raza (1 Punto)
Escribe una función que verifique si existe al menos un personaje de una raza específica en la lista, devolviendo True o False.
La búsqueda debe detenerse tan pronto como se encuentre un personaje de la raza indicada.
Ejercicio 6: Personaje con Mayor Nivel (1.5 Puntos)
Escribe una función que encuentre el nombre del primer personaje de mayor nivel dentro de una clase especificada. 
El parámetro de la clase debe tener un valor por defecto de None, permitiendo que, si no se especifica una clase,
la función devuelva el nombre del personaje con mayor nivel general.
Ejercicio 7: Incrementar Nivel de un Personaje (1.5 Puntos)
Escribe una función que, dado un nombre, incremente en uno el nivel del personaje correspondiente sin devolver nada.
Ejercicio 8: Programa un juego - Adivina la edad del personaje (2 Puntos)
Solicita por consola el nombre de un personaje. 
Luego haz que introduzca una edad hasta acertar con la edad del personaje cuyo nombre sea igual al introducido. 
Debe informar si acierta, o si el personaje es mayor o menor a la edad introducida. 
Además, si la edad introducida es 0, haz que termine el juego inmediatamente con el siguiente mensaje Interrupción por el jugador

# Nombre, Edad, Clase, Raza, Nivel, y un booleano que indica si el personaje está en el equipo.

personajes_principales = [
    #Posicion 0, 1, 2, 3, 4, 5
    ("Astarion", 239, "Rogue", "Elf", 3, True),
    ("Shadowheart", 40, "Cleric", "Half-Elf", 5, True),
    ("Wyll", 25, "Warlock", "Human", 2, False),
    ("Gale", 35, "Wizard", "Human", 5, True),
    ("Karlach", 32, "Barbarian", "Tiefling", 6, False),
    ("Lae'zel", 20, "Fighter", "Githyanki", 4, True),
    ("Jaheira", 150, "Druid", "Half-Elf", 6, False),
    ("Halsin", 350, "Druid", "Elf", 7, False),
    ("Minsc", 130, "Ranger", "Human", 5, False),
    ("Minthara", 250, "Paladin", "Drow", 8, False),
    ("Dark Urge", 30, "Sorcerer", "Dragonborn", 1, False)
]
"""
#SOLUCION 
"""
============================================================
🎮 SISTEMA DE GESTIÓN DE PERSONAJES - JUEGO DE ROL
============================================================
Este programa gestiona una base de datos de personajes de un juego de rol.
Cada personaje está representado por una tupla con:
- Nombre, Edad, Clase, Raza, Nivel, Booleano (en equipo)

El programa implementa 8 funciones principales que permiten:
1. Calcular estadísticas del equipo
2. Filtrar personajes
3. Analizar clases y razas
4. Buscar personajes específicos
5. Modificar niveles
6. Jugar a adivinar edades

Autor: [Shito Akayama]
============================================================
"""

# ============================================================
# BASE DE DATOS DE PERSONAJES
# ============================================================
# Lista de tuplas donde cada tupla representa un personaje
# Índices: 0-Nombre, 1-Edad, 2-Clase, 3-Raza, 4-Nivel, 5-EnEquipo
# ============================================================
personajes_principales = [
    #Posicion 0, 1, 2, 3, 4, 5
    ("Astarion", 239, "Rogue", "Elf", 3, True),        # Personaje 1: Elfo pícaro
    ("Shadowheart", 40, "Cleric", "Half-Elf", 5, True), # Personaje 2: Clériga medio-elfa
    ("Wyll", 25, "Warlock", "Human", 2, False),         # Personaje 3: Hechicero humano
    ("Gale", 35, "Wizard", "Human", 5, True),           # Personaje 4: Mago humano
    ("Karlach", 32, "Barbarian", "Tiefling", 6, False), # Personaje 5: Bárbara tiefling
    ("Lae'zel", 20, "Fighter", "Githyanki", 4, True),   # Personaje 6: Guerrera githyanki
    ("Jaheira", 150, "Druid", "Half-Elf", 6, False),    # Personaje 7: Druida medio-elfa
    ("Halsin", 350, "Druid", "Elf", 7, False),          # Personaje 8: Druida elfo
    ("Minsc", 130, "Ranger", "Human", 5, False),        # Personaje 9: Explorador humano
    ("Minthara", 250, "Paladin", "Drow", 8, False),     # Personaje 10: Paladín drow
    ("Dark Urge", 30, "Sorcerer", "Dragonborn", 1, False) # Personaje 11: Hechicero dragonborn
]

# ============================================================
# CONSTANTES PARA ACCEDER A LOS ELEMENTOS DE LA TUPLA
# ============================================================
# Definimos constantes para mejorar la legibilidad y mantenimiento
# En lugar de usar números (0,1,2,3,4,5), usamos nombres descriptivos
# ============================================================
NOMBRE_PERSONAJE = 0    # Índice del nombre en la tupla
EDAD_PERSONAJE = 1      # Índice de la edad en la tupla
CLASE_PERSONAJE = 2     # Índice de la clase en la tupla
RAZA_PERSONAJE = 3      # Índice de la raza en la tupla
NIVEL_PERSONAJE = 4     # Índice del nivel en la tupla
EN_EQUIPO = 5           # Índice del booleano "en equipo" en la tupla

# ============================================================
# MENÚ PRINCIPAL
# ============================================================
# El menú principal es el corazón del programa.
# Permite al usuario navegar entre los 8 ejercicios implementados.
# Usa un bucle while True para mantener el programa corriendo
# hasta que el usuario decida salir.
# ============================================================

def mostrar_menu_principal():
    """
    Muestra el menú principal con todas las opciones disponibles.
    Esta función solo se encarga de la presentación visual.
    Usa emojis para hacer el menú más amigable y atractivo.
    """
    print("\n" + "="*60)
    print("🎮 SISTEMA DE GESTIÓN DE PERSONAJES - MENÚ PRINCIPAL")
    print("="*60)
    print("1. 📊 Ejercicio 1 - Nivel medio del equipo")
    print("2. 👥 Ejercicio 2 - Filtrar personajes del equipo")
    print("3. 🎭 Ejercicio 3 - Clases únicas")
    print("4. 📈 Ejercicio 4 - Conteo de razas")
    print("5. 🔍 Ejercicio 5 - Verificar existencia de raza")
    print("6. 🏆 Ejercicio 6 - Personaje con mayor nivel")
    print("7. ⬆️ Ejercicio 7 - Incrementar nivel de personaje")
    print("8. 🎯 Ejercicio 8 - Juego adivina la edad")
    print("0. 🚪 Salir")
    print("-"*60)

def menu_principal(personajes):
    """
    Controla la navegación del programa.
    - Recibe la lista de personajes como parámetro
    - Usa un bucle infinito que solo termina con la opción 0
    - Cada opción llama a la función correspondiente
    - Maneja errores con try/except para evitar que el programa falle
    
    Parámetros:
    - personajes: Lista de tuplas con los datos de los personajes
    """
    while True:
        mostrar_menu_principal()
        
        try:
            # Solicita la opción al usuario y elimina espacios en blanco
            opcion = input("🔍 Selecciona una opción (0-8): ").strip()
            
            # ========== OPCIÓN 0: SALIR ==========
            if opcion == "0":
                print("\n👋 ¡Gracias por usar el sistema! ¡Hasta luego!")
                break
            
            # ========== OPCIÓN 1: NIVEL MEDIO DEL EQUIPO ==========
            # Calcula el promedio de niveles de los personajes que están en el equipo
            # Usa división entera (//) para obtener solo la parte entera
            elif opcion == "1":
                print("\n" + "="*50)
                print("📊 EJERCICIO 1: Nivel medio del equipo")
                print("="*50)
                resultado = calcular_nivel_medio_team(personajes)
                print(f"\n✅ El nivel medio del equipo es: {resultado}")
                input("\nPresiona Enter para continuar...")
            
            # ========== OPCIÓN 2: FILTRAR PERSONAJES DEL EQUIPO ==========
            # Filtra y muestra solo los personajes que tienen EN_EQUIPO = True
            # Útil para saber quiénes están activos en el equipo
            elif opcion == "2":
                print("\n" + "="*50)
                print("👥 EJERCICIO 2: Filtrar personajes del equipo")
                print("="*50)
                equipo = filtrar_personajes(personajes)
                print(f"\n✅ Personajes en el equipo ({len(equipo)}):")
                for personaje in equipo:
                    print(f"  • {personaje[NOMBRE_PERSONAJE]} - {personaje[CLASE_PERSONAJE]} (Nivel {personaje[NIVEL_PERSONAJE]})")
                input("\nPresiona Enter para continuar...")
            
            # ========== OPCIÓN 3: CLASES ÚNICAS ==========
            # Usa un conjunto (set) para eliminar duplicados automáticamente
            # Los sets en Python no permiten elementos repetidos
            elif opcion == "3":
                print("\n" + "="*50)
                print("🎭 EJERCICIO 3: Clases únicas")
                print("="*50)
                clases = clases_unicas(personajes)
                print(f"\n✅ Clases únicas encontradas ({len(clases)}):")
                for clase in sorted(clases):  # sorted() ordena alfabéticamente
                    print(f"  • {clase}")
                input("\nPresiona Enter para continuar...")
            
            # ========== OPCIÓN 4: CONTEO DE RAZAS ==========
            # Crea un diccionario donde la clave es la raza y el valor el contador
            # Ejemplo: {"Human": 3, "Elf": 2, ...}
            elif opcion == "4":
                print("\n" + "="*50)
                print("📈 EJERCICIO 4: Conteo de personajes por raza")
                print("="*50)
                conteo = contar_personajes_raza(personajes)
                print("\n✅ Conteo de razas:")
                for raza, cantidad in sorted(conteo.items()):
                    print(f"  • {raza}: {cantidad} personaje(s)")
                input("\nPresiona Enter para continuar...")
            
            # ========== OPCIÓN 5: VERIFICAR EXISTENCIA DE RAZA ==========
            # Búsqueda eficiente: se detiene en cuanto encuentra la raza
            # Esto es más rápido que buscar en toda la lista
            elif opcion == "5":
                print("\n" + "="*50)
                print("🔍 EJERCICIO 5: Verificar existencia de raza")
                print("="*50)
                raza_buscada = input("\nIntroduce una raza para buscar: ").strip()
                if not raza_buscada:  # Si el usuario no escribe nada, usa "Human" por defecto
                    raza_buscada = "Human"
                existe = verificar_raza(personajes, raza_buscada)
                print(f"\n✅ ¿Existe al menos un personaje de la raza '{raza_buscada}'? {existe}")
                input("\nPresiona Enter para continuar...")
            
            # ========== OPCIÓN 6: PERSONAJE CON MAYOR NIVEL ==========
            # Encuentra el personaje con el nivel más alto
            # Permite filtrar por clase específica o buscar en general
            # Devuelve todos los detalles del personaje encontrado
            elif opcion == "6":
                print("\n" + "="*50)
                print("🏆 EJERCICIO 6: Personaje con mayor nivel")
                print("="*50)
                clase_input = input("\nIntroduce una clase (deja en blanco para nivel general): ").strip()
                
                if clase_input:
                    # Busca el personaje con mayor nivel en la clase especificada
                    personaje = encontrar_mayor_nivel(personajes, clase_input)
                    if personaje:
                        print(f"\n✅ Personaje con mayor nivel en la clase '{clase_input}':")
                        print(f"   📛 Nombre: {personaje[NOMBRE_PERSONAJE]}")
                        print(f"   📊 Nivel: {personaje[NIVEL_PERSONAJE]}")
                        print(f"   🎭 Clase: {personaje[CLASE_PERSONAJE]}")
                        print(f"   🧬 Raza: {personaje[RAZA_PERSONAJE]}")
                        print(f"   📅 Edad: {personaje[EDAD_PERSONAJE]} años")
                        if personaje[EN_EQUIPO]:
                            print(f"   ⭐ En el equipo: Sí")
                        else:
                            print(f"   ⭐ En el equipo: No")
                    else:
                        print(f"\n❌ No se encontraron personajes de la clase '{clase_input}'")
                else:
                    # Busca el personaje con mayor nivel general (sin filtrar por clase)
                    personaje = encontrar_mayor_nivel(personajes)
                    if personaje:
                        print(f"\n✅ Personaje con mayor nivel general:")
                        print(f"   📛 Nombre: {personaje[NOMBRE_PERSONAJE]}")
                        print(f"   📊 Nivel: {personaje[NIVEL_PERSONAJE]}")
                        print(f"   🎭 Clase: {personaje[CLASE_PERSONAJE]}")
                        print(f"   🧬 Raza: {personaje[RAZA_PERSONAJE]}")
                        print(f"   📅 Edad: {personaje[EDAD_PERSONAJE]} años")
                        if personaje[EN_EQUIPO]:
                            print(f"   ⭐ En el equipo: Sí")
                        else:
                            print(f"   ⭐ En el equipo: No")
                    else:
                        print("\n❌ No hay personajes disponibles")
                input("\nPresiona Enter para continuar...")
            
            # ========== OPCIÓN 7: INCREMENTAR NIVEL ==========
            # Modifica la lista original (efecto permanente)
            # Usa un menú secundario para seleccionar el personaje
            elif opcion == "7":
                print("\n" + "="*50)
                print("⬆️ EJERCICIO 7: Incrementar nivel de personaje")
                print("="*50)
                menu_incrementar_nivel(personajes)
            
            # ========== OPCIÓN 8: JUEGO ADIVINA EDAD ==========
            # Juego interactivo donde el usuario adivina la edad
            # Usa un bucle while para intentos múltiples
            # Termina cuando acierta o escribe 0
            elif opcion == "8":
                print("\n" + "="*50)
                print("🎯 EJERCICIO 8: Juego - Adivina la edad")
                print("="*50)
                juego_adivina_edad(personajes)
            
            # ========== OPCIÓN INVÁLIDA ==========
            else:
                print("\n❌ Opción inválida. Por favor, selecciona una opción del 0 al 8.")
                input("\nPresiona Enter para continuar...")
        
        # Manejo de interrupción del usuario (Ctrl+C)
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        # Manejo de cualquier otro error inesperado
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("\nPresiona Enter para continuar...")

# ============================================================
# EJERCICIO 1: Calcular el nivel medio del equipo
# ============================================================
# OBJETIVO: Calcular el promedio de niveles de los personajes en el equipo
# LÓGICA:
# 1. Recorremos todos los personajes
# 2. Solo consideramos los que están en el equipo (EN_EQUIPO = True)
# 3. Sumamos los niveles de esos personajes
# 4. Contamos cuántos son
# 5. Dividimos la suma entre el contador (división entera)
# 6. Si no hay personajes en el equipo, devolvemos 0
# ============================================================

def calcular_nivel_medio_team(personajes):
    """
    Calcula el nivel medio de los personajes que están en el equipo.
    
    Args:
        personajes: Lista de tuplas con datos de personajes
    
    Returns:
        int: Parte entera del nivel medio (división entera)
    
    Ejemplo:
        Si los niveles en equipo son [3, 5, 5, 4], la media es 17/4 = 4
    """
    suma_niveles = 0  # Acumulador para sumar todos los niveles
    contador = 0      # Contador para saber cuántos personajes hay en el equipo
    
    # Recorremos cada personaje en la lista
    for personaje in personajes:
        # Verificamos si el personaje está en el equipo (posición 5)
        if personaje[EN_EQUIPO]:
            suma_niveles += personaje[NIVEL_PERSONAJE]  # Sumamos su nivel
            contador += 1  # Incrementamos el contador
    
    # Si hay personajes en el equipo, calculamos la media
    # Usamos división entera (//) para obtener solo la parte entera
    # Si no hay personajes, devolvemos 0 para evitar división entre cero
    return suma_niveles // contador if contador > 0 else 0

# ============================================================
# EJERCICIO 2: Filtrar personajes en el equipo
# ============================================================
# OBJETIVO: Obtener una lista solo con los personajes que están en el equipo
# LÓGICA:
# 1. Creamos una lista vacía para almacenar los personajes del equipo
# 2. Recorremos todos los personajes
# 3. Si el personaje está en el equipo (EN_EQUIPO = True), lo agregamos
# 4. Devolvemos la nueva lista
# ============================================================

def filtrar_personajes(personajes):
    """
    Filtra y devuelve solo los personajes que están en el equipo.
    
    Args:
        personajes: Lista de tuplas con datos de personajes
    
    Returns:
        list: Nueva lista con los personajes que tienen EN_EQUIPO = True
    
    Ejemplo:
        Si hay 11 personajes y 4 están en el equipo, devuelve esos 4
    """
    personajes_team = []  # Lista vacía para almacenar los personajes del equipo
    
    # Recorremos todos los personajes
    for personaje in personajes:
        # Si el personaje está en el equipo (posición 5 = True)
        if personaje[EN_EQUIPO]:
            personajes_team.append(personaje)  # Lo agregamos a la nueva lista
    
    return personajes_team  # Devolvemos la lista filtrada

# ============================================================
# EJERCICIO 3: Conjunto de clases únicas
# ============================================================
# OBJETIVO: Encontrar todas las clases diferentes sin repetir
# LÓGICA:
# 1. Usamos un set (conjunto) que automáticamente elimina duplicados
# 2. Recorremos todos los personajes
# 3. Agregamos su clase al set
# 4. El set solo guarda valores únicos
# 5. Devolvemos el set con las clases únicas
# ============================================================

def clases_unicas(personajes):
    """
    Encuentra todas las clases únicas de los personajes.
    
    Args:
        personajes: Lista de tuplas con datos de personajes
    
    Returns:
        set: Conjunto con las clases únicas (sin repetir)
    
    Ejemplo:
        Si hay clases: "Rogue", "Cleric", "Wizard", "Rogue"
        Devuelve: {"Rogue", "Cleric", "Wizard"}
    """
    clases = set()  # Creamos un conjunto vacío (automáticamente elimina duplicados)
    
    # Recorremos todos los personajes
    for personaje in personajes:
        # Agregamos la clase al conjunto (posición 2)
        # Si ya existe, no se duplica
        clases.add(personaje[CLASE_PERSONAJE])
    
    return clases  # Devolvemos el conjunto con clases únicas

# ============================================================
# EJERCICIO 4: Conteo de Personajes por Raza
# ============================================================
# OBJETIVO: Contar cuántos personajes hay de cada raza
# LÓGICA:
# 1. Usamos un diccionario donde la clave es la raza y el valor es el contador
# 2. Recorremos todos los personajes
# 3. Si la raza ya existe en el diccionario, incrementamos su contador
# 4. Si la raza no existe, la agregamos al diccionario con valor 1
# ============================================================

def contar_personajes_raza(personajes):
    """
    Cuenta cuántos personajes hay de cada raza.
    
    Args:
        personajes: Lista de tuplas con datos de personajes
    
    Returns:
        dict: Diccionario con razas como claves y cantidades como valores
    
    Ejemplo:
        {"Human": 3, "Elf": 2, "Half-Elf": 2, "Tiefling": 1, ...}
    """
    conteo_raza = {}  # Diccionario vacío para almacenar el conteo
    
    # Recorremos todos los personajes
    for personaje in personajes:
        raza = personaje[RAZA_PERSONAJE]  # Obtenemos la raza (posición 3)
        
        # Si la raza ya está en el diccionario
        if raza in conteo_raza:
            conteo_raza[raza] += 1  # Incrementamos el contador en 1
        else:
            conteo_raza[raza] = 1   # Inicializamos el contador en 1
    
    return conteo_raza  # Devolvemos el diccionario con los conteos

# ============================================================
# EJERCICIO 5: Verificación de Existencia de Raza
# ============================================================
# OBJETIVO: Verificar si existe al menos un personaje de una raza específica
# LÓGICA:
# 1. Convertimos la raza a minúsculas para búsqueda sin distinción de mayúsculas
# 2. Recorremos los personajes
# 3. Si encontramos un personaje de esa raza, devolvemos True inmediatamente
# 4. Si terminamos el bucle sin encontrar, devolvemos False
# 5. LA BÚSQUEDA SE DETIENE TAN PRONTO COMO ENCUENTRA UNO (eficiencia)
# ============================================================

def verificar_raza(personajes, raza_buscada):
    """
    Verifica si existe al menos un personaje de una raza específica.
    La búsqueda se detiene en cuanto encuentra un personaje de esa raza.
    
    Args:
        personajes: Lista de tuplas con datos de personajes
        raza_buscada: String con la raza a buscar
    
    Returns:
        bool: True si existe al menos uno, False si no existe
    
    Ejemplo:
        verificar_raza(personajes, "Human") -> True (hay varios humanos)
        verificar_raza(personajes, "Dragon") -> False (no hay dragones)
    """
    raza_buscada = raza_buscada.lower()  # Convertimos a minúsculas para búsqueda flexible
    
    # Recorremos todos los personajes
    for personaje in personajes:
        # Comparamos la raza del personaje (posición 3) con la raza buscada
        # Ambos en minúsculas para evitar problemas con mayúsculas
        if personaje[RAZA_PERSONAJE].lower() == raza_buscada:
            return True  # Encontramos uno, devolvemos True y SALIMOS (eficiencia)
    
    # Si recorrimos todos los personajes y no encontramos ninguno
    return False

# ============================================================
# EJERCICIO 6: Personaje con Mayor Nivel
# ============================================================
# OBJETIVO: Encontrar el personaje con el nivel más alto
# LÓGICA:
# 1. Inicializamos variables para guardar el mejor personaje y su nivel
# 2. Recorremos todos los personajes
# 3. Si el personaje cumple con el filtro de clase (si se especifica)
# 4. Comparamos su nivel con el máximo actual
# 5. Si es mayor, actualizamos el máximo y guardamos el personaje
# 6. Devolvemos el personaje completo (tupla)
# ============================================================

def encontrar_mayor_nivel(personajes, clase=None):
    """
    Encuentra el personaje con el nivel más alto.
    Permite filtrar por clase específica o buscar en general.
    
    Args:
        personajes: Lista de tuplas con datos de personajes
        clase: String con la clase a filtrar (opcional, por defecto None)
    
    Returns:
        tuple: Tupla completa del personaje con mayor nivel
        None: Si no hay personajes o no se encuentra ninguno
    
    Ejemplo:
        encontrar_mayor_nivel(personajes) -> ("Minthara", 250, "Paladin", "Drow", 8, False)
        encontrar_mayor_nivel(personajes, "Druid") -> ("Halsin", 350, "Druid", "Elf", 7, False)
    """
    personaje_maximo = None  # Variable para guardar el mejor personaje
    nivel_maximo = 0         # Variable para guardar el nivel más alto encontrado
    
    # Recorremos todos los personajes
    for personaje in personajes:
        # Verificamos si el personaje cumple con el filtro de clase
        # Si clase es None, no filtramos (todos los personajes son válidos)
        # Si clase tiene un valor, solo consideramos personajes de esa clase
        if clase is None or personaje[CLASE_PERSONAJE] == clase:
            # Comparamos el nivel del personaje actual con el máximo encontrado
            if personaje[NIVEL_PERSONAJE] > nivel_maximo:
                # Si es mayor, actualizamos el máximo y guardamos el personaje
                personaje_maximo = personaje
                nivel_maximo = personaje[NIVEL_PERSONAJE]
    
    # Devolvemos el personaje con mayor nivel (o None si no hay)
    return personaje_maximo

# ============================================================
# EJERCICIO 7: Incrementar Nivel de un Personaje
# ============================================================
# OBJETIVO: Aumentar en 1 el nivel de un personaje específico
# LÓGICA:
# 1. Mostramos todos los personajes con su número y nivel actual
# 2. El usuario puede elegir por número o por nombre
# 3. Buscamos el personaje en la lista
# 4. Creamos una nueva tupla con el nivel incrementado en 1
# 5. Reemplazamos la tupla original en la lista
# 6. Mostramos un mensaje de confirmación
# 7. MODIFICA LA LISTA ORIGINAL (efecto permanente)
# ============================================================

def menu_incrementar_nivel(personajes):
    """
    Menú interactivo para incrementar el nivel de un personaje.
    Permite seleccionar por número o por nombre.
    
    Args:
        personajes: Lista de tuplas con datos de personajes (se modifica en el lugar)
    
    Nota: La función modifica la lista original (efecto permanente)
    """
    while True:
        print("\n" + "="*50)
        print("🎮 SUBIR DE NIVEL - Menú")
        print("="*50)
        
        # Mostramos todos los personajes disponibles con su número y nivel
        print("\n📊 Personajes disponibles:")
        for i, personaje in enumerate(personajes):
            # Indicamos con un ⭐ si el personaje está en el equipo
            en_equipo = "⭐" if personaje[EN_EQUIPO] else "  "
            print(f"  {i}. {en_equipo} {personaje[NOMBRE_PERSONAJE]} - Nivel: {personaje[NIVEL_PERSONAJE]} ({personaje[CLASE_PERSONAJE]})")
        
        print("\nOpciones:")
        print("  • Introduce el NÚMERO del personaje para subirlo de nivel")
        print("  • Escribe el NOMBRE para buscar por nombre")
        print("  • Escribe 'salir' para volver")
        
        opcion = input("\n🔍 Elige una opción: ").strip()
        
        # Opción para salir del menú
        if opcion.lower() == 'salir':
            print("👋 Saliendo del menú...")
            break
        
        # Si la opción es un número (selección por índice)
        if opcion.isdigit():
            indice = int(opcion)  # Convertimos a entero
            
            # Verificamos que el índice sea válido (0 <= indice < longitud de la lista)
            if 0 <= indice < len(personajes):
                # Obtenemos el personaje actual
                personaje_actual = personajes[indice]
                
                # Creamos una NUEVA TUPLA con el nivel incrementado en 1
                # Las tuplas son inmutables, por eso debemos crear una nueva
                personajes[indice] = (
                    personaje_actual[NOMBRE_PERSONAJE],     # Mantenemos el nombre
                    personaje_actual[EDAD_PERSONAJE],       # Mantenemos la edad
                    personaje_actual[CLASE_PERSONAJE],      # Mantenemos la clase
                    personaje_actual[RAZA_PERSONAJE],       # Mantenemos la raza
                    personaje_actual[NIVEL_PERSONAJE] + 1,  # ¡INCREMENTAMOS EL NIVEL!
                    personaje_actual[EN_EQUIPO],            # Mantenemos el estado del equipo
                )
                # Mostramos mensaje de confirmación
                print(f"\n✅ ¡{personaje_actual[NOMBRE_PERSONAJE]} subió al nivel {personaje_actual[NIVEL_PERSONAJE] + 1}!")
            else:
                print(f"\n❌ Número inválido. Debe ser entre 0 y {len(personajes) - 1}")
        else:
            # Si la opción NO es un número, la tratamos como nombre
            encontrado = False
            for i, personaje in enumerate(personajes):
                # Buscamos el nombre ignorando mayúsculas/minúsculas
                if personaje[NOMBRE_PERSONAJE].lower() == opcion.lower():
                    # Encontramos el personaje, lo incrementamos
                    personaje_actual = personajes[i]
                    personajes[i] = (
                        personaje_actual[NOMBRE_PERSONAJE],
                        personaje_actual[EDAD_PERSONAJE],
                        personaje_actual[CLASE_PERSONAJE],
                        personaje_actual[RAZA_PERSONAJE],
                        personaje_actual[NIVEL_PERSONAJE] + 1,
                        personaje_actual[EN_EQUIPO],
                    )
                    print(f"\n✅ ¡{personaje_actual[NOMBRE_PERSONAJE]} subió al nivel {personaje_actual[NIVEL_PERSONAJE] + 1}!")
                    encontrado = True
                    break  # Salimos del bucle después de encontrar y actualizar
            
            if not encontrado:
                print(f"\n❌ No se encontró al personaje '{opcion}'")

# ============================================================
# EJERCICIO 8: Juego - Adivina la Edad del Personaje
# ============================================================
# OBJETIVO: Crear un juego interactivo donde el usuario adivina la edad
# LÓGICA:
# 1. Solicita el nombre de un personaje
# 2. Busca el personaje en la lista
# 3. Si no existe, muestra mensaje y termina
# 4. Si existe, inicia un bucle de adivinanzas
# 5. El usuario introduce edades hasta acertar
# 6. Da pistas: "es mayor" o "es menor"
# 7. Si el usuario escribe 0, termina el juego
# 8. Si acierta, felicita y muestra el número de intentos
# ============================================================

def juego_adivina_edad(personajes):
    """
    Juego interactivo donde el usuario debe adivinar la edad de un personaje.
    El usuario ingresa edades y el programa da pistas (mayor/menor).
    
    Args:
        personajes: Lista de tuplas con datos de personajes
    
    Nota: El juego termina cuando el usuario acierta o escribe 0
    """
    # SOLICITAR NOMBRE DEL PERSONAJE
    nombre_buscado = input("\n🔍 Introduce el nombre del personaje: ").strip()
    
    # Validamos que el nombre no esté vacío
    if not nombre_buscado:
        print("❌ No ingresaste un nombre válido")
        return
    
    # BUSCAR EL PERSONAJE EN LA LISTA
    personaje_encontrado = None
    for personaje in personajes:
        # Buscamos ignorando mayúsculas/minúsculas
        if personaje[NOMBRE_PERSONAJE].lower() == nombre_buscado.lower():
            personaje_encontrado = personaje
            break  # Salimos del bucle al encontrar el personaje
    
    # Si no se encontró el personaje, mostramos mensaje y terminamos
    if not personaje_encontrado:
        print(f"❌ No se encontró ningún personaje con el nombre '{nombre_buscado}'")
        return
    
    # DESEMPAQUETAMOS LA TUPLA DEL PERSONAJE ENCONTRADO
    # Esto es más legible que usar índices numéricos
    nombre, edad_real, clase, raza, nivel, en_equipo = personaje_encontrado
    
    # Mostramos información del personaje (ocultamos la edad)
    print(f"\n🎯 ¡Encontrado! Adivina la edad de {nombre} (Clase: {clase}, Raza: {raza})")
    print("💡 Pista: Escribe 0 para salir del juego")
    
    # INICIAMOS EL JUEGO
    intentos = 0  # Contador de intentos
    
    # Bucle infinito que solo termina cuando acierta o escribe 0
    while True:
        try:
            # Solicitamos la edad al usuario
            edad_usuario = input(f"\n📝 Introduce una edad para {nombre}: ").strip()
            
            # VALIDACIONES DE ENTRADA
            if not edad_usuario:
                print("⚠️ Por favor, introduce un número")
                continue
            
            # Verificamos que sea un número (permite números negativos)
            if not edad_usuario.lstrip('-').isdigit():
                print("⚠️ Por favor, introduce un número válido")
                continue
            
            # Convertimos a entero
            edad_usuario = int(edad_usuario)
            intentos += 1  # Incrementamos el contador de intentos
            
            # CONDICIÓN DE SALIDA: si escribe 0
            if edad_usuario == 0:
                print("\n🛑 Interrupción por el jugador")
                break
            
            # COMPARAMOS LA EDAD INGRESADA CON LA EDAD REAL
            if edad_usuario == edad_real:
                # ¡ACERTÓ!
                print(f"\n🎉 ¡FELICIDADES! ¡Has acertado! {nombre} tiene {edad_real} años.")
                print(f"📊 Lo lograste en {intentos} intentos.")
                break  # Termina el juego
            elif edad_usuario < edad_real:
                # La edad ingresada es menor que la real
                print(f"⬆️ {nombre} es MAYOR que {edad_usuario} años. Sigue intentando.")
            else:  # edad_usuario > edad_real
                # La edad ingresada es mayor que la real
                print(f"⬇️ {nombre} es MENOR que {edad_usuario} años. Sigue intentando.")
        
        # Manejo de errores: si el usuario ingresa algo que no es número
        except ValueError:
            print("⚠️ Por favor, introduce un número válido")
        # Manejo de interrupción (Ctrl+C)
        except KeyboardInterrupt:
            print("\n🛑 Interrupción por el jugador")
            break

# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================
# Esta es la parte que se ejecuta cuando corremos el programa
# La condición if __name__ == "__main__": asegura que el código
# solo se ejecute si el archivo se corre directamente, no si se importa
# ============================================================

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Inicia el menú principal con los personajes cargados.
    """
    # Ejecutar el menú principal
    menu_principal(personajes_principales)