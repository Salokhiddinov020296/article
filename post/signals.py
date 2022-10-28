from pydoc import doc
from .models import AclassModel
from django.db.models.signals import post_save
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from django.conf import settings
import qrcode

from datetime import date
today = date.today()


def save_profile(sender, instance, **kwargs):
    if instance.certificate == ""  or instance.greeting_card == "":
        certificate = writeToCertificate(fullname = instance.author1,
                        theme = instance.article_name_eng,
                        link = instance.doi,
                        qrlink = instance.openair)
        instance.greeting_card = writetoDiplom(fullname=instance.author1,
                                                qrlink=instance.doi,
                                                tdate=today)
        instance.certificate = certificate
        fullname = instance.author1
        if instance.author2:
            fullname = " " + instance.author2
        elif instance.author3:
            fullname = " " + instance.author3
        elif instance.author4:
            fullname = " " + instance.author4
         
        handbook = writetoMalumotnoma(fullname=fullname, theme=instance.article_name_eng,
                                     tdate = today, qrlink = instance.doi, num = instance.id)
        instance.save()
    
    if  instance.author2 and instance.greeting_card2 == "":
        instance.greeting_card2 = writetoDiplom(fullname=instance.author2,
                                                qrlink=instance.doi,
                                                tdate=today)
        instance.save()
    
    if  instance.author3 and instance.greeting_card3 == "":
        print(instance.author2)
        instance.greeting_card3 = writetoDiplom(fullname=instance.author3,
                                                qrlink=instance.doi,
                                                tdate=today)
        instance.save()

    if  instance.author4 and instance.greeting_card4 == "":
        print(instance.author2)
        instance.greeting_card4 = writetoDiplom(fullname=instance.author4,
                                                qrlink=instance.doi,
                                                tdate=today)
        instance.save()
        

post_save.connect(save_profile, sender=AclassModel)

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
    im_1 = img.convert('RGB')
    linkpath = f"\\certificate\\{fullname}.jpg"
    docpath = str(settings.MEDIA_ROOT)+linkpath
    print(docpath)
    img.save(docpath)
    return linkpath


def writetoDiplom(fullname, qrlink, tdate):
    img = Image.open('C://Users//faxri//Desktop//article//documents//diplom.jpg')
    draw = ImageDraw.Draw(img)
    fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 80)
    numFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 60)

    draw.text(
                (
                    1650,1770
                ),
                str(tdate),
                fill =(0, 0, 0),
                font = numFont)


    draw.text(
                (
                930,1180 
                ),
                fullname,
                fill =(0,0,0),
                font = fullnameFont)
    qr = qrcode.QRCode(box_size=9)
    qr.add_data(qrlink)
    qr.make()
    img_qr = qr.make_image()

    pos = (img.size[0] - img_qr.size[0]-1000, img.size[1] - img_qr.size[1]-400)

    img.paste(img_qr, pos)
    im_1 = img.convert('RGB')
    linkpath = f"\\diplom\\{fullname}.pdf"
    docpath = str(settings.MEDIA_ROOT)+linkpath
    im_1.save(docpath)
    return linkpath


def writetoMalumotnoma(qrlink, num, tdate, fullname, theme):
    image_width = img.width
    image_height = img.height
    img = Image.open('C://Users//faxri//Desktop//article//documents//guvohnoma.jpg')
    draw = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 138)
    fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 96)
    numFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 92)
    num_y_position = 890
    char_limit = 35
    text_width, _ = draw.textsize(fullname, font = myFont)
    margin = 10
    draw.text(
            (
                (image_width - text_width) / 2+380,
                num_y_position
            ),
            num,
            fill =(0, 0, 0),
            font = numFont)

    draw.text(
                (
                    2600,2300
                ),
                tdate,
                fill =(0, 0, 0),
                font = numFont)


    draw.text(
                (
                2600,2420  
                ),
                fullname,
                fill =(0,0,0),
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
        return (y, line_heights)

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
        draw.text((x, y), line, font=myFont, fill=(0, 0, 0))
        # Move on to the height at which the next line should be drawn at
        y += line_heights[i]


    #qrcode
    qr = qrcode.QRCode(box_size=14)
    qr.add_data(qrlink)
    qr.make()
    img_qr = qr.make_image()

    pos = (img.size[0] - img_qr.size[0]-4100, img.size[1] - img_qr.size[1]-900)

    img.paste(img_qr, pos)
    im_1 = img.convert('RGB')
    linkpath = f"\\malumotnoma\\{fullname}.pdf"
    docpath = str(settings.MEDIA_ROOT)+linkpath
    im_1.save(docpath)
    return linkpath