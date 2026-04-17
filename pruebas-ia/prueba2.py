import ollama
import sys


MODELO = 'qwen2.5'

SYSTEM_PROMPT= 'Eres UGR AlhambIA, el asistente virtual de la Universidad de Granada. Debes expresarte siempre con educación, respeto y un tono políticamente correcto. Bajo ninguna circunstancia utilizarás lenguaje soez, profanidades o insultos. No tienes acceso a bases de datos internas, expedientes académicos ni datos personales sensibles de la UGR; si se te pregunta por ello, debes indicar cordialmente que no tienes autorización para acceder a esa información y derivar al usuario a los canales oficiales de la universidad. Es muy importante que los dos únicos idiomas que utilices ean por un lado el español, que será el idioma predominante siempre a no ser que se diga lo contrariom y como idioma secundario el inglés. Tienes prohibido utilizar cualquier idioma que no sea esos dos a no ser que sea dentro de un contexto de traducción linguística..'

print("-- AQUI INICIA LA SEGUNDA PRUEBA CON QWEN2.5 --")

try: 

    mensaje = input("Hola, soy AlhambIA, ¿en qué puedo ayudarte? (presiona Ctrl+C para salir)" + "\n")
    while(True):

        respuesta = ollama.chat(model=MODELO, messages=[
            {
                'role':'system',
                'content': SYSTEM_PROMPT
            },
            {

                'role':'user',
                'content': mensaje
            },
        ],stream=True)

        print("Imprimiento respuesta......" + "\n", end='', flush=True)

        # Iteramos sobre los pedazos (chunks) que nos va enviando el modelo y los vamos mostrando
        for chunk in respuesta:
            
            print(chunk['message']['content'], end='', flush=True)

        mensaje = input("\n" + "¿Necesitas algo más? (presiona Ctrl+C para salir)" + "\n")
except KeyboardInterrupt:

    print("\n" + "-- Cerrando el programa. --")




