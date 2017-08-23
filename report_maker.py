from pptx import Presentation
from pptx.util import Length
from utils.prs_tools import get_layout
from utils.image_tools import fit_image


class Report():

    '''
    Creates a class containing a pptx presentation used to create the report.
    '''
    def __init__(self):

        self.prs = Presentation('tools/PPTX_TEMPLATE.pptx')

    '''
    Adds a "Plot with Legend" slide to the presentationa and returns that slide
    to be worked with.  Returns a dictionary with the slide object and all of
    that slides placeholder objects with their names as the key.
    '''
    def add_image_slide(self):

        img_layout = 'Plot with Legend'
        slide_info = {}

        self.cur_slide = self.prs.slides.add_slide(
                                get_layout(self.prs.slide_layouts, img_layout)
                                )


        for pl in self.cur_slide.placeholders:
            slide_info[pl.name] = pl

        slide_info['Slide'] = self.cur_slide

        return slide_info


    '''
    Saves presentation to given location.
    '''
    def save(self, file_name):
        self.prs.save(file_name)
