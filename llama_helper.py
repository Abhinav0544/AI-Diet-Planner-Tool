# llama_helper.py
from llama_cpp import Llama

# Load your quantized LLaMA model (.gguf) only once
llm = Llama(
    model_path="/Users/abhinavjaikumar/Downloads/llama-3-8b-Instruct.Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=6
)

def ask_llama(prompt: str, max_tokens: int = 1024) -> str:
    response = llm(prompt, max_tokens=max_tokens)  # removed stop
    return response["choices"][0]["text"].strip()

