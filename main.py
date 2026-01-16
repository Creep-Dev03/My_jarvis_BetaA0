# main.py
from utils.audio_tools import record_seconds, list_input_devices
from whisper_module.transcriber import transcribe_file
from llm_module.brain import ask
from tts_module.speaker import speak
from commands.actions import execute_command


def main():
    # Mostrar dispositivos de entrada disponibles
    print("Dispositivos de entrada disponibles (id, nombre):")
    for idx, name in list_input_devices():
        print(idx, "-", name)

    # Graba 5 segundos (device=0 fuerza a usar el predeterminado, mono(channels=1) para evitar problemas con whisper)
    audio_path = record_seconds(seconds=5, device=0, fs=48000, channels=1)
    
    # Transcribe audio con Whisper
    text = transcribe_file(audio_path, language="es")
    text = text.strip()  # limpia espacios y saltos de línea
    print("\n--- TRANSCRIPCIÓN ---")
    print(text)
    
    if not text:
        print("No escuché nada, intentemos de nuevo.")
        return #hara que la función acabe aqui si no hay nada
    
    response = execute_command(text)

    if response is None:
        # Pasa la transcripción al LLM y obtiene respuesta
        response = ask(text)
        # Limpiar respuesta de etiquetas HTML o saltos de línea excesivos
        response = response.replace("<br>", "\n").replace("<|assistant|>", "").replace("<|end|>", "").strip()

    print("\n--- RESPUESTA DEL LLM ---")
    print(response)

    # Habla la respuesta
    speak(response)

if __name__ == "__main__":
    main()
