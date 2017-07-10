import glob
from shutil import copy2, rmtree
from os import path
import zipfile
import tempfile
from image_order import ImageOrderScanner


#method for creating zip files from existing excel files and storing them in a temp directory
def createZip(files):

    #create the temp directory
    temp_dir = tempfile.mkdtemp()
    print (temp_dir)

    #make a copy of the renamed file in the temp directory
    for file in files:
        new_file_name = '{}\{}{}'.format(temp_dir, path.basename(file)[:-4], 'zip')
        copy2(file, new_file_name)
        print(new_file_name)

    #returning temp location for use elsewhere and eventual removal
    return temp_dir

#test lines
files = glob.glob('*.xlsx')

temp_dir = createZip(files)

input('Press Enter to clear temp files')

rmtree(temp_dir)
