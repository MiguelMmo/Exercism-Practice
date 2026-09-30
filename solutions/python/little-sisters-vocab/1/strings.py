""" Funciones que permite generar el cambio en una cadena de texto o palabra especifica de una lista"""


def add_prefix_un(word):
    # Función que añade el prefijo "un" a una palabra dada
    # Parámetros:
    # word (str): La palabra raíz
    # Retorna:
    # str: La palabra raíz con el prefijo "un" al inicio
    sentence = "un" + word
    return sentence


def make_word_groups(vocab_words):
    # Función que transforma una lista con un prefijo y varias palabras
    # Parámetros:
    # vocab_words (list[str]): Lista de palabras con el prefijo en la primera posición
    # Retorna:
    # str: Cadena con el prefijo seguido de las palabras transformadas, separadas por ' :: '
    """
        Ejemplo
    >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    for i in range(1, len(vocab_words)):
        vocab_words[i] = prefix + vocab_words[i]
    groups_list = ' :: '.join(vocab_words)
    return groups_list


def remove_suffix_ness(word):
    # Función que elimina el sufijo "ness" de una palabra, ajustando la ortografía si es necesario
    # Parámetros:
    # word (str): Palabra a la que se le quitará el sufijo
    # Retorna:
    # str: Palabra sin el sufijo "ness" y con corrección ortográfica si aplica
    """
    Ejemplo:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    if word.endswith('ness') and word[-5] == 'i':
        result = word[:-5] 
        result = result + 'y'
        return result
    else:
        result = word[:-4] 
        return result
        

def adjective_to_verb(sentence, index):
    # Función que convierte un adjetivo dentro de una oración en verbo
    # Parámetros:
    # sentence (str): La oración que contiene el adjetivo
    # index (int): Índice del adjetivo dentro de la oración
    # Retorna:
    # str: El adjetivo transformado en verbo (añadiendo "en")
    """
    Ejemplo:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    word_index = sentence.split()
    word_index = word_index[index]
    if word_index[-1] == '.':
        result =  word_index[:-1] + 'en'
        return result
    else:
        return word_index + 'en'
    

