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


st.markdown("""
Collection of plots and visualizations from my astronomical data analysis.
            
By: Ishfahani Rusyda
            
            
**Packages used:** matplotlib, seaborn
""")

# =========================
# Plot List
# =========================
plots = [
    (
    "Cosmic Star Formation History",
    "csfh_cividis.png",
    "Plot of star formation rate density as a function of the age of the Universe (bottom x-axis) with corresponding redshift shown on the top x-axis. The figure illustrates the peak of cosmic star formation activity around redshift z ≈ 2."
    ),

    (
        "Histogram: Comparisaon of host galaxy properties from simulation and observation (DES5YR Subset).",
        "final_baseline_prop.png",
        "Histogram comparison of host galaxy properties, including redshift, stellar mass, u−r color, and Log EW[OII], between observational data and simulations. Observational data are shown as points with error bars, while simulations are represented by histograms. The chi-square statistic displayed in the top-left corner of each panel quantifies how well the simulations reproduce the observations, where values closer to 1 indicate better agreement."
    ),

    (
        "Contour plot: of host galaxies u-r color",
        "hostlibnonmpi.png",
        "Contour plots comparing different combinations of color systems and filters as functions of stellar mass (top row) and mean stellar age (middle row). The bottom row shows the distribution of host galaxy colors for each configuration."
    ),

    (
        "Mass Step as a function of Redshift",
        "mass_step_vs_redshift.png",
        "Evolution of the Hubble residual step as a function of redshift. The model prediction is shown as continuous lines, while observational data are displayed in redshift bins using points with error bars."
    ),

    (
        "Star Formation History",
        "sfh.png",
        "Normalized stellar mass formed as a function of time for galaxies with different formation times, indicated by the legend. The figure illustrates how star formation histories evolve for different galaxy populations."
    ),

    (
        "Comparison of host galaxy properties from Simulation vs Observation",
        "sim_obs_param2.png",
        "Comparison between simulated and observed host galaxy properties. The plots show u−r color and Log EW[OII] as functions of stellar mass. Simulations are represented by blue contour distributions, while observational data are shown as yellow data points."
    ),

    (
        "Density heatmap: Simulation vs Observation",
        "sim_obs_param3.png",
        "2D binned density plot comparing DES5YR observations (top) and simulations (bottom). The x-axis shows stellar mass, log(M*/M☉), and the y-axis shows rest-frame u−r color (SDSS Vega). The colormap represents Log EW[OII], with yellow indicating higher values and blue indicating lower values."
    ),

    (
        "Histogram and CDF: Comparison of three dataset",
        "SN_comp_hostlibmpi.png",
        "Histogram and cumulative distribution function (CDF) comparison between DES5YR observations, a DES5YR subset, and simulations. The panels show distributions of redshift, host galaxy stellar mass log(Mass/M☉), and rest-frame U−R host galaxy color. KS statistics and p-values are included to evaluate the similarity between observed and simulated samples."
    ),


]

# =========================
# Display Plots
# =========================
for title, filename, caption in plots:

    st.subheader(title)

    image = Image.open(f"plots/{filename}")

    st.image(
    image,
    width="stretch"
    )

    st.markdown(
        f"<p style='font-size:18px;'>{caption}</p>",
        unsafe_allow_html=True
    )

    st.write("---")