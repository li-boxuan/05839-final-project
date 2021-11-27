import streamlit as st
import streamlit.components.v1 as components


def write():
    st.header("Exploratory Data Analysis")
    st.write("In this section, we clean & analyze the original datasets")
    st.subheader("Demography")
    components.html(open("./eda/eda_demography.html", "r", encoding='utf-8').read(), height=4800)
    st.subheader("Economics")
    components.html(open("./eda/economic_data_eda.html", "r", encoding='utf-8').read(), height=2500)
    st.subheader("Education")
    components.html(open("./eda/education.html", "r", encoding='utf-8').read(), height=3300)
    st.subheader("Housing")
    components.html(open("./eda/housing.html", "r", encoding='utf-8').read(), height=3000)
    # TODO: cannot run climate.ipynb