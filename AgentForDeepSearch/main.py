import streamlit as st
import io
import sys
import agenticDeepSearch as ads

st.set_page_config(page_title="Deep Search Agent", page_icon="🧠", layout="centered")

st.title("🧠 Deep Search Agent using Google Gemini + LangChain")

st.markdown("""
This app uses **Google Gemini 2.0 Flash** with **LangChain tools (Wikipedia + Math)**  
to perform reasoning, factual lookup, and calculations interactively.
""")

user_query = st.text_input("Enter your search query:")

if st.button("Search"):
    if user_query.strip() == "":
        st.warning("⚠️ Please enter a valid query.")
    else:
        with st.spinner("🤔 Thinking... please wait"):
            
            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()

            try:
                response = ads.langchain_agent_tool(user_query)
            except Exception as e:
                response = f"❌ Error: {str(e)}"

            
            sys.stdout = old_stdout

            
            thinking_output = mystdout.getvalue()

        st.subheader("🧩 Agent Thinking Process:")
        st.code(thinking_output, language="text")

        st.subheader("✅ Final Response:")
        st.write(response)
