import os
from datetime import datetime

# Log folder and file
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "organizer.log")

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

def write_log(message):
    """Write messages to the log file with timestamp."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Example usage
write_log("File Organizer started.")
write_log("Sample file moved successfully.")