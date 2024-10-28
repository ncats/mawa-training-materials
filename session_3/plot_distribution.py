import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_distribution(T_obs=None):
    # Generate a normalized Gaussian distribution
    mean = 10
    std = 2
    x = np.linspace(mean - 4*std, mean + 4*std, 1000)
    y = (1/(std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std)**2)

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Plot a solid red line at T_obs if T_obs is not None
    if T_obs is not None:
        ax.axvline(T_obs, color='red', linestyle='-', linewidth=2)

    # Set the labels
    ax.set_xlabel("Total Red Neighbor Counts T")
    ax.set_ylabel("Frequency")

    # Display the plot using Streamlit
    st.pyplot(fig)

def main():

    if 'plot_T_obs' not in st.session_state:
        st.session_state['plot_T_obs'] = False
    plot_T_obs = st.checkbox('Plot T_obs', key='plot_T_obs')

    if 'T_obs' not in st.session_state:
        st.session_state['T_obs'] = 14
    T_obs = st.number_input('Observed T:', min_value=0.0, max_value=100.0, key='T_obs', disabled=not plot_T_obs, step=0.1)

    T_obs = None if not plot_T_obs else T_obs

    plot_distribution(T_obs=T_obs)

if __name__ == "__main__":
    main()
