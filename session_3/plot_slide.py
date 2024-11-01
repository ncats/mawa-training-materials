import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def draw_slide(seed=42, alpha=1, analysis_radius=0, configuration=0):
    # Set the seed for reproducibility
    np.random.seed(seed)

    # Define the rectangular region of interest in microns
    width, height = 400, 400

    # Number of circles
    num_circles = 50

    # Generate random positions for the circles
    x_positions = np.random.uniform(0, width, num_circles)
    y_positions = np.random.uniform(0, height, num_circles)

    # Generate random colors (blue and red) with more blues than reds
    colors = np.random.choice(['blue', 'red'], num_circles, p=[0.8, 0.2])

    # Permute the colors based on the configuration
    np.random.seed(seed + configuration)
    permuted_colors = np.random.permutation(colors)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the circles with smaller size, black outline, and transparency
    for i, (x, y, color) in enumerate(zip(x_positions, y_positions, permuted_colors)):
        circle = plt.Circle((x, y), 5, color=color, ec='black', alpha=alpha)  # Circle radius set to 5 microns, edge color set to black, transparency set by alpha
        ax.add_artist(circle)

        # Draw a larger circle around red cells if the option is enabled
        if (analysis_radius != 0) and color == 'red':
            if (x - analysis_radius >= 0) and (x + analysis_radius <= width) and (y - analysis_radius >= 0) and (y + analysis_radius <= height):
                large_circle = plt.Circle((x, y), analysis_radius, color='none', ec='black', linestyle='--')
                ax.add_artist(large_circle)

                # Count the number of blue neighbors inside the analysis radius
                blue_neighbors = 0
                for j, (x2, y2, color2) in enumerate(zip(x_positions, y_positions, permuted_colors)):
                    if color2 == 'blue' and np.sqrt((x - x2)**2 + (y - y2)**2) <= analysis_radius:
                        blue_neighbors += 1

                # Place the count prominently next to the corresponding red center
                ax.text(x + 10, y, str(blue_neighbors), color='black', fontsize=12, ha='left', va='center')

    # Set the limits of the plot
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')

    # Label the axes
    ax.set_xlabel('X Coordinate (microns)')
    ax.set_ylabel('Y Coordinate (microns)')

    # Display the plot using Streamlit
    st.pyplot(fig)

def main():
    if 'seed' not in st.session_state:
        st.session_state['seed'] = 47
    seed = st.number_input('Seed:', min_value=0, max_value=1000, key='seed')

    if 'alpha' not in st.session_state:
        st.session_state['alpha'] = 1
    alpha = st.session_state['alpha']
    # alpha = st.number_input('Transparency (alpha):', min_value=0.0, max_value=1.0, value=0.5, step=0.1, key='alpha')

    if 'analysis_radius' not in st.session_state:
        st.session_state['analysis_radius'] = 0
    analysis_radius = st.number_input('Analysis Radius (microns):', min_value=0, max_value=200, step=1, key='analysis_radius')

    if 'configuration' not in st.session_state:
        st.session_state['configuration'] = 0
    configuration = st.number_input('Configuration:', min_value=0, step=1, key='configuration')

    draw_slide(seed=seed, alpha=alpha, analysis_radius=analysis_radius, configuration=configuration)

if __name__ == "__main__":
    main()
