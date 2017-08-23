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

'''
Inserts and image into the passed placeholder.  Checks the size of the
placeholder and uses fit_image to make sure the entire image will be
displayed.  Since PPTX changes the object after the image is inserted,
this will return that new object.
'''
def insert_image(self, placeholder, image):

    size = [
        int(Length(placeholder.width).pt),
        int(Length(placeholder.height).pt)
    ]

    img = fit_image(image, size)

    img_placeholder = placeholder.insert_picture(img)

    return img_placeholder
