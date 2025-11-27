import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calculations import calculate_intensity

class BeamformerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Beamformer Simulator")
        self.root.geometry("400x300")

        input_frame = ttk.Frame(root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(input_frame, text="Number of Speakers (between 2 and 4)").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_speakers = tk.IntVar(value=2)
        speaker_spinbox = ttk.Spinbox(input_frame, from_=2, to=4, textvariable=self.num_speakers, width=15)
        speaker_spinbox.grid(row=0, column=1, pady=5)
        
        ttk.Label(input_frame, text="Speaker Spacing (m):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.spacing = tk.DoubleVar(value=0.1)
        spacing_entry = ttk.Entry(input_frame, textvariable=self.spacing, width=15)
        spacing_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(input_frame, text="Observation Distance (m):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.distance = tk.DoubleVar(value=1.0)
        distance_entry = ttk.Entry(input_frame, textvariable=self.distance, width=15)
        distance_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(input_frame, text="Frequency (Hz):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.frequency = tk.DoubleVar(value=4000)
        freq_entry = ttk.Entry(input_frame, textvariable=self.frequency, width=15)
        freq_entry.grid(row=3, column=1, pady=5)
        
        ttk.Label(input_frame, text="Speaker width (m):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.speaker_width = tk.DoubleVar(value=0.003)
        angle_entry = ttk.Entry(input_frame, textvariable=self.speaker_width, width=15)
        angle_entry.grid(row=4, column=1, pady=5)
        
        run_button = ttk.Button(input_frame, text="Run Simulation", command=self.simulate)
        run_button.grid(row=5, column=0, columnspan=2, pady=20)

    def simulate(self):
        n_speakers = self.num_speakers.get()
        speaker_spacing = self.spacing.get()
        obs_distance = self.distance.get()
        frequency = self.frequency.get()
        speaker_width = self.speaker_width.get()

        if n_speakers < 1 or speaker_spacing < 0 or obs_distance < 0 \
            or frequency < 0 or speaker_width < 0:
            messagebox.showerror("Invalid Input", "Invalid inputs")
            return
        else:
            calculate_intensity(n_speakers, speaker_spacing, obs_distance, frequency, speaker_width)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = BeamformerGUI(root)
    root.mainloop()