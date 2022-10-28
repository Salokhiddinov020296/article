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
linkFont = ImageFont.truetype('C://Users//faxri//Desktop//article//Roboto//Roboto_Italic.ttf', 19)
fullname_y_position = 525
link_y_position = 450
char_limit = 35
tdate = "2022-10-28"
doilink = "https://doi.org/10.5281/zenodo.7239853"
fullname = "Arslonov Faxriyorjon"
theme = "ON THE MOTION OF THE MAXWELL PENDULUM"
text_width, _ = draw.textsize(fullname, font = myFont)
qrlink = "https://note.nkmk.me/en/python-pillow-qrcode/"

draw.text(
            (
                238,240
            ),
            theme,
            fill =(0, 0, 0),
            font = linkFont)

draw.text(
            (
                238,270
            ),
            fullname,
            fill =(0, 0, 0),
            font = linkFont)

draw.text(
            (
                238,300
            ),
            tdate,
            fill =(0, 0, 0),
            font = linkFont)


draw.text(
            (
                238,330
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