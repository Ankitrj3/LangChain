import promptTemplate as pt
import streamlit as st

st.title("Generating names for your best friends using Google Gemini LLM integrated with LangChain!")

living_being = st.text_input(label="Enter the details about your best friend:")
if st.button("Generate Names"):
    names = pt.generate_names(living_being)
    st.write("Here are some funny calling names for your best friend:")
    st.write(names)

