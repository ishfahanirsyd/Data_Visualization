import streamlit as st
from PIL import Image

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Astronomical Data Visualization",
    layout="wide"
)

# =========================
# Title
# =========================
st.title("Astronomical Data Visualization")

st.write(
    "Collection of plots and visualizations from my astronomical data analysis."
)

# =========================
# Plot List
# =========================
plots = [
    ("csfh_cividis.png", "Cosmic star formation history visualization."),
    ("final_baseline_prop.png", "Baseline property comparison plot."),
    ("hostlibnonmpi.png", "Host galaxy library analysis (non-MPI version)."),
    ("mass_step_vs_redshift.png", "Mass step evolution as a function of redshift."),
    # ("obs_color_step.png", "Observed color step relation."),
    # ("sfh.png", "Star formation history plot."),
    # ("sim_obs_param2.png", "Simulation vs observation comparison for parameter set 2."),
    # ("sim_obs_param3.png", "Simulation vs observation comparison for parameter set 3."),
    # ("SN_comp_hostlibmpi.png", "Supernova comparison using MPI host library."),
    # ("SNUR_age_hostlibnonmpi.png", "Supernova age analysis using non-MPI host library."),
]

# =========================
# Display Plots
# =========================
for filename, caption in plots:

    st.subheader(filename.replace(".png", "").replace("_", " ").title())

    image = Image.open(f"plots/{filename}")

    st.image(
    image,
    caption=caption,
    width="stretch"
)

    st.write("---")