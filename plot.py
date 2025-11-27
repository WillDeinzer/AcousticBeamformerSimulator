import matplotlib.pyplot as plt
import numpy as np

def plot_intensity(positions, intensities):
    normalized = intensities / np.max(intensities)
    plt.ylabel('Normalized Intensity')
    plt.figure(figsize=(10, 7))
    plt.title('Intensity at each position value')
    plt.xlabel('Position (m)')
    plt.ylabel('Relative intensity')

    plt.plot(positions, normalized, c='b')
    plt.show()