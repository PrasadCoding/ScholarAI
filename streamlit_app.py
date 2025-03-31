import streamlit as st

def page_2():
    st.title("Page 2")

pg = st.navigation(["home.py", page_2])
pg.run()
