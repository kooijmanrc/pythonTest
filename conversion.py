import os
import json
 # Replace with the actual folder path
folder_path = r'C:\testlog'


# Create an empty JSON file named "RTU_LOG"
rtu_log_filename = "RTU_LOG.json"
open(rtu_log_filename, 'w').close()

# Find ".log" files in the specified folder
log_files = [file for file in os.listdir(folder_path) if file.endswith(".log")]

for log_file in log_files:
    SWCNAME = log_file.split("DATA")[0]

    with open(os.path.join(folder_path, log_file), 'r') as file:
        for line in file:
            LINE = line.split()

            if len(LINE) != 5:
                continue

            TIME = LINE[0] + " " + LINE[1]

            if LINE[3].startswith("[TX"):
                output = {
                    "SWC": SWCNAME,
                    "direction": "outgoing",
                    "data": LINE[4],
                    "TIME": TIME
                }
            elif LINE[3].startswith("[RX"):
                output = {
                    "SWC": SWCNAME,
                    "direction": "incoming",
                    "data": LINE[4],
                    "TIME": TIME
                }
            elif LINE[3].startswith("LinkStatus"):
                output = {
                    "SWC": SWCNAME,
                    "LINK": LINE[4],
                    "TIME": TIME
                }
            else:
                continue

            # Append the output to "RTU_LOG.json"
            with open(rtu_log_filename, 'a') as rtu_log_file:
                rtu_log_file.write(json.dumps(output) + "\n")

            # Print the output
            print(output)