import streamlit as st
import random
import string

def password_generator(length, use_digits, use_special_char):
    characters = string.ascii_letters

    if use_digits:
        characters +=string.digits

    if use_special_char:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


st.title("THE PASSWORD GENERATOR - GET SAFE PASSWORDS")

lengths = st.slider("Select length of password", min_value=8, max_value=32, value = 16, step =1)

use_digits = st.checkbox("Include digits")
use_special_char = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = password_generator(lengths, use_digits, use_special_char)
    st.success("Password generated successfully!")
    st.write(f"Generated Password:")
    st.code(password, language="txt")
    st.write("Copy the password and use it safely")

    st.write("by: [Fatima_zohra](https://github.com/M-fatimaZohra)")
    
