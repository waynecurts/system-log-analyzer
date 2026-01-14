def analyze_log(file_path):
    """
    Reads a log file and returns number of lines.
    """
    with open(file_path, "r") as file:
        return len(file.readlines())
