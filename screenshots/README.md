
## Screenshots

### Initial Execution

The application starts by accepting the directory path and creating the first timestamped log file. The CMD displays the application status while detailed execution information is stored in the log file.

### Scheduled Execution

The application automatically runs every 1 minute using the Python `schedule` module. Each scheduled execution creates a new timestamped log file.

### Program Shutdown

The application can be safely stopped using `Ctrl+C`. The program handles `KeyboardInterrupt` and exits cleanly.




