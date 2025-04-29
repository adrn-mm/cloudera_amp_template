import streamlit as st
import pandas as pd

st.title("Cloudera AMP Test - Streamlit Minimal App")

# Input sederhana
user_input = st.text_input("Masukkan nama Anda:", "")

# Membuat dataframe dari input
if user_input:
    df = pd.DataFrame({
        "Nama": [user_input],
        "Pesan": [f"Selamat datang di Cloudera AMP, {user_input}!"]
    })
    st.write("Hasil:")
    st.dataframe(df)
else:
    st.write("Silakan masukkan nama Anda di atas.")