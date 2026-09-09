# Source Code

This directory contains the core Python implementation of the **Automated Directory Cleaner** system.

## DirectoryCleaner.py

`DirectoryCleaner.py` is the main application responsible for scanning a specified directory, identifying empty files, removing them automatically, and generating detailed execution logs.

### Responsibilities

- Validate the provided directory path
- Recursively scan directories and subdirectories
- Identify empty files
- Remove empty files automatically
- Track total files scanned
- Track empty files found
- Track successfully deleted files
- Handle file-system related exceptions
- Generate timestamped log files
- Record deleted file paths and processing errors
- Generate an execution summary
- Calculate total execution time
- Continuously execute the cleanup process using scheduled execution

## Core Modules

| **Module** | **Purpose** |
|------------|-------------|
| `os` | Directory traversal, path validation, file-size checking, and file deletion |
| `sys` | Command-line argument handling |
| `time` | Timestamp generation and execution-time measurement |
| `schedule` | Periodic execution of the directory-cleaning task |

## Execution Flow

```text
Command-Line Argument
        ↓
Directory Validation
        ↓
Recursive Directory Scan
        ↓
File Detection
        ↓
Empty File Identification
        ↓
File Deletion
        ↓
Exception Handling
        ↓
Execution Summary
        ↓
Timestamped Log Generation
        ↓
Scheduled Re-execution

```

````text
## Key Implementation Concepts

### 1. Command-Line Argument Processing

The application accepts the directory path through a command-line argument.

```python
DirName = sys.argv[1]
````

This allows different directories to be processed without modifying the source code.

### 2. Directory Validation

The application verifies whether the provided path exists and whether it is a directory.

```python
os.path.exists(DirName)
```

```python
os.path.isdir(DirName)
```

### 3. Recursive Directory Traversal

The application uses `os.walk()` to recursively scan the target directory and its subdirectories.

```python
for FolderName, SubFolder, FileName in os.walk(DirName):
```

### 4. Empty File Detection

A file is considered empty when its size is `0` bytes.

```python
if os.path.getsize(fname) == 0:
```

### 5. Automated File Deletion

Detected empty files are removed using `os.remove()`.

```python
os.remove(fname)
```

The deleted-file counter is increased only after successful deletion.

### 6. Exception Handling

File operations are protected using exception handling so that an error with one file does not terminate the complete scanning process.

The application handles:

* `OSError`
* General `Exception`

Example:

```python
try:
    if os.path.getsize(fname) == 0:
        os.remove(fname)

except OSError as e:
    ErrorCount = ErrorCount + 1

except Exception as e:
    ErrorCount = ErrorCount + 1
```

Errors are also recorded in the execution log.

### 7. Execution Metrics

The application maintains the following execution statistics:

* Total files scanned
* Empty files found
* Files successfully deleted
* Errors encountered
* Total execution time

Execution time is calculated using:

```python
StartTime = time.time()

# Directory scanning and cleanup

EndTime = time.time()

ExecutionTime = EndTime - StartTime
```

### 8. Timestamped Logging

A timestamp is generated for every execution.

```python
TimeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
```

The application automatically creates the `logs` directory and generates a timestamped log file.

Example:

```text
logs/Automated-Directory-Cleaner_2026-09-09_11-30-45.log
```

The log records:

* Deleted file paths
* Processing errors
* Directory scanned
* Total files scanned
* Empty files found
* Files deleted
* Errors encountered
* Execution time
* Completion status

## Scheduled Execution

The application uses the `schedule` library to execute the directory-cleaning process every 1 minute.

```python
schedule.every(1).minutes.do(DirectoryScanner, DirName)
```

The application continuously checks for scheduled tasks using:

```python
while True:
    schedule.run_pending()
    time.sleep(1)
```

The process continues running until manually stopped.

Press:

```text
Ctrl + C
```

to stop the application gracefully.

## Command-Line Usage

Run the application by providing the directory path as a command-line argument:

```bash
python src/main.py <directory_path>
```

Example:

```bash
python src/main.py Data
```

The specified directory and its subdirectories will be scanned for empty files.

## Source Code Design

The implementation demonstrates practical application of:

* Python File-System Automation
* Recursive Directory Traversal
* Command-Line Argument Processing
* File Detection and Deletion
* Exception Handling
* Timestamped Logging
* Execution-Time Measurement
* Scheduled Task Automation
* File Management
* Python Standard Library

```
```

## Author
**Ishwari Surve**
