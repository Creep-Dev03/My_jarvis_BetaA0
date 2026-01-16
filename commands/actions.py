from datetime import datetime

def execute_command(text):
    """primera prueba de función"""
    text = text.lower()
    if "hora" in text:
        ahora = datetime.now()
        return f"Son las {ahora.strftime('%H:%M')}."
    return None