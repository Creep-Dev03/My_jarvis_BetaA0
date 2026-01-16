#sera el responsable de grabar los audios
# utils/audio_tools.py
import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import os

DEFAULT_FS = 16000  # Whisper funciona bien con 16 kHz

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def unique_filename(folder="data/audios", prefix="audio", ext="wav"):
    ensure_dir(folder)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    idx = 1
    while True:
        name = f"{prefix}_{ts}_{idx}.{ext}"
        path = os.path.join(folder, name)
        if not os.path.exists(path):
            return path
        idx += 1

def record_seconds(seconds=5, fs=DEFAULT_FS, device=None, channels=1, folder="data/audios"):
    """
    Graba 'seconds' segundos y guarda WAV en data/audios con nombre único.
    device: id del dispositivo (opcional)
    Retorna la ruta del archivo guardado.
    """
    frames = int(seconds * fs)
    print(f"Grabando {seconds}s a {fs}Hz ...")
    recording = sd.rec(frames, samplerate=fs, channels=channels, dtype="int16", device=device)
    sd.wait()
    filename = unique_filename(folder=folder)
    write(filename, fs, recording)
    print(f"Grabación guardada en: {filename}")
    return filename

def list_input_devices():
    """
    Devuelve lista de dispositivos de entrada (útil para elegir device id).
    """
    devices = sd.query_devices()
    inputs = []
    for i, d in enumerate(devices):
        if d['max_input_channels'] > 0:
            inputs.append((i, d['name']))
    return inputs
