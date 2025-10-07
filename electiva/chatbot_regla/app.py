from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chatbot', methods=['POST'])
def chatbot ():
    data = request.get_json()
    user_message = data.get("mensaje", " ").lower()

    if "hola" in user_message:
        respuesta = "Hola"
    elif "como estas" in user_message:
        respuesta = "Bello"
    elif "nombre" in user_message:
        respuesta = "Me llamo AsistenteX, tu chatbot basado en reglas."
    elif "adiós" in user_message:
        respuesta = "¡Hasta luego! Fue un placer ayudarte."
    else:
        respuesta = "Lo siento, no entendí eso. ¿Podrías repetirlo?"

    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run (debug=True)