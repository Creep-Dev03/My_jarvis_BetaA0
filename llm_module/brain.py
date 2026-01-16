# llm_module/brain.py
from llama_cpp import Llama
import os

MODEL_PATH = "data/models/phi3/Phi-3-mini-4k-instruct-q4.gguf"

# Inicializar LLM global
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,        
    n_threads=8,       
    n_gpu_layers=-1    
)

def ask(prompt: str, max_tokens=150) -> str:
    """
    Envía prompt al LLM y devuelve solo la primera respuesta limpia.
    """
    
    chat_prompt = f"<|user|>\n{prompt}<|end|>\n<|assistant|>\n"

    output = llm(
        chat_prompt,
        max_tokens=max_tokens,
        stop=["<|end|>", "<|user|>"]  
    )

    text = output["choices"][0]["text"].strip()

  
    if "<br>" in text:
        text = text.split("<br>")[0].strip()

    return text

