import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    # if re.search(r"\d", password):
    #     strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    return strength

st.title("Password Strength Meter🔐")
name1=st.text_input("enter your name")
st.write(name1)

password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_password_strength(password)
    st.progress(strength / 4)
    
    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    st.write(f"**Strength:** {levels[strength-1] if strength > 0 else 'Very Weak'}")
if st.button("signup"):
    st.write("signup-")

st.subheader("tips")
st.markdown("*use atleast 8characters")
st.markdown("*use atleast one upper and lower case")
st.markdown("*use atleast one number")
st.markdown("*use atleast 1special characters")


st.success("made by taha-Q")
