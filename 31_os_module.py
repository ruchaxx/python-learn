import os
import shutil
import send2trash

print("pwd is ",os.getcwd())
print("list dir ",os.listdir())

#shutil.move('filename','destination')   # mv cmd

#os.unlink('file path') # delete single file
#os.rmdir('folder path') # delete folder (folder empty hovu joia)

#shutil.rmtree('path') #delete all file and folder from path

#send2trash.send2trash('file path') #trash ma move kare

for folder,subfolder,file in os.walk(os.getcwd()):
    print("\nfolder ",folder)
    print("\nsubfolder ",subfolder)
    print("\nfile ",file)