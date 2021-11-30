import awesome_streamlit as ast
import streamlit as st

import pages.home
import pages.eda
import pages.visualization

PAGES = {
    "Home": pages.home,
    "EDA": pages.eda,
    "Visualization": pages.visualization,
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)


if __name__ == "__main__":
    main()