from pydoc import doc
from .models import AclassModel, BclassModel, CclassModel, DclassModel
from django.db.models.signals import post_save
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from django.conf import settings
import qrcode
Image.MAX_IMAGE_PIXELS = 1000000000 
from datetime import date
today = date.today()


def save_profile(sender, instance, **kwargs):
    today =  instance.date.date()
    if instance.language == "o'zbekcha":
        theme = instance.article_name_uz
    elif instance.language == "ruscha":
        theme = instance.article_name_ru
    else:
        
        theme = instance.article_name_en
    if instance.certificate == "" or instance.greeting_card == "":
        fullname = instance.author1
        fullname2 = None
        if instance.author2:
            fullname = fullname + " " + instance.author2
        if instance.author3:
            fullname2 = instance.author3
            if instance.author4:
                fullname2 = fullname2 + " " + instance.author4
        certificate = writeToCertificate(fullname = fullname,
                        theme = theme,
                        link = instance.doi,
                        qrlink = instance.openair, fullname2=fullname2, date=today)
        instance.greeting_card = writetoDiplom(fullname=instance.author1,
                                                qrlink=instance.doi,
                                                tdate=today, theme=theme)
        instance.certificate = certificate
        instance.save()
         
    if instance.writer_document == "":
        fullname = instance.author1
        fullname2 = None
        if instance.author2:
            fullname = fullname + " " + instance.author2
        if instance.author3:
            fullname2 = instance.author3
            if instance.author4:
                fullname2 = fullname2 + " " + instance.author4
        instance.writer_document = writetoGuvohnoma(fullname=fullname, theme=theme,
                                     tdate = today, qrlink = instance.doi, num = instance.id, fullname2=fullname2)
        instance.save()
    
    if  instance.author2 and instance.greeting_card2 == "":
        instance.greeting_card2 = writetoDiplom(fullname=instance.author2,
                                                qrlink=instance.doi,
                                                tdate=today, theme=theme)
        instance.save()
    
    if  instance.author3 and instance.greeting_card3 == "":
        print(instance.author2)
        instance.greeting_card3 = writetoDiplom(fullname=instance.author3,
                                                qrlink=instance.doi,
                                                tdate=today, theme=theme)
        instance.save()

    if  instance.author4 and instance.greeting_card4 == "":
        print(instance.author2)
        instance.greeting_card4 = writetoDiplom(fullname=instance.author4,
                                                qrlink=instance.doi,
                                                tdate=today, theme=theme)
        instance.save()

    if instance.handbook == "":
        fullname = instance.author1
        fullname2 = None
        if instance.author2:
            fullname = fullname + " " + instance.author2
        if instance.author3:
            fullname2 = instance.author3
            if instance.author4:
                fullname2 = fullname2 + ", " + instance.author4
        instance.handbook = writeMalumotnoma(today = today, fullname=fullname, doilink=instance.doi,
                                            cyberleninkalink=instance.cyberleninka, openaccesslink=instance.openaccess,
                                            zenodolink = instance.zenodo, openairelink=instance.openair, 
                                            theme=theme, fullname2=fullname2, google=instance.google)
        instance.save()

post_save.connect(save_profile, sender=AclassModel)
post_save.connect(save_profile, sender=BclassModel)
post_save.connect(save_profile, sender=CclassModel)
post_save.connect(save_profile, sender=DclassModel)

def writeToCertificate(fullname, fullname2, link, qrlink, theme, date):
    try:
        img = Image.open('C://Users//faxri//Desktop//WORK//article//documents//certificate.jpg')
    except:
        # /home/user/djangoapps/article
        img = Image.open('/home//user//djangoapps//article//documents//certificate.jpg')
    image_width = img.width
    image_height = img.height  
    margin = 5  
    draw = ImageDraw.Draw(img)
    try:
        myFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanbold.ttf', 214)
        fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanbold.ttf', 268)
        linkFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR//timesnewromanbolditalic.ttf', 200)
    except:
        myFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 214)
        fullnameFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 268)
        linkFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbolditalic.ttf', 200)
 
    char_limit = 60
    theme = theme.upper()
    # text_width, _ = draw.textsize(fullname, font = myFont)
    draw.text(
                (
                    4200,6820
                ),
                str(date),
                fill =(0, 0, 0),
                font = myFont)
    draw.text(
                (
                    4300,
                    2400
                ),
                link,
                fill =(80,31,17),
                font = linkFont)

    if len(theme)>45:
        try:
            myFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR//timesnewromanbold.ttf', 208)
        except:
            myFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 208)
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
        return (y+100, line_heights)

    text_lines = wrap(theme, char_limit)

    y, line_heights = get_y_and_heights(
        text_lines,
        (image_width, image_height),
        margin,
        myFont
    )

    for i, line in enumerate(text_lines):
        line_width = myFont.getmask(line).getbbox()[2]
        x = ((image_width - line_width) // 2)
        draw.text((x+15, y+350), line, font=myFont, fill=(25,38,144))
        y += line_heights[i]

    if fullname2:
        fullname = fullname+" "+ fullname2

    text_lines = wrap(fullname, 38)
    y, line_heights = get_y_and_heights(
        text_lines,
        (image_width, image_height),
        margin,
        fullnameFont
    )

    for i, line in enumerate(text_lines):
        line_width = fullnameFont.getmask(line).getbbox()[2]
        x = ((image_width - line_width) // 2)
        draw.text((x+10, y-990), line, font=fullnameFont, fill=(25,38,144))
        # Move on to the height at which the next line should be drawn at
        y += line_heights[i]



    #qrcode
    qr = qrcode.QRCode(box_size=30)
    qr.add_data(qrlink)
    qr.make()
    img_qr = qr.make_image()

    pos = (img.size[0] - img_qr.size[0]-8500, img.size[1] - img_qr.size[1]-1350)

    img.paste(img_qr, pos)
    im_1 = img.convert('RGB')
    linkpath = f"/certificate/{fullname}.pdf"
    docpath = str(settings.MEDIA_ROOT)+linkpath
    im_1.save(docpath)
    return linkpath


def writetoDiplom(fullname, qrlink, tdate, theme):    

    try:
        myFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR//timesnewromanbold.ttf', 28)
        theFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR//timesnewromanbold.ttf', 64)
        img = Image.open('C://Users//faxri//Desktop//WORK//article//documents//diplom.jpg')
        draw = ImageDraw.Draw(img)
        fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR//timesnewromanbold.ttf', 80)
        numFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR//timesnewromanbold.ttf', 60)
    except:
        img = Image.open('/home//user//djangoapps//article//documents//diplom.jpg')
        draw = ImageDraw.Draw(img)
        fullnameFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 80)
        numFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 60)
        myFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 28)
        theFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 64)
    image_width = img.width
    image_height = img.height
    margin = 0
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
        return (y-350, line_heights)

    text_lines = wrap(theme, 55)

    y, line_heights = get_y_and_heights(
        text_lines,
        (image_width, image_height),
        margin,
        theFont
    )

    for i, line in enumerate(text_lines):
        # Calculate the horizontally-centered position at which to draw this line
        line_width = myFont.getmask(line).getbbox()[2]
        x = ((image_width - line_width) // 2 - 1050)
        draw.text((x, y), line, font=theFont, fill=(0, 0, 255))
        # Move on to the height at which the next line should be drawn at
        y += line_heights[i]
    
    draw.text(
                (
                    1650,1770
                ),
                str(tdate),
                fill =(0, 0, 0),
                font = numFont)


    draw.text(
                (
                700,1180 
                ),
                fullname,
                fill =(0,0,255),
                font = fullnameFont)
    qr = qrcode.QRCode(box_size=9)
    qr.add_data(qrlink)
    qr.make()
    img_qr = qr.make_image()

    pos = (img.size[0] - img_qr.size[0]-1000, img.size[1] - img_qr.size[1]-400)

    img.paste(img_qr, pos)
    im_1 = img.convert('RGB')
    try:
        linkpath = f"/diplom/{fullname}.pdf"
        docpath = str(settings.MEDIA_ROOT)+linkpath
        im_1.save(docpath)
    except:
        linkpath = f"\\diplom\\{fullname}.pdf"
        docpath = str(settings.MEDIA_ROOT)+linkpath
        im_1.save(docpath)
    return linkpath


def writetoGuvohnoma(qrlink, num, tdate, fullname, theme, fullname2):
    try:
        img = Image.open('/home//user//djangoapps//article//documents//guvohnoma.jpg')
        draw = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 100)
        fullnameFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 96)
        numFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanbold.ttf', 92)
    except:
        img = Image.open('C://Users//faxri//Desktop//WORK//article//documents//guvohnoma.jpg')
        draw = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanbold.ttf', 100)
        fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanbold.ttf', 96)
        numFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanbold.ttf', 92)
    image_width = img.width
    image_height = img.height
    num_y_position = 890
    text_width, _ = draw.textsize(fullname, font = myFont)
    margin = 10
    draw.text(
            (
                2350,
                num_y_position
            ),
            str(num),
            fill =(0, 0, 255),
            font = numFont)

    draw.text(
                (
                    2640,2300
                ),
                str(tdate),
                fill =(0, 0, 255),
                font = numFont)

    if fullname2 is not None:
        fullname = fullname + " " + fullname2
        

    
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

    text_lines = wrap(fullname, 35)

    y, line_heights = get_y_and_heights(
        text_lines,
        (image_width, image_height),
        -5,
        fullnameFont
    )
    
    if len(fullname) > 60:
        y += 100

    for i, line in enumerate(text_lines):
        line_width = fullnameFont.getmask(line).getbbox()[2]
        x = ((image_width - line_width) // 2)
        draw.text((x+960, y+620), line, font=fullnameFont, fill=(0, 0, 255))
        y += line_heights[i] 

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

    text_lines = wrap(theme, 60)

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
        draw.text((x, y), line, font=myFont, fill=(0, 0, 255))
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
    linkpath = f"/guvohnoma/{fullname}.pdf"
    docpath = str(settings.MEDIA_ROOT)+linkpath
    im_1.save(docpath)
    return linkpath


def writeMalumotnoma(fullname, doilink, openairelink, openaccesslink, cyberleninkalink, google, zenodolink, theme, fullname2, today):
    try:
        img = Image.open('/home//user//djangoapps//article//documents//malumotnoma.jpeg')
        linkFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanitalic.ttf', 70)
        themeFont = ImageFont.truetype('/home//user//djangoapps//article//TNR//timesnewromanitalic.ttf', 55)
    except:
        img = Image.open('C://Users//faxri//Desktop//WORK//article//documents//malumotnoma.jpeg')
        linkFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanitalic.ttf', 70)
        themeFont = ImageFont.truetype('C://Users//faxri//Desktop//WORK//article//TNR////timesnewromanitalic.ttf', 55)
    draw = ImageDraw.Draw(img)
    tdate = str(today)
    theme = theme.upper()

    sumtekst = ""
    ty = 1120
    themelist = theme.split()
    lt = len(themelist)
    i = 0
    for tekst in themelist:
        i+=1
        sumtekst =sumtekst + " " + tekst
        if len(sumtekst) > 56:
            draw.text(
                    (
                        950,ty
                    ),
                    sumtekst,
                    fill =(0, 0, 0),
                    font = themeFont)
            sumtekst = ""
            ty += 70
        elif i == lt:
            draw.text(
                    (
                        950,ty
                    ),
                    sumtekst,
                    fill =(0, 0, 0),
                    font = themeFont)

    draw.text(
                (
                    950,1310
                ),
                fullname,
                fill =(0, 0, 0),
                font = linkFont)

    if fullname2:
        draw.text(
                (
                    950,1380
                ),
                fullname2,
                fill =(0, 0, 0),
                font = linkFont)



    draw.text(
                (
                    950,1530
                ),
                tdate,
                fill =(0, 0, 0),
                font = linkFont)
    draw.text(
                (
                    950,1640
                ),
                doilink,
                fill =(256, 0, 0),
                font = linkFont)

    #links body begin

    qr = qrcode.QRCode(box_size=8)
    qr.add_data(doilink)
    qr.make()
    img_qr = qr.make_image()
    pos = (2900, 2180)
    img.paste(img_qr, pos)
    doilink2 = None
    if len(doilink)>60:
        doilink2 = doilink[60:]
        doilink = doilink[:60]

    draw.text(
                (
                    450,2280
                ),
                doilink,
                fill =(0, 0, 256),
                font = linkFont)
    
    if doilink2:
        draw.text(
                (
                    450,2360
                ),
                doilink2,
                fill =(0, 0, 256),
                font = linkFont)



    qr = qrcode.QRCode(box_size=7)
    qr.add_data(zenodolink)
    qr.make()
    img_qr = qr.make_image()

    pos = (2900, 2590)

    img.paste(img_qr, pos)

    zenodolink2 = None
    if len(zenodolink)>60:
        zenodolink2 = zenodolink[60:]
        zenodolink = zenodolink[:60]

    draw.text(
                (
                    450,2720
                ),
                zenodolink,
                fill =(0, 0, 256),
                font = linkFont)
    if zenodolink2:
        draw.text(
                (
                    450,2790
                ),
                zenodolink2,
                fill =(0, 0, 256),
                font = linkFont)


    qr = qrcode.QRCode(box_size=7)
    qr.add_data(openairelink)
    qr.make()
    img_qr = qr.make_image()
    pos = (2900, 2940)
    img.paste(img_qr, pos)

    openairelink2 = None
    if len(openairelink)>60:
        openairelink2 = openairelink[60:]
        openairelink = openairelink[:60]

    draw.text(
                (
                    450,3100
                ),
                openairelink,
                fill =(0, 0, 256),
                font = linkFont)

    if openairelink2:
        draw.text(
                (
                    450,3170
                ),
                openairelink2,
                fill =(0, 0, 256),
                font = linkFont)

    qr = qrcode.QRCode(box_size=8)
    qr.add_data(openaccesslink)
    qr.make()
    img_qr = qr.make_image()
    pos = (2900, 3250)
    img.paste(img_qr, pos)
    openaccesslink2 = None
    
    if len(openaccesslink)>60:
        openaccesslink2 = openaccesslink[60:]
        openaccesslink = openaccesslink[:60]
    
    draw.text(
                (
                    450,3390
                ),
                openaccesslink,
                fill =(0, 0, 256),
                font = linkFont)
    
    if openaccesslink2:
        draw.text(
                (
                    450,3460
                ),
                openaccesslink2,
                fill =(0, 0, 256),
                font = linkFont)

    cyberleninkalink = "http://olddrji.lbp.world/Publisher/ShowAllArticles.aspx?uname=2181-3906"
    qr = qrcode.QRCode(box_size=7)
    qr.add_data(cyberleninkalink)
    qr.make()
    img_qr = qr.make_image()
    pos = (2900, 3650)
    img.paste(img_qr, pos)
    
    cyberleninkalink2 = None
    if len(cyberleninkalink)>60:
        cyberleninkalink2 = cyberleninkalink[60:]
        cyberleninkalink = cyberleninkalink[:60]
    
    draw.text(
                (
                    450,3835
                ),
                cyberleninkalink,
                fill =(0, 0, 256),
                font = linkFont)
    
    if cyberleninkalink2:
        draw.text(
                (
                    450,3905
                ),
                cyberleninkalink2,
                fill =(0, 0, 256),
                font = linkFont)


    qr = qrcode.QRCode(box_size=8)
    qr.add_data(google)
    qr.make()
    img_qr = qr.make_image()
    pos = (2900, 4060)
    img.paste(img_qr, pos)

    google2 = None
    if len(google)>60:
        google2 = google[60:]
        google = google[:60]
    
    draw.text(
                (
                    450,4200
                ),
                google,
                fill =(0, 0, 256),
                font = linkFont)
    
    if google2:
        draw.text(
                (
                    450,4270
                ),
                google2,
                fill =(0, 0, 256),
                font = linkFont)
    
    img.paste(img_qr, pos)
    im_1 = img.convert('RGB')
    try:
        linkpath = f"/malumotnoma/{fullname}.pdf"
        docpath = str(settings.MEDIA_ROOT)+linkpath
        im_1.save(docpath)
    except:
        linkpath = f"\\malumotnoma\\{fullname}.pdf"
        docpath = str(settings.MEDIA_ROOT)+linkpath
        im_1.save(docpath)
    return linkpath
