from transformers import pipeline

# Load an LLM from Hugging Face
llm_pipeline = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

def ask_hf_llm(prompt: str) -> str:
    """Query Hugging Face model for cocktail advice."""
    response = llm_pipeline(prompt, max_length=150, do_sample=True)
    return response[0]["generated_text"]
