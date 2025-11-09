import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def generate_names(living_being: str):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7, google_api_key=os.getenv("GEMINI_API_KEY"))
    prompt_template = PromptTemplate(
        input_variables=["living_being"],
        template="Suggest some funny calling names for a {living_being}. suggest 7 unique names only."
    )
    chain = prompt_template | llm
    response = chain.invoke({"living_being": living_being})
    return response.content

if __name__ == "__main__":
    print(generate_names("Likhitha sri she is my best friend"))
