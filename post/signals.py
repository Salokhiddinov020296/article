from pydoc import doc
from .models import AclassModel
from django.db.models.signals import post_save
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from django.conf import settings
import qrcode

def writeToCertificate(fullname, link, qrlink, theme):
    img = Image.open('C://Users//faxri//Desktop//article//documents//certificate.jpg')
    image_width = img.width
    image_height = img.height  
    margin = 10
    draw = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 38)
    fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 34)
    linkFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_BoldItalic.ttf', 26)
    fullname_y_position = 525
    link_y_position = 450
    char_limit = 35
    theme = theme.upper()
    text_width, _ = draw.textsize(fullname, font = myFont)
    # qrlink = "https://note.nkmk.me/en/python-pillow-qrcode/"
    draw.text(
                (
                    (image_width - text_width) / 2 -100,
                    link_y_position
                ),
                link,
                fill =(255, 0, 0),
                font = linkFont)

    draw.text(
                (
                    (image_width - text_width) / 2+25,
                    fullname_y_position
                ),
                fullname,
                fill =(66, 102, 245),
                font = fullnameFont)

    if len(theme)>45:
        myFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 28)

    def get_y_and_heights(text_wrapped, dimensions, margin, font):
        """Get the first vertical coordinate at which to draw text and the height of each line of text"""
        ascent, descent = font.getmetrics()
        line_heights = [
            font.getmask(text_line).getbbox()[3] + descent + margin
            for text_line in text_wrapped
        ]
        line_heights[-1] -= margin

        # Total height needed
        height_text = sum(line_heights)

        # Calculate the Y coordinate at which to draw the first line of text
        y = (dimensions[1] - height_text) // 2

        # Return the first Y coordinate and a list with the height of each line
        return (y+125, line_heights)

    text_lines = wrap(theme, char_limit)

    y, line_heights = get_y_and_heights(
        text_lines,
        (image_width, image_height),
        margin,
        myFont
    )

    for i, line in enumerate(text_lines):
        # Calculate the horizontally-centered position at which to draw this line

        line_width = myFont.getmask(line).getbbox()[2]
        x = ((image_width - line_width) // 2)
        draw.text((x, y), line, font=myFont, fill=(66, 102, 245))
        # Move on to the height at which the next line should be drawn at
        y += line_heights[i]


    #qrcode
    qr = qrcode.QRCode(box_size=4)
    qr.add_data(qrlink)
    qr.make()
    img_qr = qr.make_image()

    pos = (img.size[0] - img_qr.size[0]-180, img.size[1] - img_qr.size[1]-180)

    img.paste(img_qr, pos)
    linkpath = f"\\certificate\\{fullname}.jpg"
    docpath = str(settings.MEDIA_ROOT)+linkpath
    print(docpath)
    img.save(docpath)
    return linkpath
    # img.save(f"C://Users//faxri//Desktop//article//ready_certifacate//certificate{fullname}{theme}.jpg")0

def save_profile(sender, instance, **kwargs):
    print(instance.certificate)
    if instance.certificate=="":
        certificate = writeToCertificate(fullname = instance.author1,
                        theme = instance.article_name_uz,
                        link = instance.doi,
                        qrlink = instance.openair)
        instance.certificate = certificate
        print(instance.certificate)
        instance.save()
        

post_save.connect(save_profile, sender=AclassModel)