import openai
import os

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client (New API format)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def ask_gpt(prompt: str) -> str:
    """Send a query to OpenAI GPT-4 and return the response."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cocktail expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
