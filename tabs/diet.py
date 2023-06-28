import streamlit as st
from webFunction import train_model

def app(df,X,y,):
    st.write("This page will display information about the personalised diet")
    model, score=train_model(X,y)

