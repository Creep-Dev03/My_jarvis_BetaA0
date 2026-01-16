#literalmente de audio a texto 

import whisper
import os

# Carga global del modelo (se hace una vez)
# Usa "base" si quieres minimizar uso; "small" da más precisión.
_MODEL_NAME = os.getenv("JARVIS_WHISPER_MODEL", "base")
print(f"[Transcriber] Cargando modelo Whisper: {_MODEL_NAME} (esto tarda la primera vez)...")
_model = whisper.load_model(_MODEL_NAME)
print("[Transcriber] Modelo Whisper cargado.")

def transcribe_file(path, language=None):
    """
    Transcribe un archivo de audio (wav/mp3). Retorna string con texto.
    language: opcional, p.ej. 'es' para español (mejora en algunos casos).
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No existe el archivo: {path}")
    options = {}
    if language:
        options["language"] = language
    # Se puede pasar fp16=False si hay problemas con GPU
    result = _model.transcribe(path, **options)
    return result.get("text", "").strip()
