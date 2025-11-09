import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def generate_pet_name():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-2.0-flash')
    pet_name = model.generate_content("Suggest the dog name for a golden retriever dog. Suggest 7 unique name only.")
    return pet_name.text

if __name__ == "__main__":
    get_pet_name = generate_pet_name()
    print(get_pet_name)