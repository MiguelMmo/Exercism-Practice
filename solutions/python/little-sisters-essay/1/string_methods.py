"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    # Función que convierte la primera letra de cada palabra del título en     mayúscula
    # Parámetros:
    #   title (str): El título del ensayo que necesita formato de título
    # Retorna:
    #   str: El título con las primeras letras en mayúscula
    
    capitalize_title = title.title()
    return capitalize_title


def check_sentence_ending(sentence):
    # Función que verifica si una oración termina con un punto
    # Parámetros:
    #   sentence (str): La oración a verificar
    # Retorna:
    #   bool: True si la oración termina correctamente con punto, False en caso contrario
    check_sentence_ending = sentence[-1]
    if check_sentence_ending == '.':
        return True
    return False


def clean_up_spacing(sentence):
    # Función que elimina los espacios en blanco al inicio y al final de una oración
    # Parámetros:
    #   sentence (str): La oración que se desea limpiar
    # Retorna:
    #   str: La oración sin espacios en blanco al inicio ni al final
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    # Función que reemplaza una palabra dentro de una oración por otra nueva
    # Parámetros:
    #   sentence (str): La oración en la que se reemplazará la palabra
    #   old_word (str): La palabra que se quiere reemplazar
    #   new_word (str): La palabra nueva que sustituirá a la anterior
    # Retorna:
    #   str: La oración con la palabra reemplazada
    words = sentence.split()
    for i in range(len(words)):
        if words[i] == old_word + '.':
            words[i] = new_word + '.'
    return ' '.join(words)
