import streamlit as st
import random

header = st.container()
body = st.container()

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#&*."

generated_password = alphabets + number + symbols 
length_for_password = 18

my_password = "".join(random.sample(generated_password, length_for_password))

with header:
    st.header("Password Generator")
    st.write("Password generation can sometimes be very difficult to think of. Especially when you find yourself opening a new account on the internet and you have been prompted to generate a password that is not less than 12 characters and it should include a number, both cases and a symbol. If you ever encountered this problem, then this web app is a free solution for you.\n")
    st.write("Welcome to the password generator. This web application generates an 18 character length of a password randomly.")

with body:
    if st.button("Generate Password"):
        st.write(f"\nYour generated password is: {my_password}")
        st.write("Goodbye!")