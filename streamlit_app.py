import awesome_streamlit as ast
import streamlit as st

import pages.home
import pages.eda
import pages.visualization
import pages.favored_county

PAGES = {
    "Home": pages.home,
    "EDA": pages.eda,
    "Visualization": pages.visualization,
    "Find Your Favored Counties": pages.favored_county,
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()