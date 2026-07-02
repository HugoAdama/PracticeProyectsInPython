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
#LIBRERIAS 
import random  #Libreria para los numeros aleatorios 
import subprocess #Libreria 1 para la limpieza de pantalla 
import sys        #Libreria 2 para la limpieza de pantalla 
import time     #Libreria para la animacion de los dados 

#FUNCIONES DE UTILIDAD
def limpiar_pantalla():
    """
    Limpia la pantalla de la terminal usando el comando apropiado para cada SO.
    """
    # 'sys.platform' identifica el sistema operativo de forma fiable
    if sys.platform.startswith('win'):
        # En Windows, 'cls' es un comando interno del shell (cmd.exe)
        # Por eso, necesitamos ejecutarlo a través del shell con 'shell=True'
        subprocess.run('cls', shell=True)
    else:
        # En Linux y macOS, el comando es 'clear'.
        # Al ser un programa externo, no es estrictamente necesario 'shell=True'
        # lo que es más seguro.
        subprocess.run('clear')
        
def pausa():
    input("\nPresiona Enter para continuar...")

#ARTE ASCII DE LOS DADOS 
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
    if not lista_numeros:
        return ["     "] *5 # Si no hay dados se devuelve lines vacias 
    #Obtenemos el arte ASCII de cada dados 
    ascii_dados = [dado_ascii(n) for n in lista_numeros]
    #Concatenamos fila por fila 
    lineas = []
    for fila in range(5):
        linea= "".join(dado[fila] for dado in ascii_dados)
        lineas.append(linea)
    return lineas 

def mostrar_dados_jugadores(dados1,dados2,nombre1,nombre2):
    """
    Muestra en pantalla los dados de ambos jugadores lado a lado.
    dados1 y dados2 son listas de números (resultados de cada dado).
    """ 
    #Obtener las lineas de cada jugador
    lineas1 = dibujar_dados(dados1)
    lineas2 = dibujar_dados(dados2)
    
    #Calcular sumas 
    suma1= sum(dados1)
    suma2= sum(dados2)
    
    #Imprimimos una cabecera con los nombres de los jugadores y la suma
    print(f"{nombre1} (Total: {suma1})".ljust(30)  + " " + f"{nombre2} (Total: {suma2})" )
    print("-" * 60)
    
    #Imprimimos fila por fila , intercalando los dados de ambos jugadores
    for fila in range(5):
        #Asegurar que ambas lineas tengan el mismo ancho (padding)
        linea1 = lineas1[fila] if fila < len(lineas1) else " " * 7 
        linea2 = lineas2[fila] if fila < len(lineas2) else " " * 7 
        
        #Imprimimos con un espacio de separacion
        print(f"{linea1}  {linea2}")
            
 #ANIMACION DEL LANZAMIENTO
def animar_lanzamiento(num_dados,nombre1,nombre2):
    """
    Realiza una animación de dados girando durante ~2 segundos,
    y devuelve los resultados finales (listas de números) y las sumas.
    """
    #Generamos los resultados finales 
    resultados1 = [random.randint(1, 6) for _ in range(num_dados)]
    resultados2 = [random.randint(1, 6) for _ in range(num_dados)]
    
    #Bucle para la animacion con 20 frames
    for _ in range(20):
       # Generar números temporales aleatorios para la animación
        temp1 = [random.randint(1, 6) for _ in range(num_dados)]
        temp2 = [random.randint(1, 6) for _ in range(num_dados)]
        limpiar_pantalla()
        print("  ¡Lanzando dados!  ")
        print()
        mostrar_dados_jugadores(temp1, temp2, nombre1, nombre2)
        time.sleep(0.1)  # pausa breve entre frames
    
    # Mostrar el resultado final (con los números reales)
    limpiar_pantalla()
    print("  ¡Resultado final!  ")
    print()
    mostrar_dados_jugadores(resultados1, resultados2, nombre1, nombre2)
    print()
    
    # Calcular sumas
    suma1 = sum(resultados1)
    suma2 = sum(resultados2)
    return resultados1, resultados2, suma1, suma2 
                    
            
# MENÚ PRINCIPAL
def mostrar_menu():

    print("="*60)
    print("Bienvenido al Duelo de Dados!")
    print("="*60)
    print("Seleccione el nivel de dificultad:")
    print("1. Facil     (1 dado)")
    print("2. Medio     (3 dados)")
    print("3. Dificil   (5 dados)")
    print("4. Ver estadisticas")
    print("0. Salir del juego")
    print("="*60)

def pedir_nombres():
    print("\nIngresa los nombres de los jugadores")
    nombre_player1= input("Jugador 1 (o presiona Enter para usar 'Jugador 1'):").strip()
    if nombre_player1 == "":
        nombre_player1 = "Jugador 1"
    nombre_player2= input("Jugador 2 (o presiona Enter para usar 'Jugador 2'):").strip()
    if nombre_player2 == "":
        nombre_player2 = "Jugador 2"    
    return nombre_player1, nombre_player2

def iniciar_estadisticas():
    return {
        "partidas" : 0 ,
        "victorias1" : 0 ,
        "victorias2" : 0 ,
        "empates" : 0 ,
        "score1" : 0 , # suma total de puntos del jugador 1
        "score2" : 0 , # suma total de puntos del jugador 2 
    }
    
def mostrar_estadisticas(est, nombre1, nombre2):
    limpiar_pantalla()
    print("\n" + "="*60)
    print("ESTADISTICAS DEL JUEGO")    
    print("="*60)    
    print(f"Partidas jugadas: {est['partidas']}")
    print(f"Victorias de {nombre1}: {est['victorias1']}")
    print(f"Victorias de {nombre2}: {est['victorias2']}")
    print(f"Empates: {est['empates']}")
    print(f"Puntos totales de {nombre1}: {est['score1']}")
    print(f"Puntos totales de {nombre2}: {est['score2']}")
    
    if est['partidas'] > 0:
        # Promedios
        promedio1 = est['score1'] / est['partidas']
        promedio2 = est['score2'] / est['partidas']
        print(f"Promedio de puntos de {nombre1}: {promedio1:.1f}")
        print(f"Promedio de puntos de {nombre2}: {promedio2:.1f}")
        
        # Porcentajes de victorias
        pct1 = (est['victorias1'] / est['partidas']) * 100
        pct2 = (est['victorias2'] / est['partidas']) * 100
        print("\nPorcentaje de victorias:")
        print(f"{nombre1}: {pct1:.1f}%")
        print(f"{nombre2}: {pct2:.1f}%")
    else:
        print("\nAún no se ha jugado ninguna partida.")
        
    print("="*60)
    pausa()
 
def actualizar_estadisticas(est,ganador,score1,score2):
    est['partidas'] += 1  
    est['score1'] += score1  
    est['score2'] += score2 
    if ganador == 1:
        est['victorias1'] += 1 
    elif ganador == 2:
        est['victorias2'] += 1  
    else:
        est['empates'] += 1
        

""""  
ANIMACION SIMPLE DE LOS DADOS 
def animar_lanzamiento(num_dados):
    
    Muestra una animación de dados rodando y devuelve el resultado final.
    
    # Número de iteraciones de la animación
    iteraciones = 10
    # Lista temporal para ir mostrando resultados
    resultados = [0] * num_dados
    
    for i in range(iteraciones):
        # Generamos números aleatorios para cada dado
        for j in range(num_dados):
            resultados[j] = random.randint(1, 6)
        
        # Mostramos la tirada actual en la misma línea
        # Usamos \r para ir al inicio de la línea y sobrescribir
        print(f"\r Lanzando... {resultados}", end="")
        
        # Pequeña pausa para que se vea el movimiento
        time.sleep(0.20)
    
    # Última pausa antes de mostrar el resultado final
    time.sleep(0.5)
    print()  # Salto de línea para que lo siguiente no se sobrescriba
    
    return resultados
"""

#LANZAMIENTO DE DADOS
def tirar_dados(num_dados):
    return [random.randint(1,6) for _ in range(num_dados)]
    
    
def play_game(num_dados,nombre1,nombre2,estadisticas): 
    
    res1,res2,suma1,suma2 = animar_lanzamiento(num_dados,nombre1,nombre2)
    
    #SE DETERMINA EL GANADOR 
    if suma1 > suma2:
        print(f"\n {nombre1}  WINS!")
        ganador = 1
    elif suma2 > suma1:
        print(f"\n {nombre2} WINS!")
        ganador = 2 
    else:
        print("\n Empateee :O")    
        ganador = 0  
        
#SE ACTUALIZA LAS ESTADISTICAS 
    actualizar_estadisticas(estadisticas,ganador, suma1,suma2)
    pausa()
    
#INTERFAZ DEL MENU
def menu_principal():
    
    #PEDIMOS LOS NOMBRES DE LOS JUGADORES 
    nombre1 , nombre2 = pedir_nombres()
    estadisticas = iniciar_estadisticas()

    while True:
        mostrar_menu() 
        opcion = input("Seleccione una opcion (0-4) :").strip()
 
        if opcion == "0":
            print("\n" + "="*60)
            print("\nGracias por jugar al Duelo de Dados! Seeya!")
            print("\n" + "="*60) 
            break
        elif opcion == "1":
            num_dados = 1  
            nivel = "Facil"  

        elif opcion == "2":
            num_dados = 3 
            nivel = "Medio"  
 
        elif opcion == "3":
            num_dados = 5 
            nivel = "Dficil"  
            
        elif opcion == "4":
            mostrar_estadisticas(estadisticas,nombre1,nombre2)
            continue # Volvemos al menu principal   
            
        else:
                print("\n" + "="*60)
                print("\nBro opcion no valida , selecciona una opcion del menu")
                print("\n" + "="*60)
                pausa()
        
        print(f"\n Nivel escogido {nivel}")
        while True:
            play_game(num_dados,nombre1,nombre2, estadisticas)
            respuesta = input("\nJugamos otra partida?? (S/N):").strip().lower()
            if respuesta != 's':
                break
    
if __name__== "__main__":
    menu_principal()