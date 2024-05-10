from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import qrcode
img = Image.open('C://Users//faxri//Desktop//article//documents//malumotnoma.jpg')
image_width = img.width
image_height = img.height  
margin = 10
draw = ImageDraw.Draw(img)
myFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 24)
fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 24)
linkFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 18)
themeFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 16)
fullname_y_position = 525
link_y_position = 450
char_limit = 35
tdate = "2022-10-28"
doilink = "https://doi.org/10.5281/zenodo.7239853"
fullname = "Arslonov Faxriyorjon, Azizov Laziz"
fullname2 = "Axmadov Shaxmat, Raxmatov Ahmad"
theme = "THE MAXWELL PENDULUM ON THE MOTION OF THE MAXWELL PENDULUM MEN KECHA KORDIM SENI QAYERDA EDING"
text_width, _ = draw.textsize(fullname, font = myFont)

tekstlen = 0
sumtekst = ""
ty = 240
themelist = theme.split()
lt = len(themelist)
i = 0
for tekst in themelist:
    i+=1
    tekstlen += len(tekst)
    if tekstlen < 30:
        sumtekst =sumtekst + " " + tekst
        if i == lt:
            draw.text(
                (
                    238,ty
                ),
                sumtekst,
                fill =(0, 0, 0),
                font = themeFont)
    else:
        draw.text(
                (
                    238,ty
                ),
                sumtekst,
                fill =(0, 0, 0),
                font = themeFont)
        
        tekstlen = 0
        sumtekst = ""
        ty += 20


draw.text(
            (
                238,300
            ),
            fullname,
            fill =(0, 0, 0),
            font = linkFont)

if fullname2:
    draw.text(
            (
                238,325
            ),
            fullname2,
            fill =(0, 0, 0),
            font = linkFont)



draw.text(
            (
                238,368
            ),
            tdate,
            fill =(0, 0, 0),
            font = linkFont)


draw.text(
            (
                238,398
            ),
            doilink,
            fill =(256, 0, 0),
            font = linkFont)


draw.text(
            (
                120,550
            ),
            doilink,
            fill =(0, 0, 256),
            font = linkFont)

qr = qrcode.QRCode(box_size=2)
qr.add_data(doilink)
qr.make()
img_qr = qr.make_image()

pos = (653, 505)

img.paste(img_qr, pos)


zenodolink = "https://phoenixnap.com/kb/how-to-change-root-password-linux"
draw.text(
            (
                120,640
            ),
            zenodolink,
            fill =(0, 0, 256),
            font = linkFont)

qr = qrcode.QRCode(box_size=2)
qr.add_data(zenodolink)
qr.make()
img_qr = qr.make_image()

pos = (653, 590)

img.paste(img_qr, pos)


openairelink = "https://phoenixnap.com/kb/how-to-change-root-password-linux"
draw.text(
            (
                120,725
            ),
            openairelink,
            fill =(0, 0, 256),
            font = linkFont)


qr = qrcode.QRCode(box_size=2)
qr.add_data(openairelink)
qr.make()
img_qr = qr.make_image()
pos = (653, 685)
img.paste(img_qr, pos)

openaccesslink = "https://phoenixnap.com/kb/how-to-change-root-password-linux"
draw.text(
            (
                120,817
            ),
            openaccesslink,
            fill =(0, 0, 256),
            font = linkFont)

qr = qrcode.QRCode(box_size=2)
qr.add_data(openaccesslink)
qr.make()
img_qr = qr.make_image()
pos = (653, 773)
img.paste(img_qr, pos)


cyberleninkalink = "https://phoenixnap.com/kb/how-to-change-root-password-linux"
draw.text(
            (
                120,902
            ),
            cyberleninkalink,
            fill =(0, 0, 256),
            font = linkFont)

qr = qrcode.QRCode(box_size=2)
qr.add_data(cyberleninkalink)
qr.make()
img_qr = qr.make_image()
pos = (653, 858)
img.paste(img_qr, pos)

google = "https://phoenixnap.com/kb/how-to-change-root-password-linux"
draw.text(
            (
                120,990
            ),
            google,
            fill =(0, 0, 256),
            font = linkFont)

qr = qrcode.QRCode(box_size=2)
qr.add_data(google)
qr.make()
img_qr = qr.make_image()
pos = (653, 945)
img.paste(img_qr, pos)

img.show()
img.save(f"C://Users//faxri//Desktop//article//ready_certifacate//malumotnoma{fullname}{theme}.jpg")