import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from translator import translate_and_pronounce, generate_audio
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Serve the main HTML file
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Endpoint to translate and generate audio
@app.route('/api/translate', methods=['POST'])
def translate_api():
    data = request.json
    source_language = data.get('source_language', 'English')
    target_language = data.get('target_language', 'Japanese')
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({"error": "Please provide text to translate"}), 400

    # Call translation logic
    result = translate_and_pronounce(text, source_language, target_language)
    
    if "error" in result:
        return jsonify(result), 500
        
    translation = result.get("translation", "")
    pronunciation = result.get("pronunciation", "")
    
    # Generate audio for the translation
    audio_file = generate_audio(translation, target_language)
    
    response = {
        "translation": translation,
        "pronunciation": pronunciation,
        "audio_url": None
    }
    
    if audio_file and audio_file.endswith(".mp3"):
        # Serve the generated mp3 file path so frontend can construct URL
        response["audio_url"] = f"/audio/{audio_file}"
        
    return jsonify(response)

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    if not os.environ.get("GROQ_API_KEY"):
        print("WARNING: GROQ_API_KEY is not set in the environment.")
    app.run(debug=True, port=5000)
