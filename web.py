import streamlit as st
import functuns

todos = functuns.get_todos()

st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")