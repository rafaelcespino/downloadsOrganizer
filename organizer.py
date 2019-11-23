import os
import shutil

#prompts the user to enter the directory to be organized
try:
    pathString = input("Please enter the directory that you would like to organize\n")
    path = os.path.normpath(pathString)
    os.chdir(path)
except FileNotFoundError:
    print("Error: That directory does not exist")

#file extensions for each category
audio_extensions = {".mp3", ".wav", ".ogg", ".flac", ".wma", ".aac"}
video_extensions = {".mp4", ".mkv", ".mov", ".wav", ".avi", ".wmv", ".flv"}
executable_extensions = {".exe", ".dmg", ".pkg", ".msi", ".deb"}
picture_extensions = {".png", ".JPG", ".gif", ".tiff", ".psd", ".raw", ".HEIC"}
compressed_extensions = {".zip", ".7z", ".tar", ".rar"}
document_extensions = {".pdf", ".pptx", ".xlsx", ".doc", ".docx", ".xls", ".ppt", ".pptx"}


#moves all files to their respective folder
def moveFiles():
    audioCreated = False
    videoCreated = False
    executableCreated = False
    pictureCreated = False
    compressedCreated = False
    documentCreated = False
    otherCreated = False

    #Creates each folder if not yet created then moves each file into its respective folder
    for file in os.listdir(path):
        for extension in audio_extensions:
            if(file.endswith(extension)):
                if(not audioCreated):
                    os.mkdir("Music and Audio")
                    audioCreated = True
                shutil.move(file, 'Music and Audio/%s' % file)

        for extension in video_extensions:
            if(file.endswith(extension)):
                if(not videoCreated):
                    os.mkdir("Videos")
                    videoCreated = True
                shutil.move(file, 'Videos/%s' % file)

        for extension in executable_extensions:
            if(file.endswith(extension)):
                if(not executableCreated):
                    os.mkdir("Executables and Installers")
                    executableCreated = True
                shutil.move(file, 'Executables and Installers/%s' % file)

        for extension in document_extensions:
            if(file.endswith(extension)):
                if(not documentCreated):
                    os.mkdir("Documents")
                    documentCreated = True
                shutil.move(file, 'Documents/%s' % file)

        for extension in picture_extensions:
            if(file.endswith(extension)):
                if(not pictureCreated):
                    os.mkdir("Pictures")
                    pictureCreated = True
                shutil.move(file, 'Pictures/%s' % file)

        for extension in compressed_extensions:
            if(file.endswith(extension)):
                if(not compressedCreated):
                    os.mkdir("Compressed Files")
                    compressedCreated = True
                shutil.move(file, 'Compressed Files/%s' % file)

        #moves file to others folder if it is not the organizer python file nor a folder
        if(os.path.isfile(file) and file != 'organizer.py'):
            if(not otherCreated):
                os.mkdir("Others")
                otherCreated = True
            shutil.move(file, 'Others/%s' % file)


moveFiles()

