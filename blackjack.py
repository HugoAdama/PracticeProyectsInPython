#PRUEBA TECNICA BLACKJACK

import random 

# Lista de cartas disponibles en la baraja
valor_cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'AS']

# Diccionario que convierte cada carta en su valor numérico para calcular puntos
valor_num_cartas = {
    2:2, 3:3, 4:4, 5:5, 6:6, 7:7,
    8:8, 9:9, 10:10,
    'J':10, 'Q':10, 'K':10, 'AS':11
}


# Función encargada de sacar una carta aleatoria del mazo
# Recibe el mazo, escoge una posición aleatoria y elimina esa carta
def repartir_cartas(mazo_cartas):

    mazo_size = len(mazo_cartas)

    # Elegimos una posición aleatoria dentro del mazo
    rand_index = random.randint(0, mazo_size - 1)

    # Sacamos la carta y la eliminamos del mazo
    carta = mazo_cartas.pop(rand_index)

    return carta



# Función que crea una nueva partida
# Crea el mazo, reparte 2 cartas al jugador y 2 a la casa
def iniciar_partida():

    # Crea un mazo con 4 copias de cada carta
    mazo_cartas = [carta for carta in valor_cartas for j in range(4)]

    mano_player = []
    mano_casa = []


    # Reparte dos cartas para cada participante
    for j in range(2):

        mano_player.append(repartir_cartas(mazo_cartas))
        mano_casa.append(repartir_cartas(mazo_cartas))


    return mano_player, mano_casa, mazo_cartas



# Función que revisa si el jugador todavía puede seguir jugando
# Si tiene 21 o menos puntos puede continuar
def still_playing(mano_player):

    if sum_cartas(mano_player) <= 21:
        return True

    return False



# Función que suma los puntos de las cartas
# También controla el caso especial del AS
def sum_cartas(mano):

    suma = 0


    # Suma el valor de cada carta
    for carta in mano:
        suma += valor_num_cartas[carta]


    # El AS puede valer 11 o 1 dependiendo de la situación
    if 'AS' in mano:

        num_ases = sum([1 for j in mano if j == 'AS'])

        contador = 0

        # Si nos pasamos de 21 convertimos AS de 11 a 1
        while contador < num_ases and suma > 21:

            suma -= 10
            contador += 1


    return suma



# Función que decide quién gana la partida
def know_winner(mano_player, mano_casa):

    puntos_player = sum_cartas(mano_player)
    puntos_casa = sum_cartas(mano_casa)


    # Si la casa se pasa de 21 gana el jugador
    if puntos_casa > 21:
        return 'Gana el jugador'


    # Si el jugador tiene más puntos sin pasarse de 21 gana
    if puntos_player <= 21 and puntos_player > puntos_casa:
        return 'Gana el jugador'


    # En cualquier otro caso gana la casa
    return 'Gana la casa'



# Función para preguntar si el jugador quiere volver a jugar
def jugar_otra_partida():

    while True:

        respuesta = input('¿Quieres jugar otra partida? (S/N): ').upper()


        if respuesta == 'S':
            return True


        elif respuesta == 'N':
            return False


        else:
            print('Respuesta no válida. Escribe S o N')




# ---------------- PROGRAMA PRINCIPAL ----------------


while True:

    print('\nBienvenido a BlackJack de Shito')


    # Inicia una nueva partida
    mano_player, mano_casa, mazo_cartas = iniciar_partida()



    # Turno del jugador
    while still_playing(mano_player):


        print('\nTus cartas:', mano_player, 'Puntos:', sum_cartas(mano_player))

        print('Cartas de la casa:', mano_casa, 'Puntos:', sum_cartas(mano_casa))


        pide_o_planta = input(
            '¿Pedir carta (P) o plantarse (S)? '
        ).upper()



        # El jugador pide una nueva carta
        if pide_o_planta == 'P':

            mano_player.append(repartir_cartas(mazo_cartas))


        # El jugador se planta y juega la casa
        elif pide_o_planta == 'S':

            # La casa roba hasta tener mínimo 17 puntos
            while sum_cartas(mano_casa) <= 16:

                mano_casa.append(repartir_cartas(mazo_cartas))

            break



    # Se muestra el resultado final
    winner = know_winner(mano_player, mano_casa)

    print('\nResultado final:')
    print('Jugador:', mano_player, sum_cartas(mano_player))
    print('Casa:', mano_casa, sum_cartas(mano_casa))

    print(winner)



    # Pregunta si quiere continuar
    if not jugar_otra_partida():

        print('Gracias por jugar BlackJack de Shito')

        break