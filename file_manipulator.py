'''
Functions that work with the WINd excel files to extract and name the images for later use
'''



import glob, re, zipfile, tempfile
from shutil import copy2, rmtree
from os import path
from image_order import imageOrderScanner

'''
method for creating zip files from existing excel files and storing them in a
temp directory
'''
def createZip(files):

    #create the temp directory
    temp_dir = tempfile.mkdtemp()


    #make a copy of the renamed file in the temp directory
    for file in files:
        new_file_name = '{}\{}{}'.format(
            temp_dir,
            path.basename(file)[:-4],
            'zip'
            )
        
        copy2(file, new_file_name)

    #returning temp location for use elsewhere and eventual removal
    return temp_dir


'''
Searches the WINd file name and returns the channel that was scanned. Checks for
common phrase in WINd files and returns either the channel number or that it is
a WiFi File
'''
def identifyChannel(filename):
    
    if 'CH' in filename:
        return re.search('(?<=CH)\w+',filename).group(0)
    elif 'WIFI' in filename:
        return 'WiFi'
    else:
        return None

'''
Test Code Below Here, to be deleted later
'''
files = glob.glob('*.xlsx')

temp_dir = createZip(files)

for file in files:
    print(identifyChannel(file))

input('Press Enter to clear temp files')

rmtree(temp_dir)
