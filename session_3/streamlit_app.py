import streamlit as st

from plot_slide import main as plot_slide
from plot_distribution import main as plot_distribution

for key in st.session_state.keys():
    st.session_state[key] = st.session_state[key]

pg = st.navigation([
    st.Page(plot_slide, title="Plot slide", url_path="plot-slide"),
    st.Page(plot_distribution, title="Plot distribution", url_path="plot-distribution"),
])

st.set_page_config(page_title="Generate PPT figures", page_icon=":material/edit:")

pg.run()
