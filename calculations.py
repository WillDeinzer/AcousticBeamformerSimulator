import numpy as np
from plot import plot_intensity 
from scipy.integrate import quad
from scipy.signal import find_peaks

def get_maxima_and_minima(x_positions, intensities, prominence=0.01):
    max_idx, _ = find_peaks(intensities, prominence=prominence)
    min_idx, _ = find_peaks(-intensities, prominence=prominence)
    return x_positions[max_idx], x_positions[min_idx]

def speaker_positions(num_speakers, spacing):
    half_span = (num_speakers - 1) * spacing / 2
    return np.linspace(-half_span, half_span, num_speakers)

# Integrand for a single speaker at an observation point
def integrand(y, x_n, x_obs, obs_distance, A, k):
    r_n = np.sqrt((x_obs - x_n - y)**2 + obs_distance**2)
    complex_val = (A / r_n) * np.exp(1j * k * r_n)
    return complex_val.real, complex_val.imag

# Get the pressure value for a single observation point (result of the integral)
# Uses numerical integration, since there is no closed form analytic solution
def calculate_pressure(x_obs, centers, obs_distance, A, k, a):
    total_real = 0
    total_imag = 0
    for x_n in centers:
        real, _ = quad(lambda y: integrand(y, x_n, x_obs, obs_distance, A, k)[0], -a/2, a/2)
        imag, _ = quad(lambda y: integrand(y, x_n, x_obs, obs_distance, A, k)[1], -a/2, a/2)
        total_real += real
        total_imag += imag
    return total_real + 1j * total_imag


def calculate_intensity(num_speakers, spacing, obs_distance, frequency, speaker_width):
    speaker_centers = speaker_positions(num_speakers, spacing)
    k = 2 * np.pi * frequency / 343.0
    a = speaker_width
    A = 1.0
    obs_locations = np.linspace(-1.0, 1.0, 1000)
    intensities = []
    for x_obs in obs_locations:
        pressure = calculate_pressure(x_obs, speaker_centers, obs_distance, A, k, a)
        intensities.append(np.abs(pressure)**2)
    plot_intensity(obs_locations, intensities)

