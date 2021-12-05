import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data

DATA_URL = "./datasets/merged.csv"

feature_columns = ['Total Population', 'Men Percentage',
       'Women Percentage', 'Hispanic Percentage', 'White Percentage',
       'Black Percentage', 'Native Percentage', 'Asian Percentage',
       'Pacific Percentage', 'Drive', 'Carpool', 'Transit', 'Walk',
       'OtherTransp', 'WorkAtHome', 'MeanCommute', 'income',
       'Total Employment Rate', 'Salary', 'Housing Price', 'Temperature Avg',
       'Temperature Max', 'Temperature Min', 'Precipitation',
       'Advanced Degree Percentage']
@st.cache
def load_data():
    df = pd.read_csv(DATA_URL)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df = df.round(2)
    counties_map = alt.topo_feature(data.us_10m.url, 'counties')
    return df, counties_map

def write():
    st.header("Map Visualization")
    st.write("Let us have a quick view of datasets on Map!")
    full_data, counties_map = load_data()
    all_state = full_data['State'].unique()

    selected_feature = st.selectbox("Select a feature to view", feature_columns, index=0)
    country_chart = alt.Chart(counties_map).mark_geoshape().encode(
        color=alt.Color('{}:Q'.format(selected_feature), scale=alt.Scale(type='linear')),
        tooltip=['County:N', '{}:Q'.format(selected_feature)],
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(full_data, 'GeoFIPS', ['County', selected_feature]),
    ).properties(
        width=700,
        height=400
    ).project(
        type='albersUsa'
    )
    st.write(country_chart)

    selected_state = st.selectbox("Select a State to view more details", all_state, index=4)
    state_chart = alt.Chart(counties_map).mark_geoshape().encode(
        color=alt.Color('{}:Q'.format(selected_feature), scale=alt.Scale(type='linear')),
        tooltip=['County:N', '{}:Q'.format(selected_feature)],
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(full_data[full_data['State'] == selected_state], 'GeoFIPS', ['County', selected_feature]),
    ).properties(
        width=700,
        height=400
    ).project(
        type='albersUsa'
    )
    st.write(state_chart)
