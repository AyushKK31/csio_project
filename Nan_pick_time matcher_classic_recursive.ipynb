#code for the recursive and clasic stta lta

# classic sta lta using 1_3 window 


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from obspy import read
from obspy.signal.trigger import classic_sta_lta

# Function to sanitize file names (removes special characters)
def sanitize_filename(name):
    return name.replace(".", "").replace(":", "").replace("-", "").replace("_", "")

# Load the pick data
pick_data = pd.read_csv(
    "dataset_earthquakes/metadata.csv", 
    usecols=['trace_name_original_Z', 'trace_p_pick_time', 'trace_s_pick_time', 'source_sensor_distance']
)

# Filter out cases where P-pick time is missing
missing_p_pick_data = pick_data[pick_data["trace_p_pick_time"].isna()]

# Directory containing miniSEED files
mseed_dir = Path("miniSEED_files")
output_dir = Path("output_missing_p_pick_classic_2")
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

# Define STA/LTA parameters
sta_window = 1  # Short-Term Average window (seconds)
lta_window = 3  # Long-Term Average window (seconds)
threshold = 2.0  # Threshold for marking STA/LTA peaks

# Debug: Print available files (sanitized)
available_files = {sanitize_filename(f.name): f for f in mseed_dir.glob("*")}
print("Available MSEED files:", list(available_files.keys()))

# Loop through each miniSEED file where P-pick time is missing
for _, row in missing_p_pick_data.iterrows():
    original_name = row["trace_name_original_Z"].strip()
    sanitized_name = sanitize_filename(original_name)  # Sanitize name
    file_path = available_files.get(sanitized_name)  # Get matching file

    if file_path is None:
        print(f"⚠️ File not found: {original_name} (Sanitized: {sanitized_name})")
        continue

    print(f"✅ Processing file: {file_path}")

    # Read the miniSEED file
    stream = read(str(file_path))

    for trace in stream:
        print(f"Processing trace: {trace.id}")

        # Get the sampling rate of the trace
        sampling_rate = trace.stats.sampling_rate

        # Compute STA/LTA using classic method
        try:
            cft = classic_sta_lta(trace.data, int(sta_window * sampling_rate), int(lta_window * sampling_rate))
        except Exception as e:
            print(f"Error computing STA/LTA for trace {trace.id}: {e}")
            continue

        # Get time axis
        times = trace.times("matplotlib")

        # Find where STA/LTA ratio ≥ threshold
        significant_indices = np.where(cft >= threshold)[0]
        significant_times = times[significant_indices]

        # Plot the waveform and STA/LTA ratio
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # Plot the waveform
        ax1.plot(times, trace.data, label=f"Waveform: {trace.id}", color="blue", alpha=0.6)
        ax1.set_xlabel("Time (UTC)")
        ax1.set_ylabel("Amplitude")
        ax1.set_title(f"Waveform and Classic STA/LTA: {trace.id} (Missing P-Pick)")
        ax1.legend(loc="upper left")
        ax1.grid()

        # Plot the STA/LTA ratio
        ax2 = ax1.twinx()
        ax2.plot(times[:len(cft)], cft, label="Classic STA/LTA Ratio", color="orange")
        ax2.set_ylabel("STA/LTA Ratio")
        ax2.legend(loc="upper right")

        # Mark times where STA/LTA ratio is ≥ threshold
        for t in significant_times:
            ax1.axvline(t, color="red", linestyle="--", alpha=0.6)

        # Save the plot
        output_file = output_dir / f"{file_path.stem}_{trace.id}_missing_p_pick_classic.png"
        plt.savefig(output_file)
        plt.close()
        print(f"✅ Plot saved to: {output_file}")



# recursive sta lta window 1_3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from obspy import read
from obspy.signal.trigger import recursive_sta_lta

# Function to sanitize file names (removes special characters)
def sanitize_filename(name):
    return name.replace(".", "").replace(":", "").replace("-", "").replace("_", "")

# Load the pick data
pick_data = pd.read_csv(
    "dataset_earthquakes/metadata.csv", 
    usecols=['trace_name_original_Z', 'trace_p_pick_time', 'trace_s_pick_time', 'source_sensor_distance']
)

# Filter out cases where P-pick time is missing
missing_p_pick_data = pick_data[pick_data["trace_p_pick_time"].isna()]

# Directory containing miniSEED files
mseed_dir = Path("miniSEED_files")
output_dir = Path("output_missing_p_pick_recursive_1.7")
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

# Define STA/LTA parameters
sta_window = 1  # Short-Term Average window (seconds)
lta_window = 3  # Long-Term Average window (seconds)
threshold = 1.7  # Threshold for marking STA/LTA peaks

# Debug: Print available files (sanitized)
available_files = {sanitize_filename(f.name): f for f in mseed_dir.glob("*")}
print("Available MSEED files:", list(available_files.keys()))

# Loop through each miniSEED file where P-pick time is missing
for _, row in missing_p_pick_data.iterrows():
    original_name = row["trace_name_original_Z"].strip()
    sanitized_name = sanitize_filename(original_name)  # Sanitize name
    file_path = available_files.get(sanitized_name)  # Get matching file

    if file_path is None:
        print(f"⚠️ File not found: {original_name} (Sanitized: {sanitized_name})")
        continue

    print(f"✅ Processing file: {file_path}")

    # Read the miniSEED file
    stream = read(str(file_path))

    for trace in stream:
        print(f"Processing trace: {trace.id}")

        # Get the sampling rate of the trace
        sampling_rate = trace.stats.sampling_rate

        # Compute STA/LTA using recursive method
        try:
            cft = recursive_sta_lta(trace.data, int(sta_window * sampling_rate), int(lta_window * sampling_rate))
        except Exception as e:
            print(f"Error computing STA/LTA for trace {trace.id}: {e}")
            continue

        # Get time axis
        times = trace.times("matplotlib")

        # Find where STA/LTA ratio ≥ threshold
        significant_indices = np.where(cft >= threshold)[0]
        significant_times = times[significant_indices]

        # Plot the waveform and STA/LTA ratio
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # Plot the waveform
        ax1.plot(times, trace.data, label=f"Waveform: {trace.id}", color="blue", alpha=0.6)
        ax1.set_xlabel("Time (UTC)")
        ax1.set_ylabel("Amplitude")
        ax1.set_title(f"Waveform and Recursive STA/LTA: {trace.id} (Missing P-Pick)")
        ax1.legend(loc="upper left")
        ax1.grid()

        # Plot the STA/LTA ratio
        ax2 = ax1.twinx()
        ax2.plot(times[:len(cft)], cft, label="Recursive STA/LTA Ratio", color="orange")
        ax2.set_ylabel("STA/LTA Ratio")
        ax2.legend(loc="upper right")

        # Mark times where STA/LTA ratio is ≥ threshold
        for t in significant_times:
            ax1.axvline(t, color="red", linestyle="--", alpha=0.6)

        # Save the plot
        output_file = output_dir / f"{file_path.stem}_{trace.id}_missing_p_pick_recursive.png"
        plt.savefig(output_file)
        plt.close()
        print(f"✅ Plot saved to: {output_file}")




