import openai
import os

# Get OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set API key globally
openai.api_key = OPENAI_API_KEY

def ask_gpt(prompt: str) -> str:
    """Send a query to OpenAI GPT-4 and return the response."""
    response = openai.ChatCompletion.create(
        model="gpt-3",
        messages=[
            {"role": "system", "content": "You are a cocktail expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"]
