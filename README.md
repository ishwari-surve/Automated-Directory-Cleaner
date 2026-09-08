# Automated Directory Cleaner

A Python-based file management and automation tool that recursively scans a specified directory, identifies and removes empty files, and generates timestamped execution logs with cleanup statistics and error details.

## 📌 Overview

**Automated Directory Cleaner** automates routine directory-cleanup tasks using Python.

The application accepts a directory path through the command line, scans the directory and its subdirectories, identifies files with zero bytes, and automatically removes them.

Every execution generates a timestamped log containing deleted file paths, errors encountered during processing, execution statistics, and total execution time.

The application also supports scheduled execution using the Python `schedule` library, allowing the cleanup process to run automatically at a fixed interval.

## 🚀 Features

* 🔍 **Recursive Directory Scanning**

  * Scans the specified directory and all its subdirectories using `os.walk()`.

* 🧹 **Empty File Detection**

  * Identifies files with a size of 0 bytes.

* 🗑️ **Automatic File Deletion**

  * Removes detected empty files automatically.

* 📝 **Deleted File Logging**

  * Records the complete path of every successfully deleted file.

* ⏱️ **Timestamped Logs**

  * Creates a unique log file for each execution.
  * Example:

    ```text
    CleanOps_2026-09-08_20-12-15.log
    ```

* ⚠️ **Exception Handling**

  * Handles file-system errors without terminating the complete scanning process.
  * Records errors in the execution log.

* 📊 **Execution Statistics**

  * Provides:

    * Total files scanned
    * Empty files found
    * Files deleted
    * Errors encountered
    * Execution time

* 📁 **Automatic Log Directory Creation**

  * Creates the `logs` directory automatically if it does not exist.

* 🔄 **Scheduled Execution**

  * Uses the Python `schedule` library to execute the directory-cleaning process automatically every 1 minute.

* 🛑 **Graceful Shutdown**

  * Supports `Ctrl + C` to safely stop the continuously running application.

## 🛠️ Technologies Used

| Technology             | Purpose                                                 |
| ---------------------- | ------------------------------------------------------- |
| **Python**             | Core programming language                               |
| **os**                 | Directory traversal, file detection and file operations |
| **sys**                | Command-line argument handling                          |
| **time**               | Timestamp generation and execution-time measurement     |
| **schedule**           | Scheduled task execution                                |
| **Exception Handling** | File-system error management                            |

## 📂 Project Structure

```text
Automated-Directory-Cleaner/
│
├── main.py
├── logs/
│   └── CleanOps_YYYY-MM-DD_HH-MM-SS.log
├── .gitignore
├── LICENSE
└── README.md
```

> Log files are generated automatically inside the `logs` directory when the application runs.

## ⚙️ Requirements

* Python 3.x
* `schedule` Python package

Install the required dependency:

```bash
pip install schedule
```

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/<your-username>/Automated-Directory-Cleaner.git
```

### Navigate to the Project

```bash
cd Automated-Directory-Cleaner
```

### Run the Application

Provide the directory you want to scan:

```bash
python main.py Data
```

Replace `Data` with the directory you want to clean.

## 💻 Example Execution

```text
----------------------------------------------------
---------------CleanOps------------------------------
----------------------------------------------------
Directory to scan: Data

Total Files Scanned: 7
Empty Files Found: 3
Files Deleted: 3
Errors: 0
Execution Time: 0.0 seconds
Log File created: logs/CleanOps_2026-09-08_20-12-15.log
```

The application continues running and automatically performs the cleanup process every 1 minute.

Press:

```text
Ctrl + C
```

to stop the application gracefully.

## 📝 Sample Log

A generated log file contains information similar to:

```text
----------------------------------------------------
This is a log file created by CleanOps
This is Directory Cleaner Script
----------------------------------------------------
Deleted file: Data\file4.txt
Deleted file: Data\file5.txt
Deleted file: Data\file6.txt

========== Execution Summary ==========
Directory Scanned : Data
Total Files       : 7
Empty Files Found : 3
Files Deleted     : 3
Errors            : 0
Execution Time    : 0.0 seconds
Completed
----------------------------------------------------
```

## 🔐 Exception Handling

The application uses exception handling to prevent individual file-system errors from terminating the entire scanning process.

### OSError

Handles operating-system-level errors that may occur while accessing, checking, or deleting files.

Example:

```text
Error while processing: Data\protected.txt
Error: [Errno ...] ...
```

The error is recorded in the log, and the application continues processing the remaining files.

### General Exception Handling

Unexpected errors are also captured and logged to improve application reliability.

## 📊 Execution Summary

Every execution records important performance and cleanup metrics:

```text
========== Execution Summary ==========
Directory Scanned : Data
Total Files       : 7
Empty Files Found : 3
Files Deleted     : 3
Errors            : 0
Execution Time    : 0.0 seconds
Completed
```

These metrics provide a quick overview of the directory-cleaning operation and application performance.

## 🔄 Automation Workflow

```text
                Start
                  │
                  ▼
        Receive Directory Path
                  │
                  ▼
         Validate Directory
                  │
                  ▼
      Scan Directory Recursively
                  │
                  ▼
          Check Each File
                  │
            ┌─────┴─────┐
            │           │
         Empty       Non-Empty
            │           │
            ▼           ▼
         Delete        Skip
            │
            ▼
      Log Deleted File
            │
            ▼
     Handle File Errors
            │
            ▼
   Generate Execution Summary
            │
            ▼
    Create Timestamped Log
            │
            ▼
      Scheduled Re-execution
```

## 🎯 Project Objectives

This project demonstrates practical implementation of:

* Python automation
* File-system programming
* Recursive directory traversal
* File handling and management
* Command-line argument processing
* Scheduled task execution
* Exception handling
* Logging
* Execution-time measurement
* Automation workflow design

## 🔮 Future Enhancements

* Configurable scheduling intervals
* File-age based cleanup
* File-size based cleanup rules
* Configurable cleanup policies
* JSON-based configuration
* Improved command-line interface
* Email notifications
* Desktop/system notifications
* Unit testing
* Detailed logging levels
* Directory health monitoring dashboard

## 📈 Skills Demonstrated

**Programming:** Python

**Core Concepts:** Functions · Loops · Conditional Statements · Exception Handling · Command-Line Arguments

**Automation:** Scheduled Execution · Automated File Cleanup · Directory Monitoring

**File-System Operations:** Directory Traversal · File Detection · File Metadata · File Deletion

**Logging & Monitoring:** Timestamped Logs · Error Logging · Execution Metrics · Execution Summary

## 👩‍💻 Author

**Ishwari Surve**

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.
