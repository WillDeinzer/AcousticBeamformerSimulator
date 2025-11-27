import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# -------------------------------
# Minimal plot function
# -------------------------------
def plot_intensity(x, intensity):
    plt.figure(figsize=(8,4))
    plt.plot(x, intensity)
    plt.xlabel("x position (m)")
    plt.ylabel("Normalized Intensity")
    plt.title("Single Speaker Diffraction Pattern")
    plt.grid(True)
    plt.show()

# -------------------------------
# Helper to find maxima/minima
# -------------------------------
def get_maxima_and_minima(x_positions, intensities, prominence=0.01):
    max_idx, _ = find_peaks(intensities, prominence=prominence)
    min_idx, _ = find_peaks(-intensities, prominence=prominence)
    return x_positions[max_idx], x_positions[min_idx]

# -------------------------------
# Single speaker far-field function
# -------------------------------
def single_speaker_far_field(x_positions, obs_distance, speaker_width, frequency, include_1_over_r=False):
    c = 343.0
    wavelength = c / frequency
    k = 2 * np.pi / wavelength

    theta = np.arctan2(x_positions, obs_distance)
    sin_theta = np.sin(theta)

    arg = 0.5 * k * speaker_width * sin_theta
    intensity = np.ones_like(arg)
    nonzero = arg != 0
    intensity[nonzero] = (np.sin(arg[nonzero]) / arg[nonzero])**2

    if include_1_over_r:
        r = np.sqrt(x_positions**2 + obs_distance**2)
        intensity *= (1 / r)**2
        intensity /= np.max(intensity)  # normalize again

    return intensity

# -------------------------------
# Wrapper to simulate and plot
# -------------------------------
def simulate_single_speaker(x_positions, obs_distance, speaker_width, frequency, include_1_over_r=False):
    intensity = single_speaker_far_field(x_positions, obs_distance, speaker_width, frequency,
                                         include_1_over_r=include_1_over_r)
    maxima, minima = get_maxima_and_minima(x_positions, intensity)
    print("Maxima positions:", maxima)
    print("Minima positions:", minima)
    plot_intensity(x_positions, intensity)
    return intensity

# -------------------------------
# Test the simulation
# -------------------------------
if __name__ == "__main__":
    # Observation line: 1 meter away, 1 meter wide range
    x_positions = np.linspace(-0.01, 0.01, 1000)  # meters
    obs_distance = 1.0                            # meters
    speaker_width = 0.01                        # 2 cm buzzer
    frequency = 4000                            # 4 kHz

    simulate_single_speaker(x_positions, obs_distance, speaker_width, frequency,
                            include_1_over_r=False)
