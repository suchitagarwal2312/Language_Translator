from google_trans_new import google_translator
import streamlit as st
translator = google_translator()
st.title("Suchit's Language Translators")
text = st.text_input("Enter a text to translate")
translate = translator.translate(text, lang_tgt='fr')
st.write(translate)

#to run streamlit program... streamlit run filepath.py on anaconda prompt
