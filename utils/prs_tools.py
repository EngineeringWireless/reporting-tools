'''
method for finding a specific layout from the powerpoint template.  Accepts
all the layouts and the known name of the slide needed.
'''
def get_layout(layouts, layout_name):

    for layout in layouts:
        if layout.name == layout_name:
            return layout
        else:
            return None
