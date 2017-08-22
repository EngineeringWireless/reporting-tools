'''
Functions that work with the WINd excel files to extract and name the images for
later use
'''



import glob, re, zipfile, tempfile, natsort
from shutil import copy2, rmtree
from os import path
from utils.image_order import imageOrderScanner

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
order the images appear in.  Currently Creates a copy of the image file in an
output folder and gives it the appropriate name.  The placement of the images
will need to be finalized later.
'''
def nameImages(images,imageOrder):

    counter = 0
    top_n = 1

    while counter < len(images):

        for name in imageOrder:
            copy2(
                images[counter],
                '../TEST_FILES/Output/Top {} {}.png'.format(top_n, name)
                )
            counter += 1

        top_n += 1

'''
Test Code Below Here, to be deleted later
'''
files = glob.glob('../TEST_FILES/*.xlsx')

temp_dir = createZip(files)
first_zip = glob.glob(temp_dir +'/*.zip')
temp_img = grabImages(temp_dir,path.basename(first_zip[0]))
print ('This is a {} file'.format(identifyReportType(path.basename(first_zip[0]))))

nameImages(temp_img, imageOrderScanner())


input('Press Enter to clear temp files')

rmtree(temp_dir)
