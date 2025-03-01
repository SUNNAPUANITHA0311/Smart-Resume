import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))

# List available models
models = genai.list_models()
for model in models:
    print(model.name)