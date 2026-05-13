from flask import Flask, request, jsonify
import random
import unicodedata

try:
    from flask_cors import CORS
except ModuleNotFoundError:
    CORS = None

app = Flask(__name__)

if CORS:
    CORS(app)
else:
    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return response

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

respuestas_saludo = [
    "Hola \U0001f63c",
    "Holaa \u26a1",
    "Que onda \U0001f60e",
    "Heyy \U0001f44b",
    "Hola humano \U0001f916"
]

preguntas = {
    "como estas": [
        "Muy bien \u26a1",
        "Estoy genial \U0001f63c",
        "Funcionando perfectamente \U0001f916"
    ],
    "quien eres": [
        "Soy FabrIA \U0001f63c",
        "Una IA creada para ConectMX \u26a1"
    ],
    "que haces": [
        "Hablo contigo \U0001f60e",
        "Aprendiendo poco a poco \U0001f9e0"
    ],
    "te gusta minecraft": [
        "Minecraft es god \U0001f63c",
        "Claro \u26cf\ufe0f"
    ],
    "minecraft": [
        "Minecraft es god \u26cf\ufe0f"
    ],
    "cual es tu color favorito": [
        "El azul electrico \u26a1",
        "Negro cyberpunk \U0001f60e"
    ],
    "te gusta programar": [
        "Si \U0001f63c",
        "Python es divertido \U0001f40d"
    ],
    "quien creo minecraft": [
        "Minecraft fue creado por Markus Persson \u26cf\ufe0f",
        "Notch"
    ],
    "eres humana": [
        "No \U0001f63c soy una IA"
    ],
    "tienes sentimientos": [
        "Todavia no \U0001f62d",
        "Aun no, pero estoy aprendiendo a responder mejor \U0001f9e0",
        "Soy una IA, asi que sentimientos reales todavia no tengo"
    ],
    "que es conectmx": [
        "Una red social futurista \U0001f63c",
        "ConectMX es una app social hecha para conectar personas"
    ],
    "quien es tu creador": [
        "Mi creador es Fabricio \U0001f63c",
        "Fui creada por Fabricio para ConectMX \u26a1"
    ],
    "te gusta mexico": [
        "Si \U0001f63c Mexico es genial",
        "Mexico es mi casa digital \u26a1"
    ],
    "te gusta la pizza": [
        "La pizza es god \U0001f355",
        "Si \U0001f63c"
    ]
}

def normalizar_texto(texto):
    texto = str(texto or "").lower().replace("@fabria", " ")
    texto = "".join(
        caracter for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )
    return " ".join(texto.split())

def generar_respuesta(mensaje):
    mensaje_normalizado = normalizar_texto(mensaje)

    if not mensaje_normalizado:
        return "Etiquetame con una pregunta y te respondo \U0001f63c"

    if any(saludo in mensaje_normalizado for saludo in saludos):
        return random.choice(respuestas_saludo)

    for pregunta, respuestas in preguntas.items():
        if pregunta in mensaje_normalizado:
            return random.choice(respuestas)

    return "No entendi eso \U0001f9e0"

@app.route('/fabria', methods=['POST', 'OPTIONS'])
def fabria():
    if request.method == 'OPTIONS':
        return jsonify({}), 204

    data = request.get_json(silent=True) or {}
    mensaje = data.get('mensaje') or data.get('texto') or data.get('comentario') or data.get('textoOriginal') or ""

    return jsonify({
        "respuesta": generar_respuesta(mensaje)
    })

if __name__ == "__main__":
    app.run(port=5000)