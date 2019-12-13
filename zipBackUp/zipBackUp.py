#created by Mark Foos, based on Automate the Boring Stuff in Python
#Chapter 9, added functionality of asking for zip file name and creating new backup folder

# Copies folder contents and backs it up to a zip file


import zipfile, os, shutil, pathlib

# test print statement
print("starting program")

path = os.getcwd()

#test print statement for working directory
print("The current working directory: %s" % path)

# main funciton
#creates a new backup folder, moves newly created zip files into folder

def backUpToZip(folder):
    #backs up the entire contents t a ZIP file.



    newFolderName = ("\\" + "zipBackUpFolder")
    backUpFolderVerification = input("have you created a backup folder? (y or n)\n\n")

#conditional for error handling of new backup folder creation
    if backUpFolderVerification == 'n':
        try:
            folder = str(os.mkdir(path + newFolderName))
            print(folder)
        except:
            print("backupfolder was previously made")
            folder = path + newFolderName
            print(folder)
    number = 1
# input for zip file name, can't use '_' in naming
    zipFileNameInput = input("Enter your fileName: \n\n")
    while True:
        zipFileName = zipFileNameInput + '_' + str(number) + '.zip'
        p = pathlib.Path(folder + "\\" + zipFileName)

# conditional for previously named zip file to incremented if found
# in back up folder
        if not p.is_file():
            print("this file does not have a previous backup")
            print(folder)
            break
        number = number + 1

# actually creating zip files
    print('Creating %s...' % (zipFileName))
    backUpZip = zipfile.ZipFile(zipFileName, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))

        backUpZip.write(foldername)

        for filename in filenames:

            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backUpZip.write(os.path.join(foldername, filename))

    backUpZip.close()
    print("Done.")

# moves zip file to back up directory
    newFileDirectory = (os.getcwd() + "\\" + zipFileName)
    newFileDirectory2 = os.path.abspath(newFileDirectory)
    print(newFileDirectory2)

    shutil.move(str(newFileDirectory2), (path + '\\zipBackUpFolder'))

# path of file to be zipped, call zip function
backUpToZip(path + "\\zipTest")
