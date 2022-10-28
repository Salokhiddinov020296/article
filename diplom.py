from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from django.conf import settings
import qrcode


img = Image.open('C://Users//faxri//Desktop//article//documents//diplom.jpg')
image_width = img.width
image_height = img.height  
margin = 10
draw = ImageDraw.Draw(img)
myFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 138)
fullnameFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 80)
numFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 60)
fullname_y_position = 525
num_y_position = 890
char_limit = 35
tdate = "2022-10-28"
num = "2022-10-28125"
fullname = "Arslonov Faxriyorjon"
theme = "ON THE MOTION OF THE MAXWELL PENDULUM"
text_width, _ = draw.textsize(fullname, font = myFont)
qrlink = "https://note.nkmk.me/en/python-pillow-qrcode/"

draw.text(
            (
                1650,1770
            ),
            tdate,
            fill =(0, 0, 0),
            font = numFont)


draw.text(
            (
              930,1180 
            ),
            fullname,
            fill =(0,0,0),
            font = fullnameFont)

if len(theme)>45:
    myFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Bold.ttf', 28)


#qrcode
qr = qrcode.QRCode(box_size=9)
qr.add_data(qrlink)
qr.make()
img_qr = qr.make_image()

pos = (img.size[0] - img_qr.size[0]-1000, img.size[1] - img_qr.size[1]-400)

img.paste(img_qr, pos)
img.show()
img.save(f"C://Users//faxri//Desktop//article//ready_certifacate//guvohnoma{fullname}{theme}.jpg")