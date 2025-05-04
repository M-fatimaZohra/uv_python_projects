import re
import streamlit as st

import random
import string

common_passwords = [
    "Password123!",
    "Admin@123",
    "Qwerty@123",
    "Welcome#123",
    "P@ssw0rd",
    "Letmein@1",
    "Test@123",
    "Summer2023!",
    "Winter#2024",
    "User@1234",
    "Abc@1234",
    "Login@123",
    "Passw0rd!",
    "1qaz@WSX",
    "ChangeMe@123",
    "TempPass@1",
    "October2023@",
    "Default#123",
    "Spring2024!",
    "Autumn@2023",
    "P@55word",
    "Company@123",
    "Root@2024",
    "Secret@321",
    "Welcome123!",
    "MyPass@2023",
    "Secure#1234",
    "UpdateMe@1",
    "Example@123",
    "Test123@!"
]

#password generator function
def password_generator(length, use_digits, use_special_char):
    characters = string.ascii_letters

    if use_digits:
        characters +=string.digits

    if use_special_char:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


#password cheaker function
def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.write(" :blue[Password should be at least 8 characters long.]")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.write(" :blue[Include both uppercase and lowercase letters.]")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.write(" :blue[Add at least one number (0-9).]")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=\[\]{};:'\",.<>/?\\|`~\-]"
, password):
        score += 1
    else:
        st.write(" :blue[Include at least one special character (!@#$%^&*).]")
    
    # Common Password Check

    if password in common_passwords:
        st.write(f" :blue[password {password} is following the criteria but still weak, at its is one of common passwords]")
        score -=3
    
    # Strength Rating
    if score == 4:
        st.write("#### :green[🟢 Strong Password!]")
        st.write(f"#### :green[{score} out of 4]")
        st.code(f"{password}", language="txt")
    elif score == 3:
        st.write("##### :orange[🟡 Moderate Password - Consider adding more security features.]")
        st.write(f"##### :orange[{score} out of 4]")
    else:
        for i in range(4):
            mid = len(password) // 2
            #create a suggested password
            suggested = password[:mid] + random.choice(string.ascii_uppercase) + random.choice("!@#$%&*")+ str(random.randint(10, 99)) +password.replace("a", "@").replace("s", "$").replace("o", "0")+password[:mid]
            
            st.write("###### Suggested Password:")
            st.code(f"{suggested}", language="txt")

        st.write("##### :red[🔴 Weak Password - Improve it using the suggestions above.]")
        st.write(f"##### :red[{score} out of 4]")

# Passowrd checker UI
st.title("Password Strength Checker")
# Get user input

password = st.text_input("Enter your password:")
if st.button("Check Password Strength"):
    if password == "":
        st.write(" :blue[Please enter a password to check its strength.]")
    else:    
      check_password_strength(password)



# password generator UI
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

    


st.write("##### :green[by: [Fatima_zohra](https://github.com/M-fatimaZohra)]")   
