# AI Machine Translation Studio 🌍

A Machine Translation web application that translates text from one language to another (e.g., English to Japanese) using advanced Natural Language Processing techniques. The application not only provides the translated text, but also the phonetic pronunciation (like Rōmaji) and generates a spoken audio format of the translation using `gTTS` (Google Text-to-Speech).

## Features
- **High-Quality Translations**: Powered by the highly capable `llama-3.3-70b-versatile` language model via the **Groq API**.
- **Multilingual Support**: Translates between English, Spanish, French, German, Japanese, Chinese, and Korean.
- **Phonetic Pronunciation**: See exactly how to pronounce the foreign language text (e.g., Pinyin, Rōmaji).
- **Audio Generation**: Listen to the native pronunciation instantly from a generated `mp3`.
- **Streamlit Interface**: An interactive, modern web interface.

## Prerequisites
- Python 3.8+
- A Groq API Key (You can get one from [Groq Console](https://console.groq.com/))

## Installation

1. **Navigate to the project directory**:
   ```bash
   cd c:\Users\anits-csm\Documents\english_to_jap
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On **Windows** (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - On **Windows** (Command Prompt):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables**:
   Open the `.env` file (if it doesn't exist, create it from `.env.example`) and insert your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## How to Run the Application

1. Open your terminal or command prompt.
2. Ensure your virtual environment is activated (you should see `(venv)` in your terminal prompt).
3. Start the Flask server by running:
   ```bash
   python backend.py
   ```
4. Once the server starts, open your web browser and navigate to:
   **[http://localhost:5000](http://localhost:5000)**
5. From the Custom Frontend interface:
   - Select your Source and Target languages from the sidebar.
   - Enter your text in the text area.
   - Click **🚀 Translate Now**.
   - Review your translation, read the phonetics, and play the generated audio!
