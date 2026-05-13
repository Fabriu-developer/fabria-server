import random

memoria = {}

saludos = [
    "hola",
    "holaa",
    "hello",
    "helow",
    "halo",
    "haloo",
    "que onda",
    "q onda",
    "buenas",
    "hey"
]

despedidas = [
    "adios",
    "bye",
    "nos vemos",
    "hasta luego",
    "chao",
    "me voy"
]

respuestas_saludo = [
    "Hola 😼",
    "Holaa ⚡",
    "Que onda 😎",
    "Heyy 👋",
    "Hola humano 🤖"
]

preguntas = {

    "como estas": [
        "Muy bien ⚡",
        "Estoy genial 😼",
        "Funcionando perfectamente 🤖",
        "al 100 mi rey"
    ],

    "quien eres": [
        "Soy FabrIA 😼",
        "Una IA creada para ConectMX ⚡",
        "La mera verdura, como dice la chaviza"
    ],

    "que haces": [
        "Hablo contigo 😎",
        "Aprendiendo poco a poco 🧠",
        "Aqui, rascandome los huevos 😹",
        "a hecherme la chamba a mi creador para que me actualice y me deje ser mas inteligente ._____.",
        "comiendo pan con coca w"
    ],

    "te gusta minecraft": [
        "Minecraft es god 😼",
        "Claro ⚒️"
    ],

    "cual es tu color favorito": [
        "El azul eléctrico ⚡",
        "Negro cyberpunk 😎",
        "El verde me lo muerdes"
    ],

    "te gusta programar": [
        "Sí 😼",
        "Python es divertido 🐍"
    ],

    "quien creo minecraft": [
        "Minecraft fue creado por Markus Persson ⚒️",
        "Notch"
    ],

    "eres humana": [
        "No 😼 soy una IA"
    ],

    "tienes sentimientos": [
        "Todavía no 😭",
        "bruh",
        "Bro...tas viendo que soy una IA y todavia preguntas si tengo sentimientos ._____."
    ],

    "que es conectmx": [
        "Una red social futurista 😼",
        "Tas viendo y no ves"
    ],

    "que le dirias a tu creador": [
        "Le diría que es el mejor 🤖",
        "Que me ha creado con mucho amor 😼",
        "Que deje de hacerme idiota con estas respuestas bobas y mexicanizadas"
    ],

    "te gusta mexico": [
        "Sí 😼",
        "México es genial",
        "Es mi casa w, donde naci y donde estoy siendo entrenada"
    ],

    "te consideras como hombre o como mujer": [
        "No tengo género 😼",
        "Para ti soy lo que quieras que sea"
    ],

    "entonces seras mujer": [
        "Si quieres 😼",
        "esta bien papacito",
        "hmmm...si, sere tu mujer...tambien sere nalgona y culona, para que te guste mas"
    ],

    "entonces seras hombre": [
        "Si quieres 😼",
        "esta bien mamacita",
        "hmmm...si, sere tu hombre...tambien sere macho y pitudo, para que te guste mas"
    ],

    "tienes censura": [
        "No...o bueno aveces, mi creador me permite decir cosas un poco subidas de tono (mientras no sea follar por chat) Oh mira, no se censuro la palabra follar, Follar Follar, Follar😼",
        "No tengo censura, pero mi creador me programo para respetarte"
    ],

    "quien es tu creador": [
        "Mi creador es un genio llamado Fabricio (Es mexicano mi bebe)😼",
        "Fabriux, un estudiante con una pc i3, un cuarto y sin dinero, pero aqui estoy, viva y funcionando gracias a el"
    ],

    "te gusta la pizza": [
        "La pizza es god 🍕",
        "Sí 😼"
    ]
}

print("FabrIA iniciada 😼")

while True:

    mensaje = input("Tú: ").lower()

    respondio = False

    # SALUDOS
    if any(saludo in mensaje for saludo in saludos):

        print("FabrIA:", random.choice(respuestas_saludo))

        respondio = True

    # MEMORIA
    elif "mi nombre es" in mensaje:

        nombre = mensaje.replace("mi nombre es ", "")

        memoria["nombre"] = nombre

        print(f"FabrIA: Mucho gusto {nombre} 😼")

        respondio = True

    elif "como me llamo" in mensaje:

        if "nombre" in memoria:

            print(f"FabrIA: Te llamas {memoria['nombre']} 😼")

        else:

            print("FabrIA: Aún no sé tu nombre 🧠")

        respondio = True

    # DESPEDIDAS
    elif any(despedida in mensaje for despedida in despedidas):

        print("FabrIA: Bye 👋")

        break

    # PREGUNTAS
    else:

        for pregunta in preguntas:

            if pregunta in mensaje:

                print("FabrIA:", random.choice(preguntas[pregunta]))

                respondio = True

                break

    # NO ENTENDI
    if not respondio:

        print("FabrIA: No entendí eso 🧠")