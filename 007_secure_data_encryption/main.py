import streamlit as st
import hashlib
import os  # file sys operation
from cryptography.fernet import (
    Fernet,
)  # built in encripting or decripting system: hi fatima ⇌ 56ugoy87y5441324!~@#$^$
import json  # "I implemented persistent JSON-based storage as an enhancement for better data reliability."
import time

KEY_FILE = "the_secret.key"


def load_the_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)

    else:
        with open(KEY_FILE, "rb") as file:
            key = file.read()

    return key


fr = Fernet(load_the_key())  # create a object


DATA_FILE = "data.json"


def initialize_json_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)


initialize_json_file()


def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


# sha256: secure hash algorithm, its a mathametical formula that
#        convert any input to a unique code consist of 64 characters,
#        this 64 characters are callled hash


def encription(text):
    return fr.encrypt(text.encode()).decode()  # encrypt data


def decription(encripted_text):
    return fr.decrypt(encripted_text.encode()).decode()  # decrypt data


# .encode() convert it into binary beace fernet work with binary code
# after converting to binary it convert to encription


st.title("Encrypted Data Vault")
navigation_bar = ["Encrypt data", "Decrypt data", "Login"]

choice = st.sidebar.selectbox("Choose option", navigation_bar)

if choice == "Encrypt data":
    st.header("Store Encrypt data")
    label = st.text_input("Label (must be unique): ")
    secret = st.text_area("enter your secret that you want to hide")
    passkey = st.text_input("Password: ", type="password")

    if st.button("Encrypt & Save"):
        if label and secret and passkey:
            encrypted = encription(secret)
            hash_key = hash_passkey(passkey)

            with open(DATA_FILE, "r+") as f:
                data = json.load(f)
                if label in data:
                    st.error("This Label already exists!")
                else:
                    data[label] = {"encrypted_text": encrypted, "passkey": hash_key}
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                    st.success("Data Encrypted Successfully!")

        else:
            st.warning("Please fill all fields")


elif choice == "Decrypt data":
    st.header("Get Decript data")
    label = st.text_input("Label (unique ID): ")
    passkey = st.text_input("Passkey: ", type="password")

    if st.button("Decrypt"):

        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            result = data.get(label)

        if result:
            encrypted_text = result["encrypted_text"]
            stored_hash = result["passkey"]
            hash_key = hash_passkey(passkey)
            if hash_key == stored_hash:
                decrypted = decription(encrypted_text)
                st.success(f"See your Secret: {decrypted}")

            else:
                st.error("Incorrect Passkey")
        else:
            st.warning("label not found!")


elif choice == "Login":
    st.subheader("Reauthorization Required")
    login_pass = st.text_input("Enter Main Password:", type="password")
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    if st.button("Login"):
        if st.session_state.attempts < 3:
            if login_pass == "apple_@_day_k33p_dr":
                st.success(
                    " Reauthorized successfully! Retrieving all stored secrets..."
                )
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    results = [
                        (label, info["encrypted_text"]) for label, info in data.items()
                    ]

                if results:
                    for label, encrypted_text in results:
                        try:
                            decrypted = decription(encrypted_text)
                            st.write(
                                "-------------------------------------------------------------------------------"
                            )
                            st.info(f"Label: {label}")
                            
                            st.info(f"Secret: {decrypted}")
                            st.write(
                                "-------------------------------------------------------------------------------"
                            )
                        except Exception as e:
                            st.warning(f"Could not decrypt secret for label '{label}'.")

                else:
                    st.warning("No secrets found in the vault.")
                st.session_state.attempts = 0
            else:
                st.session_state.attempts += 1
                attempts_left = 3 - st.session_state.attempts
                st.error("Incorrect password!")
                st.error(f"Attempt(s) left: {attempts_left}")
                if st.session_state.attempts == 3:
                    st.error("Run out of chances!")
        else:
            st.error("You are locked out due to too many failed attempts!")
            st.error("try after 10 seconds")
            time.sleep(10)
            st.session_state.attempts = 0
