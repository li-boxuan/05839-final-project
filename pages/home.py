import streamlit as st

def write():
    st.title("Find Your Favorite Counties")
    st.header("Team Members")
    st.markdown("""
    Boxuan Li (boxuanli)

    Jiachen Wang (jw7)

    Fan Shi (fans)

    Fangwei Gao (fangweig)

    """)

    st.header("Introduction")
    st.markdown("""
    
    In this study, we explore several datasets that provides demographic, housing, climate, education and economic data for each county in the USA. 
    
    In EDA section, we cleaned the dataset and perform exploratary analysis. We found some interesting results. 
    
    - Not surprisingly, several counties from California, Massachusetts and New York have the highest median housing price. However, 19 of the top 20 counties with highest housing price growth from 2019 to 2021 are counties in Idaho
    - Among the top 10 counties with the most commute time, the majority of residents in most counties (for example, Los Angeles County, Cook County and etc.) choose to drive, while in Kings County and Queens County, a decent amount of residents choose public transportation.
    - 9 out of 20 counties with highest percent of adults with advanced degree are from Washington Metropolitan Area.

    To help users get a better understanding on different aspects of counties, we create a visualization tool where users can compare among any counties. Users can choose any aspect that they are interested in and see what are the top/last 10 counties with that aspect. Bar plots are also available for visualization. 

    By applying Nearest Neighbor, we provide a tool where users can find counties that are similar to certain counties in certain aspects. For example, a user lives in Allegheny county and they are thinking about moving. They enjoy the weather and the traffic in Allegheny, so they look for counties of similar weather and commute time. It turns out that Ashe County in NC, Hendricks County in IN, Henry County in IN, Washington County in PA and Greene County in PA are good candidates.
    """)

    st.header("Datasets")

    st.markdown("""

    The datasets come from different sources, including:

    - Demography: [Kaggle: US Census Demographic Data](https://www.kaggle.com/muonneutrino/us-census-demographic-data)  
    - Education: [Kaggle: USA Unemployment & Education Level](https://www.kaggle.com/valbauman/student-engagement-online-learning-supplement?select=education.csv)
    - Housing Price: [National Association of Realtors](https://www.nar.realtor/research-and-statistics/housing-statistics/county-median-home-prices-and-monthly-mortgage-payment)
    - Climate: [National Oceanic and Atomspheric Administration](https://www.ncdc.noaa.gov/cag/county/mapping/110/pcp/202001/12/value)
    - Economic: [Kaggle: US Economic Profile by County 1969-2019](https://www.kaggle.com/davidbroberts/us-economic-profile-by-county)

    """
    )

    st.header("Video")
    st.video("https://youtu.be/DGFUlDFOydc")
    