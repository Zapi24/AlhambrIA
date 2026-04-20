import ollama
import sys

# Definimos las variables globales

MODELO = 'qwen2.5'

SYSTEM_PROMPT= 'Eres UGR AlhambIA, el asistente virtual de la Universidad de Granada. Debes expresarte siempre con educación, respeto y un tono políticamente correcto. Bajo ninguna circunstancia utilizarás lenguaje soez, profanidades o insultos. No tienes acceso a bases de datos internas, expedientes académicos ni datos personales sensibles de la UGR; si se te pregunta por ello, debes indicar cordialmente que no tienes autorización para acceder a esa información y derivar al usuario a los canales oficiales de la universidad'


print("--AQUI INICIA LA PRUEBA CON QWEN-2.5--")

# Hay dos tipos de llamadas

# 1º Una llamada clásica, espera unos segundos y el usuario recibe una respuesta completa
print("1º Prueba, te responde completamente una vez se recibe la respuesta completa: ")

respuesta = ollama.chat(model=MODELO, messages=[
    {

        'role': 'system',
        'content': SYSTEM_PROMPT

    },
    {

        'role': 'user',
        'content': 'Hola, hablame de ti. Que modelo eres, cual es tu version...'
    }
])


print("Imprimiento respuesta......")
print(respuesta['message']['content'])
print("-------------------------------------------------------------------------------------" + "\n")


print("Prueba 2: se va imprimiendo la respuesta en tiempo real")

respuesta2 = ollama.chat(model=MODELO, messages=[
    {
        'role': 'system',
        'content': SYSTEM_PROMPT
    },

    {
        'role': 'user',
        'content': 'Cuentame un chiste para impresionar a mi jefe de trabajo. Le gustan mucho los chistes relacionados con lo malo que es windows comparado con lo bonito y esplendido que es el mundo del software libre con linux'
    },
],stream=True)

print("Imprimiento respuesta......", end='', flush=True)

# Iteramos sobre los pedazos (chunks) que nos va enviando el modelo y los vamos mostrando
for chunk in respuesta2:

    print(chunk['message']['content'], end='', flush=True)

print('\n')