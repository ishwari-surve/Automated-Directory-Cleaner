
## Logs

The `logs/` directory stores timestamped log files automatically generated during each execution of the **Automated Directory Cleaner**.

Each log file records detailed information about the directory scanning and cleanup process, including:

- Directory scanned
- Total files scanned
- Empty files found
- Files deleted
- Errors encountered
- Execution time
- Deleted file paths
- Error details, if any

### Log File Naming

Log files are automatically created using the following format:

```text
Automated-Directory-Cleaner_YYYY-MM-DD_HH-MM-SS.log
````

Example:

```text
logs/
├── Automated-Directory-Cleaner_2026-09-09_18-02-57.log
├── Automated-Directory-Cleaner_2026-09-09_18-03-58.log
└── Automated-Directory-Cleaner_2026-09-09_18-04-58.log
```

A new log file is generated for every execution, including scheduled executions.

### Sample Log

```text
----------------------------------------------------
This is a log file created by Automated Directory Cleaner
This is Directory Cleaner Script
----------------------------------------------------
Deleted file: Data\file1.txt
Deleted file: Data\file2.txt

========== Execution Summary ==========
Directory Scanned : Data
Total Files       : 35
Empty Files Found : 21
Files Deleted     : 21
Errors            : 0
Execution Time    : 0.04 seconds
Completed
----------------------------------------------------
```

The log files provide a complete execution history, while the CMD displays only the application status and generated log file path.

```


