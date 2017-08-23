import file_manipulator as fm
from report_maker import Report
import glob
from os import path
from shutil import rmtree
from utils.image_order import imageOrderScanner


file = files = glob.glob('../TEST_FILES/*.xlsx')

temp_dir = fm.createZip(files)
first_zip = glob.glob(temp_dir +'/*.zip')
temp_img = fm.grabImages(temp_dir,path.basename(first_zip[0]))
print ('This is a {} file'.format(fm.identifyReportType(path.basename(first_zip[0]))))
print(temp_dir)
result = fm.nameImages(temp_img, imageOrderScanner())

rp = Report()

slide = rp.add_image_slide()

rp.insert_image(slide.placeholders[12], result['File Location']['Top 1 PCI'])
rp.insert_image(slide.placeholders[13], result['File Location']['Top 1 PCI Legend'])

rp.save('Output.pptx')

input('Press Enter to clear temp files')

rmtree(temp_dir)
