import os
import numpy as np
import pandas as pd
import scipy.stats as stats
from obspy import read, UTCDateTime
from pathlib import Path

# Function to sanitize file names (removes ., :, -, _)
def sanitize_filename(name):
    return name.replace(".", "").replace(":", "").replace("-", "").replace("_", "")

# Function to compute statistics (mean, mode, std dev)
def compute_stats(data):
    if len(data) == 0:
        return {"Mean": None, "Mode": None, "Std Dev": None}
    return {
        "Mean": np.mean(data),
        "Mode": stats.mode(data, keepdims=True)[0][0] if len(data) > 1 else data[0],  
        "Std Dev": np.std(data)
    }

# Load metadata
pick_data = pd.read_csv(
    "dataset_earthquakes/metadata.csv", 
    usecols=['trace_name_original_Z', 'trace_p_pick_time', 'source_sensor_distance']
)
pick_data['sanitized_filename'] = pick_data['trace_name_original_Z'].apply(sanitize_filename)

# Directory containing miniSEED files
mseed_dir = "miniSEED_files"
output_csv = "output_stats.csv"

# Initialize a list to store results
results = []

# Loop through each miniSEED file in the directory
for file_path in Path(mseed_dir).glob("*.MSEED"):
    sanitized_mseed_name = sanitize_filename(file_path.stem)  

    # Match the sanitized name with metadata
    matched_row = pick_data[pick_data['sanitized_filename'] == sanitized_mseed_name]
    if matched_row.empty:
        continue  # Skip files without matching metadata

    p_pick_time = matched_row.iloc[0]['trace_p_pick_time']
    if pd.isna(p_pick_time):
        continue  # Skip if no P-pick time

    p_pick = UTCDateTime(p_pick_time)

    # Read the miniSEED file
    stream = read(file_path)

    for trace in stream:
        sampling_rate = trace.stats.sampling_rate  # e.g., 250 Hz
        raw_data = trace.data  

        # Compute P-pick index
        trace_start_time = trace.stats.starttime
        p_pick_index = int((p_pick - trace_start_time) * sampling_rate)

        # Ensure sufficient data exists for calculations
        if p_pick_index < 100 or p_pick_index + 200 > len(raw_data):
            continue  

        # Extract 100-sample windows
        window_1 = raw_data[p_pick_index - 100:p_pick_index]   # 100 samples before P-pick
        window_2 = raw_data[p_pick_index:p_pick_index + 100]   # 100 samples after P-pick
        window_3 = raw_data[p_pick_index + 100:p_pick_index + 200]  # Next 100 samples

        # Compute statistics
        stats_1 = compute_stats(window_1)
        stats_2 = compute_stats(window_2)
        stats_3 = compute_stats(window_3)

        # Store results
        results.append({
            "File": file_path.name,
            "Trace": trace.id,
            "P-Pick Time": p_pick_time,
            "Source-Sensor Distance": matched_row.iloc[0]['source_sensor_distance'],
            "Mean (Before)": stats_1["Mean"],
            "Mode (Before)": stats_1["Mode"],
            "Std Dev (Before)": stats_1["Std Dev"],
            "Mean (After)": stats_2["Mean"],
            "Mode (After)": stats_2["Mode"],
            "Std Dev (After)": stats_2["Std Dev"],
            "Mean (Next 100)": stats_3["Mean"],
            "Mode (Next 100)": stats_3["Mode"],
            "Std Dev (Next 100)": stats_3["Std Dev"]
        })

# Convert results to DataFrame and save to CSV
df_results = pd.DataFrame(results)
df_results.to_csv(output_csv, index=False)

print(f"Statistics saved to {output_csv}")
