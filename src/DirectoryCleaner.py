import os
import sys
import time
import schedule


def DirectoryScanner(DirName):
    StartTime = time.time()
    TimeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Border = "-" * 52

   os.makedirs("logs", exist_ok=True)

   LogFileName = "logs/Automated-Directory-Cleaner_" + TimeStamp + ".log"
    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Automated Directory Cleaner\n")
    fobj.write("This is Directory Cleaner Script\n")
    fobj.write(Border + "\n")

    
    Ret = os.path.exists(DirName)

    if Ret == False:

        print("There is No such Directory")
        fobj.write("There is No such Directory\n")
        fobj.close()

        return

    
    Ret = os.path.isdir(DirName)

    if Ret == False:

        print("It is not directory")
        fobj.write("It is not directory\n")
        fobj.close()

        return

    
    FileCount = 0
    EmptyFileCount = 0
    DeletedFileCount = 0
    ErrorCount = 0

    
    for FolderName, SubFolder, FileName in os.walk(DirName):

        for fname in FileName:

            FileCount = FileCount + 1

            fname = os.path.join(FolderName, fname)

            try:

                
                if os.path.getsize(fname) == 0:

                    EmptyFileCount = EmptyFileCount + 1

                    
                    fobj.write("Deleted file: " + fname + "\n")

                    
                    os.remove(fname)

                    DeletedFileCount = DeletedFileCount + 1

            except OSError as e:

                ErrorCount = ErrorCount + 1

                print("Error while processing:", fname)
                print("Error:", e)

                fobj.write("Error processing file: " + fname + "\n")
                fobj.write("Error: " + str(e) + "\n")

            except Exception as e:

                ErrorCount = ErrorCount + 1

                print("Unexpected Error:", e)

                fobj.write("Unexpected Error processing file: " + fname + "\n")
                fobj.write("Error: " + str(e) + "\n")

    
    EndTime = time.time()

    ExecutionTime = EndTime - StartTime

    
    fobj.write("\n")
    fobj.write("========== Execution Summary ==========\n")
    fobj.write("Directory Scanned : " + DirName + "\n")
    fobj.write("Total Files       : " + str(FileCount) + "\n")
    fobj.write("Empty Files Found : " + str(EmptyFileCount) + "\n")
    fobj.write("Files Deleted     : " + str(DeletedFileCount) + "\n")
    fobj.write("Errors            : " + str(ErrorCount) + "\n")
    fobj.write("Execution Time    : " + str(round(ExecutionTime, 2)) + " seconds\n")
    fobj.write("Completed\n")
    fobj.write(Border + "\n")

    fobj.close()

    print("Total Files Scanned:", FileCount)
    print("Empty Files Found:", EmptyFileCount)
    print("Files Deleted:", DeletedFileCount)
    print("Errors:", ErrorCount)
    print("Execution Time:", round(ExecutionTime, 2), "seconds")
    print("Log File Created:", LogFileName)


def main():

    Border = "-" * 52

    print(Border)
    print("--------------- Automated Directory Cleaner ---------------")
    print(Border)

    if len(sys.argv) != 2:

        print("Invalid number of arguments")
        print("Please!! Specify the Name of Directory")

        return

    DirName = sys.argv[1]

    print("Directory to scan:", DirName)

    
    DirectoryScanner(DirName)

    
    schedule.every(1).minutes.do(DirectoryScanner, DirName)

    
    try:

        while True:

            schedule.run_pending()

            time.sleep(1)

    except KeyboardInterrupt:

        print("\nAutomated Directory Cleaner stopped by user.")


if __name__ == "__main__":
    main()

