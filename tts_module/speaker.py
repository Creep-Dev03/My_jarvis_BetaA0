#habla, (convierte la respuesta para que genere uh audio xd)
import pyttsx3

engine = pyttsx3.init()

def speak(text: str):
    """Convierte texto a voz usando pyttsx3."""
    # Ajustes opcionales
    engine.setProperty('rate', 180)   # Velocidad de habla
    engine.setProperty('volume', 1.0) # Volumen (0.0 a 1.0)

    voices = engine.getProperty('voices')
    # Seleccionar voz (0 = hombre, 1 = mujer normalmente en Windows)
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()
