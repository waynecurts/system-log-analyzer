import sys
import json
import csv
from colorama import Fore, Style, init
import matplotlib.pyplot as plt

init(autoreset=True)


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


def export_results(results):
    with open("summary.json", "w") as jf:
        json.dump(results, jf, indent=4)

    with open("summary.csv", "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(["Level", "Count"])
        for key, value in results.items():
            writer.writerow([key, value])


def plot_results(results):
    levels = list(results.keys())
    counts = list(results.values())

    plt.bar(levels, counts)
    plt.title("Log Severity Distribution")
    plt.xlabel("Level")
    plt.ylabel("Count")
    plt.show()


def detect_anomalies(results, threshold=3):
    if results["ERROR"] >= threshold:
        print(f"{Fore.RED}⚠ High error rate detected!{Style.RESET_ALL}")


def main():
    if len(sys.argv) < 2:
        print("Usage: log-analyzer <logfile> [YYYY-MM-DD]")
        sys.exit(1)

    log_file = sys.argv[1]
    date_filter = sys.argv[2] if len(sys.argv) == 3 else None

    results = analyze_log(log_file, date_filter)

    export_results(results)
    plot_results(results)
    detect_anomalies(results)

    print("\nLog Summary:")
    print(f"{Fore.GREEN}INFO:{Style.RESET_ALL} {results['INFO']}")
    print(f"{Fore.YELLOW}WARNING:{Style.RESET_ALL} {results['WARNING']}")
    print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {results['ERROR']}")


if __name__ == "__main__":
    main()
