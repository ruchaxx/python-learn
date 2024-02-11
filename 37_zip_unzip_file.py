import zipfile

with open("fileone.txt",mode='w') as f:
    f.write("file one")

with open("filetwo.txt",mode='w') as f:
    f.write("file two")


# Zip file
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("fileone.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filetwo.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

#Unzip file
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')

###############################################################################

import shutil

#Zip whole folder

dir_to_zip = 'extracted_content'
output_file = 'shutil-example'

shutil.make_archive(output_file,'zip',dir_to_zip)

#Unzip whole folder
shutil.unpack_archive('shutil-example.zip','shutil-unzip','zip')