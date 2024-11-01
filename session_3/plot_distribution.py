from scipy.stats import norm, poisson
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_distribution(T_obs=None, fill_area=None, distribution='Gaussian'):
    mean = 10
    std = 2

    if distribution == 'Gaussian':
        x = np.linspace(mean - 4*std, mean + 4*std, 1000)
        y = (1/(std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std)**2)
        marker = None
    elif distribution == 'Poisson':
        x = np.arange(0, 30)
        y = poisson.pmf(x, mean)
        marker = 'o'

    fig, ax = plt.subplots()
    ax.plot(x, y, marker=marker, linestyle='-')

    if T_obs is not None:
        ax.axvline(T_obs, color='red', linestyle='-', linewidth=2)
        ax.text(T_obs + 0.2, max(y) * 0.95, r'$T_{\text{obs}}$', color='red', verticalalignment='bottom', fontsize=16, horizontalalignment='left')

        if fill_area == 'left':
            ax.fill_between(x, y, where=(x <= T_obs), color='green', alpha=0.5)
            if distribution == 'Gaussian':
                area = norm.cdf(T_obs, mean, std)
            elif distribution == 'Poisson':
                area = poisson.cdf(T_obs, mean)
        elif fill_area == 'right':
            ax.fill_between(x, y, where=(x >= T_obs), color='green', alpha=0.5)
            if distribution == 'Gaussian':
                area = 1 - norm.cdf(T_obs, mean, std)
            elif distribution == 'Poisson':
                area = 1 - poisson.cdf(T_obs, mean)
        else:
            area = None

        if area is not None:
            st.write(f"Area under the curve {fill_area} of T_obs: {area:.4f} (log10: {np.log10(area)})")

    ax.set_xlabel("Total Red Neighbor Counts T")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

def main():
    if 'plot_T_obs' not in st.session_state:
        st.session_state['plot_T_obs'] = False
    plot_T_obs = st.checkbox('Plot T_obs', key='plot_T_obs')

    if 'T_obs' not in st.session_state:
        st.session_state['T_obs'] = 14
    T_obs = st.number_input('Observed T:', min_value=0, max_value=100, key='T_obs', disabled=not plot_T_obs)

    T_obs = None if not plot_T_obs else T_obs

    fill_area = None
    if plot_T_obs:
        fill_area = st.radio('Fill area under the curve:', ('None', 'Left of T_obs', 'Right of T_obs'))
        if fill_area == 'Left of T_obs':
            fill_area = 'left'
        elif fill_area == 'Right of T_obs':
            fill_area = 'right'
        else:
            fill_area = None

    distribution = st.radio('Select distribution:', ('Gaussian', 'Poisson'))

    plot_distribution(T_obs=T_obs, fill_area=fill_area, distribution=distribution)

if __name__ == "__main__":
    main()
