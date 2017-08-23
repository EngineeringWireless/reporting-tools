'''
Functions that work with the WINd excel files to extract and name the images for
later use
'''



import glob, re, zipfile, tempfile, natsort
from shutil import copy2
from os import path
from utils.image_order import imageOrderScanner
import pandas as pd

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
Searches the WINd file name and returns the type of data that is being reported
in the file.  This can be used for identifying what order the images will be
appearing in the file.
'''
def identifyReportType(filename):
    if 'TopN' in filename:
        return 'Scanner'
    elif 'WIFI' in filename:
        return 'WiFi'
    if 'ue' in filename:
        return 'UE'

'''
Takes one of the zip files and extracts all of the images from it and places
them in the working temp folder.  Both the working temp folder and the zip
file are passed to the function.  Returns a sorted list of the location of each
image.
'''
def grabImages(path, zip_filename):
    embedded_image_path = '/xl/media'
    tmp_image_path = '{}/IMAGES/'.format(path)
    cur_file = '{}/{}'.format(path, zip_filename)

    #uses zipfile to extract only the
    with zipfile.ZipFile(cur_file) as z:
        for file in z.namelist():
            if '.png' in file:
                z.extract(file, tmp_image_path)

    images = glob.glob('{}{}/*.png'.format(tmp_image_path, embedded_image_path))
    images = natsort.natsorted(images)
    return images

'''
Takes an already ordered list of the images from one file and a list of the
order the images appear in.  creates a renamed file in the same temp folder and
returns a Dataframe containing which image it is and where it is.
'''
def nameImages(images,imageOrder):

    counter = 0
    top_n = 1

    image_df = pd.DataFrame(columns = ['File Location'])

    while counter < len(images):

        for name in imageOrder:

            name = 'Top {} {}'.format(top_n, name)
            file_path = path.dirname(images[counter])
            filename = '{}\\{}.png'.format(file_path, name)

            copy2(images[counter], filename)

            image_df.loc[name] = filename

            counter += 1

        top_n += 1

    return image_df
