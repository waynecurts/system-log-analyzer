import sys

def analyze_log(file_path):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("INFO"):
                counts["INFO"] += 1
            elif line.startswith("WARNING"):
                counts["WARNING"] += 1
            elif line.startswith("ERROR"):
                counts["ERROR"] += 1

    return counts
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    results = analyze_log(log_file)

    print("Log Summary:")
    for level, count in results.items():
        print(f"{level}: {count}")
