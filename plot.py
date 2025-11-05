import matplotlib.pyplot as plt

def plot_intensity(y_positions, intensities):
    plt.figure(figsize=(10, 7))
    plt.title('Intensity at each position value')
    plt.xlabel('Position (m)')
    plt.ylabel('Relative intensity')

    plt.plot(y_positions, intensities, c='b')
    plt.show()