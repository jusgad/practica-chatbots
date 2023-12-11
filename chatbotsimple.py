# pip install nltk
from nltk.chat.util import Chat, reflections
mis_reflections = {
    "ir": "fui",
    "hola": "hey"
}

# estos son los cuadros conversacionales
pares = [
    [
        # r = es los que dice el usuario
        # [] = es lo que dice la maquina // se puede cambiar
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]    
    ],
    [
        r"Cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]    
    ],
    [
        r"como estas ?",
        ["Bien y tu?",]    
    ],
    [
        r"Disculpa (.*)",
        ["No pasa nada",]    
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]    
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]    
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]    
    ],
    [
        r"Finalizar",
        ["Chao", "Fue bueno hablar contigo"]    
    ],
]

def chatear():
    print("Hola") # Mensaje por defecto
    chat = Chat(pares, mis_reflections)
    chat.converse()

if __name__== '__main__':
    chatear()

chatear()