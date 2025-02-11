import streamlit as st
from langchain_groq import ChatGroq

# Initialize the ChatGroq model (Use your actual API key here)
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    groq_api_key="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"
)

def correct_grammar(text):
    """Corrects grammar using ChatGroq LLM."""
    prompt = (
        "Check the grammar of the following text. "
        "If it's correct, return it as is. "
        "If it has grammar mistakes, correct them without changing the meaning "
        "or adding extra words. Also, list the incorrect words and provide feedback "
        "on what went wrong.\n\n"
        f"Text: {text}"
    )
    
    response = llm.invoke(prompt)  # Get AIMessage object
    corrected_text = response.content.strip()  # Extract actual text and clean it
    
    return corrected_text

# Streamlit UI
st.title("Simple LLM Grammar Checker")
st.write("Enter a sentence below to check for grammar mistakes.")

user_input = st.text_area("Enter a sentence:", "")

if st.button("Check Grammar"):
    if user_input.strip():
        corrected_text = correct_grammar(user_input)
        st.write("### Corrected Text:")
        st.write(corrected_text)
    else:
        st.warning("Please enter a sentence to check.")