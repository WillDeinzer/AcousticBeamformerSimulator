import numpy as np
from plot import plot_intensity 
from scipy.signal import find_peaks

def get_maxima_and_minima(x_positions, intensities, prominence=0.01):
    max_idx, _ = find_peaks(intensities, prominence=prominence)
    min_idx, _ = find_peaks(-intensities, prominence=prominence)
    return x_positions[max_idx], x_positions[min_idx]

def speaker_positions(num_speakers, spacing):
    half_span = (num_speakers - 1) * spacing / 2
    return np.linspace(-half_span, half_span, num_speakers)

def calculate_intensity(num_speakers, spacing, obs_distance, frequency, steering_angle):
    speaker_array = speaker_positions(num_speakers, spacing)
    wavelength = 343 / frequency
    x_range = max(2.0, 5 * wavelength)
    x_positions = np.linspace(-x_range, x_range, 1000)

    k = (2 * np.pi) / wavelength

    phase_offsets = -k * speaker_array * np.sin(np.radians(steering_angle))

    # We can keep this amplitude as 1.0, since we care about the overall shape of the intensity graph, not the true values
    A_0 = 1.0
    
    intensities = np.zeros(len(x_positions))

    for i in range(len(x_positions)):
        x_position = x_positions[i]
        total_amplitude = 0 + 0j
        for j in range(len(speaker_array)):
            r = np.sqrt(np.square(x_position - speaker_array[j]) + np.square(obs_distance))
            phase = (k * r + phase_offsets[j]) % (2*np.pi)
            # To compute the amplitude, we use (A_0 / r) * e^(i * phase) - amplitude decreases with a factor of 1/r
            total_amplitude += (A_0 / r) * np.exp(1j * phase)
        intensities[i] = np.square(np.abs((total_amplitude)))
    maxima, minima = get_maxima_and_minima(x_positions, intensities)
    print(f"Maxima positions: {maxima}")
    print(f"Minima positions: {minima}")
    plot_intensity(x_positions, intensities)

