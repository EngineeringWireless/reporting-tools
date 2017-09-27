import file_manipulator as fm
from report_maker import Report
import glob
from os import path
from shutil import rmtree
import pandas as pd
from utils.image_order import imageOrderLTEScanner, imageOrderUMTSScanner


files = glob.glob('../TEST_FILES/*.xlsx')
images_df_final = pd.DataFrame()
temp_dir = fm.createZip(files)
first_zip = glob.glob(temp_dir +'/*.zip')
print(temp_dir)
for report_file in first_zip:

    temp_img = fm.grabImages(temp_dir,path.basename(report_file))
    r_type = fm.identifyReportType(path.basename(report_file))

    print('This is a {} file'.format(r_type))

    if r_type == 'LTE Scanner':
        result = fm.nameImages(temp_img, imageOrderLTEScanner())
    elif r_type == 'UMTS Scanner':
        result = fm.nameImages(temp_img, imageOrderUMTSScanner())
    images_df = pd.DataFrame(result, index = [path.basename(report_file)[:-4]])
    images_df_final = pd.concat([images_df_final, images_df])

images_df_final.to_excel('output.xlsx')

rp = Report()

for count in range(len(images_df_final.index)):

    r_type = fm.identifyReportType(images_df_final.index[count])

    if r_type == 'LTE Scanner':
        r_order = ['RSRP', 'CINR', 'PCI']
    elif r_type == 'UMTS Scanner':
        r_order = ['Ec', 'Ec_Io', 'PSC']

    for plot_type in r_order:

        slide = rp.add_image_slide()
        print (str(count) + plot_type)
        rp.add_image(images_df_final.iloc[count]['Top 1 ' + plot_type], slide['Picture Placeholder 3'])
        rp.add_image(images_df_final.iloc[count]['Top 1 '+ plot_type +' Legend'], slide['Picture Placeholder 4'])
        slide['Text Placeholder 2'].text = str(images_df_final.index[count])
        slide['Title 1'].text = plot_type

report_name = input('>>')
rp.save(report_name + '.pptx')

input('Press Enter to clear temp files')

rmtree(temp_dir)
