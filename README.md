# Assignment-4
Module 5: Files, Exceptions, and Errors in Python

# Task 1: Read a File and Handle Errors

A small Python CLI program that demonstrates **basic file I/O** and **exception handling**.  
It interactively creates (or purposefully avoids creating) a file named `sample.txt`, then attempts to read it and prints helpful error messages when appropriate.

---

## Features

- Prompts the user: _“Do you want to create `sample.txt`? (yes/no)”_
- Creates `sample.txt` with two lines when you answer **yes**
- Treats **no** as a way to test the error path (empties the file so the read step triggers the error)
- Reads and prints file content if present
- Handles:
  - Missing file or intentionally empty file → prints: `Error: The file 'sample.txt' was not found.`
  - Any other unexpected exceptions with a friendly message
- No external imports required (does **not** use `os`)

---

---

## How to Run

> **Prerequisites:** Python 3.x installed.

1. Save the code into a file, e.g., `task1_file_error_handler.py`.
2. Open a terminal in the folder containing the file.
3. Run:
   ```bash
   python task1_file_error_handler.py
   ```
4. Answer the prompt with **yes** or **no**.

---

## What Each Input Does

- **yes** → Creates `sample.txt` with two text lines and then prints them.
- **no** → Empties `sample.txt` (or leaves it missing); the read step treats an empty/missing file as “not found” and prints:
  ```
  Error: The file 'sample.txt' was not found.
  ```
- **anything else** → Prints:
  ```
  (Invalid input! please write 'yes/no' only)
  ```
  and exits without attempting to read.

---

## Error Handling Logic

- The program wraps the **read** step in a `try/except` block.
- If `sample.txt` is missing **or** is empty (checked via `reading_file.strip() == ""`), it raises/handles `FileNotFoundError` and prints a clear message.
- Any other errors are caught by the generic `except Exception as e` and reported.

---

## Why `.strip().lower()` on the Input?

- `strip()` removes leading/trailing whitespace (so `" yes "` works).
- `lower()` makes the check case-insensitive (so `"YES"`, `"Yes"` all work).

---

## Example Runs

**Case 1: User types `yes`**
```
Do you want to create 'sample.txt'? (yes/no): yes

Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

**Case 2: User types `no` (or file ends up empty/missing)**
```
Do you want to create 'sample.txt'? (yes/no): no

Error: The file 'sample.txt' was not found.
```

**Case 3: Invalid input**
```
Do you want to create 'sample.txt'? (yes/no): y
(Invalid input! please write 'yes/no' only)
```

---

## Customization

- Change the filename by replacing `"sample.txt"` everywhere.
- Modify the lines written inside the `with open('sample.txt', 'w') as file:` block.
- If you prefer an empty file **not** to be treated as “not found,” remove this part:
  ```python
  if reading_file.strip() == "":
      raise FileNotFoundError
  ```

---

## Learning Outcomes

- Taking user input safely
- Writing to files with `with open(..., 'w')`
- Reading files with `with open(..., 'r')`
- Raising and catching exceptions to guide program flow
- Producing clear, user-friendly error messages

---

_______________________________________________________________

# Task 2: Write and Append Data to a File

## Description
This project demonstrates **file handling in Python** by performing three key operations:
1. **Writing** user input into a file (`output.txt`).
2. **Appending** more user input to the same file without erasing the previous data.
3. **Reading** the final content of the file and displaying it back to the user.

This task is useful for beginners who want to learn how to manage files in Python and understand different file access modes (`w`, `a`, `r`).

---

## Features
- **Write Mode (`w`)**  
  - Creates a new file if it doesn’t exist.  
  - Overwrites the file if it already exists.  
- **Append Mode (`a`)**  
  - Opens an existing file and adds new content at the end.  
  - If the file doesn’t exist, it will create one.  
- **Read Mode (`r`)**  
  - Opens the file in read-only mode.  
  - Displays all the text stored in the file.  
---

## How to Run
1. Copy the code into a Python file (e.g., `file_write_append.py`).  
2. Run the program in your terminal or IDE:
   ```bash
   python file_write_append.py
   ```
3. Enter your text when prompted.  
4. Check the file `output.txt` in the same directory.  

---

## Example Run
```
Enter text to write to the file: Hello World
Data successfully written to output.txt.

Enter additional text to append: This is an appended line.
Data successfully appended.

Final content of output.txt:
Hello World
This is an appended line.
```

---

## Learning Points
- **File Handling Basics**  
  Python provides modes to control file operations:  
  - `'w'` → Write mode (creates/overwrites a file).  
  - `'a'` → Append mode (adds content to the end of file).  
  - `'r'` → Read mode (reads the file).  

- **Best Practices**  
  - Always close files using `file.close()` after operations to free up resources.  
  - Alternatively, use `with open(...) as file:` to handle files safely (auto-closes the file).  

---

## Possible Improvements
- Replace `open/close` with **`with` statement** for cleaner code.  
- Add **error handling** (e.g., `try-except`) to catch unexpected issues.  
- Allow multiple appends in a loop until the user chooses to stop.  

