import os

#gets the current directory which will be organized
path = os.getcwd()

#All of the folders to be created so that files can be organized in each
folder_categories = {"Music", "Videos", "Executables and Installers", "Documents", "Other", "Pictures"}

#Creates all of the folders for each category if they do not already exist
for folder in folder_categories:
    try:
        os.mkdir(folder)
    except OSError:
        if(os.path.exists(folder)):
            print("%s folder already exists, skipping creation" % folder)
        else:
            print("Creation of the %s directory has failed" % folder)
    else:
        print("%s directory successfully created" % folder)