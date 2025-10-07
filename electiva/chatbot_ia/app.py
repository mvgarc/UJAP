from flask import Flask, request, jsonify, render_template
import os
from google import genai
from google.genai.errors import APIError

app = Flask(__name__)

# --- Inicialización del Cliente de Gemini ---
try:
    # La clave API se lee automáticamente de la variable de entorno GEMINI_API_KEY
    client = genai.Client()
    print("✨ Cliente de Gemini inicializado con éxito.")
except Exception as e:
    print(f"🚨 Error al inicializar el cliente de Gemini: {e}")
    client = None

MODELO_GEMINI = "gemini-1.5-flash"

# --- Rutas de la Aplicación ---

@app.route("/")
def index():
    # Asume que tienes un archivo index.html en la carpeta 'templates'
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    # 1. Obtener el mensaje del usuario del cuerpo del request
    data = request.get_json()
    # Asume que el frontend envía el mensaje con la clave "mensaje"
    user_message = data.get("mensaje", "") 

    if not client:
        respuesta = "Lo siento, la API no está configurada. Verifica la clave GEMINI_API_KEY."
        # CORRECCIÓN: La sintaxis del jsonify estaba mal (faltaban comillas y los dos puntos)
        return jsonify({"respuesta": respuesta}) 
    
    # Manejar el caso de mensaje vacío
    if not user_message.strip():
        return jsonify({"respuesta": "Por favor, escribe un mensaje."})

    try: 
        system_instruction = "Eres un asistente virtual amigable, útil y conciso. Responde siempre en español."
        
        # 2. Llamada a la API de Gemini
        response = client.models.generate_content(
            model=MODELO_GEMINI,
            # CORRECCIÓN: La variable 'user_message' ya está definida arriba
            contents=user_message, 
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )
        respuesta = response.text.strip()
        
    except APIError as e:
        print(f"Error de la API de Gemini: {e}")
        respuesta = "Hubo un problema al contactar a la API. Inténtalo de nuevo."
        
    except Exception as e:
        print(f"Error inesperado al generar contenido: {e}")
        respuesta = "Lo siento, ocurrió un error interno."

    return jsonify({"respuesta": respuesta})

# --- Ejecución ---
if __name__ == "__main__":
    app.run(debug=True)