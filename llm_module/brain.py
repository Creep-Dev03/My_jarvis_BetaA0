# llm_module/brain.py
from llama_cpp import Llama
import os

MODEL_PATH = "data/models/phi3/Phi-3-mini-4k-instruct-q4.gguf"

# Inicializar LLM global
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,         # suficiente para tu RAM, evita usar 4096 completos
    n_threads=8,        # tu i5 13va gen tiene 8 hilos, podemos usar todos
    n_gpu_layers=20     # usa tu RTX 4060 8GB para acelerar (ajustable)
)

def ask(prompt: str, max_tokens=150) -> str:
    """
    Envía prompt al LLM y devuelve solo la primera respuesta limpia.
    """
    # Envolver el prompt en formato de chat para Phi
    chat_prompt = f"<|user|>\n{prompt}<|end|>\n<|assistant|>\n"

    output = llm(
        chat_prompt,
        max_tokens=max_tokens,
        stop=["<|end|>", "<|user|>"]  # asegura que corte al final de la respuesta
    )

    text = output["choices"][0]["text"].strip()

    # Tomar solo la primera línea si hay <br>
    if "<br>" in text:
        text = text.split("<br>")[0].strip()

    return text
