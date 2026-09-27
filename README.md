# 📁 Python File Statistics Analyzer

A simple Python utility that analyzes files inside a selected folder and displays useful file statistics.

The project uses Python's built-in `os` module to inspect files, calculate file sizes, identify extensions, and find the largest file.

---

## 🎯 Project Goal

The goal of this project is to learn how to:

- Work with folders and files
- Use Python's `os` module
- Get file sizes
- Extract file extensions
- Store file information using dictionaries
- Calculate total file size
- Find the largest file
- Build a simple file analysis utility

---

## ✨ Features

- 📂 Analyze any folder
- 📊 Count total files
- 💾 Calculate total folder size
- 📄 Display individual file information
- 🔍 Detect file extensions
- 📈 Find the largest file
- ⚡ Uses only Python standard library

---

## 🛠️ Technologies Used

- Python
- `os` module
- Lists
- Dictionaries
- Classes and Objects
- `max()`
- Lambda functions

---

## 📁 Project Structure

```text
python-file-statistics-analyzer/
│
├── main.py
├── file_analyzer.py
├── README.md
└── .gitignore
```

---

# 🧠 Concepts Learned

## 1. `os` Module

The `os` module allows Python to interact with the operating system.

```python
import os
```

---

## 2. Checking if a Folder Exists

```python
os.path.exists(self.folder)
```

This checks whether the selected folder exists.

---

## 3. Listing Files

```python
os.listdir(self.folder)
```

This returns the names of files and folders inside the selected directory.

---

## 4. Checking for Files

```python
os.path.isfile(path)
```

This makes sure that only files are analyzed.

---

## 5. Getting File Size

```python
os.path.getsize(path)
```

This returns the file size in bytes.

The project converts bytes into KB:

```python
size / 1024
```

---

## 6. Getting File Extension

```python
os.path.splitext(name)[1]
```

For example:

```text
main.py → .py
README.md → .md
```

---

## 7. Dictionaries

Each file is stored as a dictionary:

```python
{
    "name": name,
    "size": size,
    "extension": extension
}
```

This makes the file information easy to access.

---

## 8. Finding the Largest File

The largest file is found using:

```python
largest = max(files, key=lambda file: file["size"])
```

`max()` finds the largest value, while the lambda function tells Python to compare files using their size.

---

# 🚀 How to Run

## 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/python-file-statistics-analyzer.git
```

## 2. Open the project

```bash
cd python-file-statistics-analyzer
```

## 3. Run the program

```bash
python main.py
```

## 4. Enter a folder path

Example:

```text
.
```

or:

```text
C:\Users\YourName\Documents
```

---

# 🖥️ Example Output

```text
===== FILE STATISTICS =====
Total Files: 4
Total Size : 1.59 KB

===== FILE DETAILS =====

.gitignore → 0.04 KB → No Extension
file_analyzer.py → 1.41 KB → .py
main.py → 0.14 KB → .py
README.md → 0.00 KB → .md

===== LARGEST FILE =====
Name: file_analyzer.py
Size: 1.41 KB
```

---

# 📚 What I Learned

Through this project, I learned:

- File and folder handling
- `os.listdir()`
- `os.path.exists()`
- `os.path.isfile()`
- `os.path.getsize()`
- `os.path.splitext()`
- Lists
- Dictionaries
- Classes
- Lambda functions
- `max()`
- Basic file statistics

---

# 🔮 Future Improvements

Possible future features:

- Analyze subfolders recursively
- Group files by extension
- Find duplicate files
- Find oldest and newest files
- Export statistics to CSV
- Add file-type statistics
- Create a graphical interface
- Add folder size visualization

---

# 🎓 Project Status

✅ Completed

This project was built as part of my Python learning journey to improve my understanding of file handling, automation, and data analysis.

---

# 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece