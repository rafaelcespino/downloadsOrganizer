import os
import shutil

#gets the current directory which will be organized
path = os.getcwd()

#All of the folders to be created so that files can be organized in each
folder_categories = {"Music and Audio", "Videos", "Executables and Installers", "Documents", "Pictures", "Compressed Files", 'Others'}

#file extensions for each category
audio_extensions = {".mp3", ".wav", ".ogg", ".flac", ".wma", ".aac"}
video_extensions = {".mp4", ".mkv", ".mov", ".wav", ".avi", ".wmv", ".flv"}
executable_extensions = {".exe", ".dmg", ".pkg", ".msi", ".deb"}
picture_extensions = {".png", ".jpg", ".gif", ".tiff", ".psd", ".raw", ".HEIC"}
compressed_extensions = {".zip", ".7z", ".tar", ".rar"}
document_extensions = {".pdf", ".pptx", ".xlsx", ".doc", ".docx", ".xls", ".ppt", ".pptx"}

#Creates all of the folders for each category if they do not already exist
def createFolders():
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

#moves all files to their respective folder
def moveFiles():
    for file in os.listdir(path):
        for extension in audio_extensions:
            if(file.endswith(extension)):
                shutil.move(file, 'Music and Audio/%s' % file)

        for extension in video_extensions:
            if(file.endswith(extension)):
                shutil.move(file, 'Videos/%s' % file)

        for extension in executable_extensions:
            if(file.endswith(extension)):
                shutil.move(file, 'Executables and Installers/%s' % file)

        for extension in document_extensions:
            if(file.endswith(extension)):
                shutil.move(file, 'Documents/%s' % file)

        for extension in picture_extensions:
            if(file.endswith(extension)):
                shutil.move(file, 'Pictures/%s' % file)

        for extension in compressed_extensions:
            if(file.endswith(extension)):
                shutil.move(file, 'Compressed Files/%s' % file)

        #moves file to others folder if it is not the organizer python file nor a folder
        if(os.path.isfile(file) and file != 'organizer.py'):
            shutil.move(file, 'Others/%s' % file)

createFolders()
moveFiles()
