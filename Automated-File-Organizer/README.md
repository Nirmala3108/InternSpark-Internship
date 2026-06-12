# Automated File Organizer

## Project Overview

Automated File Organizer is a Python automation script that helps users organize and manage files efficiently.

The application can:

- Organize files by category
- Rename files automatically
- Delete empty folders
- Generate operation logs
- Handle exceptions
- Accept user input

---

## Features

✔ File Sorting

✔ Automatic Renaming

✔ Empty Folder Cleanup

✔ Logging System

✔ Exception Handling

✔ Interactive Menu

---

## Technologies Used

- Python
- OS Module
- Shutil Module
- Datetime Module

---

## Project Structure

Automated-File-Organizer/

├── file_organizer.py

├── logger.py

├── config.py

├── README.md

├── logs/

│ └── organizer.log

└── sample_files/

---

## How To Run

1. Clone the repository

git clone https://github.com/yourusername/Automated-File-Organizer.git

2. Navigate to project folder

cd Automated-File-Organizer

3. Run application

python file_organizer.py

---

## Sample Input

Enter Folder Path:

D:\Downloads

Choose Option:

1

---

## Sample Output

Moved: image.jpg → Images

Moved: report.pdf → Documents

Moved: movie.mp4 → Videos

Organization Completed Successfully

Total Files Moved: 3

---

## Log Output

[2026-06-11 14:00:00] Moved 'image.jpg' to 'Images' folder

[2026-06-11 14:00:01] Moved 'report.pdf' to 'Documents' folder

[2026-06-11 14:00:02] Organization completed. 3 files moved.

---

## Author

Nirmala