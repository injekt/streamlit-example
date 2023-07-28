import streamlit as st
from langchain.llms import OpenAI
st.set_page_config(page_title="🦜🔗 Quickstart App")
st.title('🦜🔗 Quickstart App')

temperature = st.sidebar.number_input('temperature', min_value=0.0, max_value=1.0, value=0.7, step=0.1)

def generate_response(input_text):
  llm = OpenAI(temperature=temperature)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  generate_response(text)