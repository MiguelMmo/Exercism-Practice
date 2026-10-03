
"""Funciones para rastrear manos de póker y tareas relacionadas con cartas.

Documentación de listas en Python: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    """Crear una lista con la ronda actual y las dos siguientes.

    Parámetros:
        number (int): El número de la ronda actual.

    Retorna:
        list: La ronda actual y las dos que siguen.
    """
    number_one = number +1
    number_two = number +2
    next_number = [number, number_one, number_two]
    return next_number


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenar dos listas de rondas.

    Parámetros:
        rounds_1 (list): La primera lista de rondas jugadas.
        rounds_2 (list): La segunda lista de rondas jugadas.

    Retorna:
        list: Todas las rondas jugadas.
    """
    all_round = rounds_1 + rounds_2
    return all_round



def list_contains_round(rounds, number):
    """Verificar si una lista de rondas contiene un número específico.

    Parámetros:
        rounds (list): Las rondas jugadas.
        number (int): El número de ronda a verificar.

    Retorna:
        bool: True si la ronda fue jugada, False en caso contrario.
    """

    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calcular el valor promedio de las cartas en la mano.

    Parámetros:
        hand (list): Las cartas en la mano.

    Retorna:
        float: El valor promedio de las cartas.
    """
    aver_list = sum(hand) / len(hand)
    return aver_list
    


def approx_average_is_average(hand):
    """Verificar si el promedio calculado coincide con una aproximación.

    La aproximación puede ser:
    - El promedio entre la primera y la última carta.
    - El valor de la carta en la posición central.

    Parámetros:
        hand (list): Las cartas en la mano.

    Retorna:
        bool: True si alguna aproximación coincide con el promedio real.
    """
    hand.sort()
    aver_hand = sum(hand) / len(hand)
    mid_card = int(len(hand) // 2)
    min_max = (hand[0] + hand[-1]) / 2

    if aver_hand == min_max:
        return True
    if aver_hand == hand[mid_card]:
        return True
    return False 
    

    


def average_even_is_average_odd(hand):
    """Verificar si el promedio de cartas en posiciones pares
    es igual al promedio de cartas en posiciones impares.

    Parámetros:
        hand (list): Las cartas en la mano.

    Retorna:
        bool: True si los promedios son iguales, False en caso contrario.
    """
    even_hand = hand[0::2]
    odd_hand = hand [1::2]

    avg_even = sum(even_hand) / len(even_hand)
    avg_odd = sum(odd_hand) / len(odd_hand)
    return avg_even == avg_odd
    


    


def maybe_double_last(hand):
    """Multiplicar por 2 el valor de la última carta si es una J (Jack).

    Parámetros:
        hand (list): Las cartas en la mano.

    Retorna:
        list: La mano con el valor de la última carta duplicado si es J.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
        return hand
    return hand
