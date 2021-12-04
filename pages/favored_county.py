import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
from .visualization import load_data

DATA_URL = "./datasets/merged.csv"

def normalize_data(df):
    df_normalized = (df - df.mean()) / df.std()
    return df_normalized

def get_nearest_neighbors(df, columns, county):
    if len(columns) == 0:
        return []
    target = df[df["County"] == county][columns]
    target = target.dropna().to_numpy()
    data = df[columns].dropna().to_numpy()
    model = NearestNeighbors(n_neighbors = 6, ).fit(data)
    nbrs = model.kneighbors(target, return_distance=False)
    nbrs = df.loc[nbrs[0]]
    return nbrs["County"]


    
def write():    
    st.subheader("Find counties that are similiar to your favorite county in selected aspects.")


    df = load_data()
   
    df["Gender Ratio(Male/Female)"] = df["Men Percentage"] / df["Women Percentage"]
    df.drop("Men Percentage", axis=1, inplace=True)
    df.drop("Women Percentage", axis=1, inplace=True)
    df_normalize = normalize_data(df).reset_index()
    
    county = st.selectbox("Select a county of your interest", df.index)
    columns = st.multiselect("select some aspects of your interest", df.columns, ["Temperature Avg"])

    nbrs = get_nearest_neighbors(df_normalize, columns, county)

    if len(nbrs) > 0:
        st.subheader("Here are your top 5 most similiar counties, including the selected county for comparison")
        df_nbrs = df.loc[nbrs][columns]
        st.dataframe(df_nbrs)
    else:
        st.subheader("Here are your top 5 most similiar counties, including the selected county for comparison")
        st.write("Waiting for your input. Nothing to show right now.")