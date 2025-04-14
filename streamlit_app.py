# Data
import streamlit as st
st.title("Mon premier Streamlit")
st.write("Introduction")
if st.checkbox("Afficher"):
  st.write("Suite du Streamlit")

df=pd.read_csv("train.csv")

st.title("Projet de classification binaire Titanic")
st.sidebar.title("Sommaire")
pages=["Exploration", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Aller vers", pages)
