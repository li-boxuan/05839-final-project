import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_URL = "./datasets/merged.csv"

def load_data():
    df = pd.read_csv(DATA_URL)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df["County"] = df["County"] + ", " + df["State"]
    df.drop("State", axis=1, inplace=True)
    df.drop("GeoFIPS", axis=1, inplace=True)
    df.set_index("County", inplace=True)
    return df

def draw_top_ten(full_data, columns):
    st.subheader("Top 10 Counties with...")
    keyword = st.selectbox(
        "Top 10 counties with...",
        columns
    )
    # st.write(keyword)
    df = full_data[[keyword]].sort_values(by=keyword, ascending=False).head(10)
    df["County"] = df.index
    fig, ax = plt.subplots()
    sns.barplot(y="County", x=keyword, data=df, ax=ax, orient="h")
    st.pyplot(fig)


def draw_bottom_ten(full_data, columns):
    st.subheader("Bottom 10 Counties with...")
    keyword = st.selectbox(
        "Bottom 10 counties with...",
        columns
    )
    # st.write(keyword)
    df = full_data[[keyword]].sort_values(by=keyword, ascending=True).head(10)
    df["County"] = df.index
    fig, ax = plt.subplots()
    sns.barplot(y="County", x=keyword, data=df, ax=ax, orient="h")
    st.pyplot(fig)


def write():
    st.header("Data Visualization")
    st.write("Let us have a look at the dataset and get an intuition behind the data!")

    full_data = load_data()
    
    # st.dataframe(full_data)

    st.subheader("Browse counties as you like")
    counties = st.multiselect(
        'View data of :',
        full_data.index,
        ["Allegheny, Pennsylvania"]
    )
    # st.write(counties)
    df_counties = full_data.loc[counties]
    st.dataframe(df_counties)

    columns = full_data.columns
    draw_top_ten(full_data, columns)
    draw_bottom_ten(full_data, columns)
