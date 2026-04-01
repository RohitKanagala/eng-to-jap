import os
import json
from groq import Groq
from gtts import gTTS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def translate_and_pronounce(text: str, source_lang: str, target_lang: str) -> dict:
    """
    Translates text and provides pronunciation using Groq API.
    Returns a dictionary with 'translation' and 'pronunciation'.
    """
    
    prompt = f"""You are a professional linguist and translator.
Translate the following text from {source_lang} to {target_lang}.
Also provide the phonetic pronunciation (e.g., Rōmaji for Japanese, Pinyin for Chinese, or the standard phonetic spelling for others).

Text to translate:
"{text}"

Provide your response strictly in the following JSON format:
{{
    "translation": "The translated text in {target_lang}",
    "pronunciation": "The phonetic pronunciation"
}}
"""
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an API that only returns valid JSON without any markdown formatting."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            response_format={"type": "json_object"},
        )
        
        response_content = chat_completion.choices[0].message.content
        result = json.loads(response_content)
        return result
    except Exception as e:
        return {"error": str(e)}

def generate_audio(text: str, target_lang: str, file_path: str = "pronunciation.mp3") -> str:
    """
    Generates an audio file for the given text using gTTS.
    """
    # Map target language to gTTS language codes
    lang_map = {
        "Japanese": "ja",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "English": "en",
        "Italian": "it",
        "Korean": "ko",
        "Chinese": "zh-CN",
        "Russian": "ru",
        # Default fallback
        "default": "en"
    }
    
    gtts_lang = lang_map.get(target_lang, lang_map["default"])
    
    if not text or not text.strip():
        return "No text to speak"
        
    try:
        tts = gTTS(text=text, lang=gtts_lang)
        tts.save(file_path)
        return file_path
    except Exception as e:
        return str(e)
