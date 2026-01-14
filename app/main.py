import sys
from datetime import datetime

def analyze_log(file_path, date_filter=None):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(maxsplit=3)

            if len(parts) < 3:
                continue

            date = parts[0]
            level = parts[2].upper()

            if date_filter and date != date_filter:
                continue

            if level in counts:
                counts[level] += 1

    return counts



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile> [YYYY-MM-DD]")
        sys.exit(1)

    log_file = sys.argv[1]
    date_filter = sys.argv[2] if len(sys.argv) == 3 else None

    results = analyze_log(log_file, date_filter)

    print("Log Summary:")
    for level, count in results.items():
        print(f"{level}: {count}")
