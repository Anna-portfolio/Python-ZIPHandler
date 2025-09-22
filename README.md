# Python-ZIPHandler
Python script automating the processing of ZIP files and cleanup of extracted content across two directories

Two directory paths are defined and stored in the variables path01 and path02. The script searches for the first .zip file in path01 and extracts specific files to either directory based on their names. After extraction, the original .zip file is deleted.

For both directories, the script:
- Finds and extracts all .zip files.
- Deletes those .zip files after extraction.
- Removes all .xml files found in the directories.

Error Handling:
The script handles corrupted or unreadable .zip files by displaying an error message instead of crashing.
