# ---------------------------------------------------------*\
# Title: Metadata-Reader (for Fotos)
# Author: TM (05-2021)
# ---------------------------------------------------------*/
#!/usr/bin/env python3

import os
from PIL import Image
from PIL.ExifTags import TAGS

dirname = os.path.dirname(__file__)
image_file = os.path.join(dirname, 'Sample.jpg')

try:
    image = Image.open(image_file)

    exif = {}       # Dictionary to store metadata keys and value pairs.

    for tag, value in image._getexif().items():     # Iterating over the dictionary
        if tag in TAGS:                             # Extracting all the metadata as key and value pairs
            # Converting them from numerical value to string values
            exif[TAGS[tag]] = value

    print("Displaying all the metadatas of the image: \n")

    # Iterating over all EXIF data fields
    for tag_id in exif:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exif.get(tag_id)
        print(f"{tag:25}: {data}")

except IOError:
    print("Image couldn't be opened")

# -------------------------Notes-----------------------------------------------*\
#
# -----------------------------------------------------------------------------*\
