# import necessary modules
import os
import csv

# open the csv file, example is dirlist (directory structure list)
with open('dirlist.csv', newline='') as csvfile:
    # read the file
    readCSV = csv.reader(csvfile)
    # tell the reader which row is the header
    header = next(readCSV)
    # loop through an acceptable range for how many top level items will be in your directory list
    for i in range(1,450):
        # list all the column headings you want to pull data from
        for parent, sub1, sub2, sub3, sub4 in readCSV:
            # create an array that contains your un-nested subdirectories
            subdirectories = [sub1, sub2, sub3, sub4]
            # loop through your subdirectory array
            for subdirectory in subdirectories:
                # create the parent directory name, create a subdirectory for every item in the subdirectory array
                os.makedirs(os.path.join(parent, subdirectory))

# To create directory list, open terminal. cd ~ yourProject  (where this file is located with your directory csv file).
# run: python3 createParentDirectoriesWithSubdirectories.py
# Your directories should be created in the folder that contains the createParentDirectories file.
