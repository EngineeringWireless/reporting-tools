import file_manipulator as fm
from report_maker import Report
import glob
from os import path
from shutil import rmtree
import pandas as pd
from utils.image_order import imageOrderScanner


files = glob.glob('../TEST_FILES/*.xlsx')
images_df_final = pd.DataFrame()
temp_dir = fm.createZip(files)
first_zip = glob.glob(temp_dir +'/*.zip')
print(temp_dir)
for report_file in first_zip:

    temp_img = fm.grabImages(temp_dir,path.basename(report_file))
    print('This is a {} file'.format(fm.identifyReportType(path.basename(report_file))))
    result = fm.nameImages(temp_img, imageOrderScanner())

    images_df = pd.DataFrame(result, index = [path.basename(report_file)[:-4]])
    images_df_final = pd.concat([images_df_final, images_df])

images_df_final.to_excel('output.xlsx')

# rp = Report()
#
# slide = rp.add_image_slide()
#
# rp.insert_image(slide['Picture Placeholder 2'], result['File Location']['Top 1 PCI'])
# rp.insert_image(slide['Picture Placeholder 3'], result['File Location']['Top 1 PCI Legend'])
#
# rp.save('Output.pptx')

input('Press Enter to clear temp files')

rmtree(temp_dir)
