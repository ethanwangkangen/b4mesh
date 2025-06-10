def clean_performance_file():
    input_path = "Traces/Performances-Continuous.txt"
    output_path = "cleaned.txt"

    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        current_time = None
        last_written_time = None  # Track last time we wrote to avoid duplicates

        for line in infile:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            if line.startswith("Data at"):
                # Extract timestamp
                current_time = line.split("Data at")[1].strip()

                # Write comment line only if new time (different from last_written_time)
                if current_time != last_written_time:
                    outfile.write("\n")
                    outfile.write(f"# Data at {current_time}\n")
                    last_written_time = current_time
            else:
                try:
                    float(line)
                    outfile.write(line + "\n")
                except ValueError:
                    continue

if __name__ == "__main__":
    clean_performance_file()

