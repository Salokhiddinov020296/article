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
linkFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 16)
themeFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 16)
fullname_y_position = 525
link_y_position = 450
char_limit = 35
tdate = "2022-10-28"
doilink = "https://doi.org/10.5281/zenodo.7239853"
fullname = "Arslonov Faxriyorjon, Azizov Laziz"
fullname2 = "Axmadov Shaxmat, Raxmatov Ahmad"
theme = "THE MAXWELL PENDULUM ON THE MOTION OF THE MAXWELL PENDULUM"
text_width, _ = draw.textsize(fullname, font = myFont)
qrlink = "https://note.nkmk.me/en/python-pillow-qrcode/"

tekstlen = 0
sumtekst = ""
ty = 240
themelist = theme.split()
for tekst in themelist:
    tekstlen += len(tekst)
    if tekstlen < 30:
        sumtekst =sumtekst + " " + tekst
        themelist.remove(tekst)
        print(themelist, "themelist")
        print(tekst)
        print("1")
        if len(themelist) == 0:
            print("second if")
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
        ty += 30


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
                238,330
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

#qrcode
qr = qrcode.QRCode(box_size=3)
qr.add_data(qrlink)
qr.make()
img_qr = qr.make_image()

pos = (img.size[0] - img_qr.size[0], img.size[1] - img_qr.size[1])

img.paste(img_qr, pos)

img.show()
img.save(f"C://Users//faxri//Desktop//article//ready_certifacate//malumotnoma{fullname}{theme}.jpg")