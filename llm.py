import streamlit as st
from langchain_groq import ChatGroq

# Initialize the ChatGroq instance
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"
)

st.title("simple LLM Charbot")
st.write("Enter your query below:")
user_input = st.text_input("Your Qusetion :", "")


if st.button("Get Answer"):
  response = llm.invoke(user_input)
  st.write("### Response:")
  st.write(response)