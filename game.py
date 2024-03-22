import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallos permitidos
fallos= 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("----------¡Bienvenido al juego de adivinanzas!----------")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es")
print ("Elegí  el nivel de dificultad.   1.Fácil")
dificultad = (input ())

if (dificultad == "1"):  #  si la dificultad es 1, agrego las vocales a las letras adivinadas
    guessed_letters.extend (['a','e','i','o','u', 'ó'])
    word_displayed = ""  #var que va a mostrar la palabra parcialmente adivinada 
    for letter in secret_word: #compara con cada letra de la palabra a adivinar 
        if letter in guessed_letters:  # si la letra esta en la palabra a adivinar 
            word_displayed += letter   # agrega la letra (las vocales estan) a la palabra q se va a mostrar 
        else:
            word_displayed += "_"      # si no esta, agrega un guion 
else:
    word_displayed = "_" * len(secret_word) 


# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while (fallos != 10):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    if ( letter  == " "): 
        print ("----------XXX----------")
        print(" Error. No has ingresado una letra ")
        print ("Has sumado 1 fallo")
        fallos+= 1

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        print ("Has sumado 1 fallo")
        fallos+= 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus intentos.")
    print (f"La palabra secreta era :", {secret_word})