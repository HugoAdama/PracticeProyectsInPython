"""
CONSIGNA DUELO DE DADOS 
Crea un programa donde dos jugadores lancen dados y compitan por obtener más puntos.

Reglas:
El programa debe tener un dado de 6 caras.
Cada jugador lanza 3 dados.
Se suman los puntos obtenidos.
Gana quien tenga más puntos.
Si ambos tienen el mismo resultado, hay empate.
Al finalizar debe preguntar si desean jugar otra partida.

Extra:
Agregar niveles:
Fácil: 1 dado
Medio: 3 dados
Difícil: 5 dados
"""

# ========== LIBRERÍAS ==========
import random
import subprocess
import sys
import time
from playsound3 import playsound

# ========== FUNCIONES DE UTILIDAD ==========

def limpiar_pantalla():
    """Limpia la terminal usando el comando apropiado para cada SO."""
    if sys.platform.startswith('win'):
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear')

def pausa():
    input("\nPresiona Enter para continuar...")

def reproducir_sonido(ruta_archivo):
    """Reproduce un sonido si el archivo existe, si no, lo ignora."""
    try:
        playsound(ruta_archivo)
    except Exception:
        pass  # Silenciosamente ignoramos errores

# ========== ARTE ASCII DE DADOS ==========

def dado_ascii(numero):
    """Devuelve una lista de 5 strings representando un dado con el número dado."""
    if numero == 1:
        return [
            " _____ ",
            "|     |",
            "|  o  |",
            "|     |",
            "|_____|"
        ]
    elif numero == 2:
        return [
            " _____ ",
            "| o   |",
            "|     |",
            "|   o |",
            "|_____|"
        ]
    elif numero == 3:
        return [
            " _____ ",
            "| o   |",
            "|  o  |",
            "|   o |",
            "|_____|"
        ]
    elif numero == 4:
        return [
            " _____ ",
            "| o o |",
            "|     |",
            "| o o |",
            "|_____|"
        ]
    elif numero == 5:
        return [
            " _____ ",
            "| o o |",
            "|  o  |",
            "| o o |",
            "|_____|"
        ]
    else:  # numero == 6
        return [
            " _____ ",
            "| o o |",
            "| o o |",
            "| o o |",
            "|_____|"
        ]

def dibujar_dados(lista_numeros):
    """Concatena horizontalmente varios dados y devuelve 5 líneas de texto."""
    if not lista_numeros:
        return ["     "] * 5
    ascii_dados = [dado_ascii(n) for n in lista_numeros]
    lineas = []
    for fila in range(5):
        linea = "".join(dado[fila] for dado in ascii_dados)
        lineas.append(linea)
    return lineas

def mostrar_dados_jugadores(dados1, dados2, nombre1, nombre2):
    """Muestra los dados de ambos jugadores lado a lado."""
    lineas1 = dibujar_dados(dados1)
    lineas2 = dibujar_dados(dados2)
    
    suma1 = sum(dados1)
    suma2 = sum(dados2)
    
    print(f"{nombre1} (Total: {suma1})".ljust(30) + " " + f"{nombre2} (Total: {suma2})")
    print("-" * 60)
    
    for fila in range(5):
        linea1 = lineas1[fila] if fila < len(lineas1) else " " * 7
        linea2 = lineas2[fila] if fila < len(lineas2) else " " * 7
        print(f"{linea1}  {linea2}")

# ========== ANIMACIÓN DEL LANZAMIENTO ==========

def animar_lanzamiento(num_dados, nombre1, nombre2):
    """
    Realiza una animación de dados girando durante ~2 segundos,
    y devuelve los resultados finales (listas de números) y las sumas.
    """
    # Sonido de lanzamiento (una sola vez al inicio)
    reproducir_sonido("sonidos/lanzamiento.wav")
    
    # Generamos los resultados finales (los reales)
    resultados1 = [random.randint(1, 6) for _ in range(num_dados)]
    resultados2 = [random.randint(1, 6) for _ in range(num_dados)]
    
    # Bucle de animación (20 frames)
    for _ in range(20):
        temp1 = [random.randint(1, 6) for _ in range(num_dados)]
        temp2 = [random.randint(1, 6) for _ in range(num_dados)]
        limpiar_pantalla()
        print("  🎲 ¡Lanzando dados! 🎲")
        print()
        mostrar_dados_jugadores(temp1, temp2, nombre1, nombre2)
        time.sleep(0.1)
    
    # Mostrar el resultado final
    limpiar_pantalla()
    print("  🎲 ¡Resultado final! 🎲")
    print()
    mostrar_dados_jugadores(resultados1, resultados2, nombre1, nombre2)
    print()
    
    suma1 = sum(resultados1)
    suma2 = sum(resultados2)
    return resultados1, resultados2, suma1, suma2

# ========== FUNCIONES DEL JUEGO ==========

def mostrar_menu():
    """Muestra el menú principal."""
    print("=" * 60)
    print("Bienvenido al Duelo de Dados!")
    print("=" * 60)
    print("Seleccione el nivel de dificultad:")
    print("1. Fácil     (1 dado)")
    print("2. Medio     (3 dados)")
    print("3. Difícil   (5 dados)")
    print("4. Ver estadísticas")
    print("0. Salir del juego")
    print("=" * 60)

def pedir_nombres():
    """Solicita los nombres de los jugadores."""
    print("\nIngresa los nombres de los jugadores")
    nombre1 = input("Jugador 1 (o presiona Enter para usar 'Jugador 1'): ").strip()
    if nombre1 == "":
        nombre1 = "Jugador 1"
    nombre2 = input("Jugador 2 (o presiona Enter para usar 'Jugador 2'): ").strip()
    if nombre2 == "":
        nombre2 = "Jugador 2"
    return nombre1, nombre2

def iniciar_estadisticas():
    """Inicializa el diccionario de estadísticas."""
    return {
        "partidas": 0,
        "victorias1": 0,
        "victorias2": 0,
        "empates": 0,
        "score1": 0,
        "score2": 0,
    }

def actualizar_estadisticas(est, ganador, score1, score2):
    """Actualiza las estadísticas tras una partida."""
    est['partidas'] += 1
    est['score1'] += score1
    est['score2'] += score2
    if ganador == 1:
        est['victorias1'] += 1
    elif ganador == 2:
        est['victorias2'] += 1
    else:
        est['empates'] += 1

def mostrar_estadisticas(est, nombre1, nombre2):
    """Muestra las estadísticas acumuladas."""
    limpiar_pantalla()
    print("\n" + "=" * 60)
    print("ESTADISTICAS DEL JUEGO")
    print("=" * 60)
    print(f"Partidas jugadas: {est['partidas']}")
    print(f"Victorias de {nombre1}: {est['victorias1']}")
    print(f"Victorias de {nombre2}: {est['victorias2']}")
    print(f"Empates: {est['empates']}")
    print(f"Puntos totales de {nombre1}: {est['score1']}")
    print(f"Puntos totales de {nombre2}: {est['score2']}")
    
    if est['partidas'] > 0:
        promedio1 = est['score1'] / est['partidas']
        promedio2 = est['score2'] / est['partidas']
        print(f"Promedio de puntos de {nombre1}: {promedio1:.1f}")
        print(f"Promedio de puntos de {nombre2}: {promedio2:.1f}")
        
        pct1 = (est['victorias1'] / est['partidas']) * 100
        pct2 = (est['victorias2'] / est['partidas']) * 100
        print("\nPorcentaje de victorias:")
        print(f"{nombre1}: {pct1:.1f}%")
        print(f"{nombre2}: {pct2:.1f}%")
    else:
        print("\nAún no se ha jugado ninguna partida.")
    
    print("=" * 60)
    pausa()

def play_game(num_dados, nombre1, nombre2, estadisticas):
    """Ejecuta una partida con el número de dados indicado."""
    # Mostrar el nivel elegido
    niveles = {1: "Fácil", 3: "Medio", 5: "Difícil"}
    nivel = niveles.get(num_dados, "Desconocido")
    print(f"\n🎲 Nivel {nivel} - {num_dados} dado(s) cada jugador\n")
    
    # Animar y obtener resultados
    res1, res2, suma1, suma2 = animar_lanzamiento(num_dados, nombre1, nombre2)
    
    # Determinar ganador
    if suma1 > suma2:
        print(f"\n🏆 ¡{nombre1} WINS! 🏆")
        ganador = 1
        reproducir_sonido("sonidos/victoria.wav")
    elif suma2 > suma1:
        print(f"\n🏆 ¡{nombre2} WINS! 🏆")
        ganador = 2
        reproducir_sonido("sonidos/victoria.wav")
    else:
        print("\n🤝 Empate 🤝")
        ganador = 0
        reproducir_sonido("sonidos/empate.wav")
    
    # Actualizar estadísticas
    actualizar_estadisticas(estadisticas, ganador, suma1, suma2)
    pausa()

# ========== MENÚ PRINCIPAL ==========

def menu_principal():
    """Bucle principal del juego."""
    # Pedir nombres al inicio
    nombre1, nombre2 = pedir_nombres()
    estadisticas = iniciar_estadisticas()
    
    # Sonido de bienvenida (solo una vez)
    reproducir_sonido("sonidos/menu.wav")
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción (0-4): ").strip()
        
        if opcion == "0":
            print("\n" + "=" * 60)
            print("Gracias por jugar al Duelo de Dados. ¡Hasta luego!")
            print("=" * 60)
            break
        
        elif opcion == "1":
            num_dados = 1
        elif opcion == "2":
            num_dados = 3
        elif opcion == "3":
            num_dados = 5
        elif opcion == "4":
            mostrar_estadisticas(estadisticas, nombre1, nombre2)
            continue  # Volver al menú
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")
            pausa()
            continue
        
        # Bucle interno para repetir partidas en el mismo nivel
        while True:
            play_game(num_dados, nombre1, nombre2, estadisticas)
            respuesta = input("\n¿Jugamos otra partida? (S/N): ").strip().lower()
            if respuesta != 's':
                break

# ========== EJECUCIÓN ==========
if __name__ == "__main__":
    menu_principal()