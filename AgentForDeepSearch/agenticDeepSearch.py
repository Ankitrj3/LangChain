import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType, load_tools

load_dotenv()

def langchain_agent_tool(user_query: str):
    api_key = os.getenv("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.6,
        google_api_key=api_key
    )

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    template = """
    You are a knowledgeable assistant. Use reliable data and perform necessary calculations.
    Question: {question}
    """
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )

    formatted_prompt = prompt.format(question=user_query)
    result = agent.run(formatted_prompt)
    return result

if __name__ == "__main__":
    user_input = "What is the average height of humans in India? Multiply that value by 2."
    print(langchain_agent_tool(user_input))
