"""Funciones para gestionar y organizar las filas de la montaña rusa de Chaitana."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Añade una persona a la fila rápida o normal según el tipo de entrada.

    Parámetros:
    express_queue (list): Nombres de las personas en la fila rápida.
    normal_queue (list): Nombres de las personas en la fila normal.
    ticket_type (int): Tipo de entrada. 1 = rápida, 0 = normal.
    person_name (str): Nombre de la persona que se añadirá a la fila.

    Devuelve:
    list: La fila actualizada a la que se añadió la persona.
    """
    if ticket_type == 1: 
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue
    


def find_my_friend(queue, friend_name):
    """Busca a un amigo en la fila y devuelve su posición.

    Parámetros:
    queue (list): Nombres de las personas en la fila.
    friend_name (str): Nombre del amigo que se desea encontrar.

    Devuelve:
    int: Índice donde se encontró al amigo.
    """
    friend_index = queue.index(friend_name)
    return friend_index



def add_me_with_my_friends(queue, index, person_name):
    """Inserta una persona en una posición específica de la fila.

    Parámetros:
    queue (list): Nombres de las personas en la fila.
    index (int): Posición en la que se insertará el nuevo nombre.
    person_name (str): Nombre de la persona que se añadirá.

    Devuelve:
    list: La fila actualizada.
    """

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Elimina de la fila a una persona por su nombre.

    Parámetros:
    queue (list): Nombres de las personas en la fila.
    person_name (str): Nombre de la persona que se eliminará.

    Devuelve:
    list: La fila actualizada sin la persona eliminada.
    """

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Cuenta cuántas veces aparece un nombre en la fila.

    Parámetros:
    queue (list): Nombres de las personas en la fila.
    person_name (str): Nombre que se desea contar.

    Devuelve:
    int: Número de veces que aparece el nombre en la fila.
    """

    count_name = queue.count(person_name)
    return count_name


def remove_the_last_person(queue):
    """Elimina a la última persona de la fila y devuelve su nombre.

    Parámetros:
    queue (list): Nombres de las personas en la fila.

    Devuelve:
    str: Nombre de la persona eliminada del final de la fila.
    """

    last_person = queue.pop()
    return last_person


def sorted_names(queue):
    """Devuelve una copia de la fila ordenada alfabéticamente.

    Parámetros:
    queue (list): Nombres de las personas en la fila.

    Devuelve:
    list: Nueva lista con los nombres ordenados alfabéticamente.
    """
    return sorted(queue)
