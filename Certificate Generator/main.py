from PIL import Image, ImageDraw, ImageFont
import sys
import datetime
import os

print(sys.argv)

name = sys.argv[1]
task = sys.argv[2]

today = datetime.date.today()

img = Image.open("./certificate.jpg")

font_name = "Comic Sans MS.ttf" if os.name == "posix" else "comic.ttf"

print(img.size)

surface = ImageDraw.Draw(img)

font = ImageFont.truetype(font_name, img.size[1]//len(name))
surface.text((img.size[0]//2, 300), name, font=font, fill=(0, 0, 255), anchor="mm")

font = ImageFont.truetype(font_name, img.size[1]//len(task))
surface.text((img.size[0]//2, 450), task, font=font, fill=(0, 0, 255), anchor="mm")

print(today.day, today.month, today.year)
font = ImageFont.truetype(font_name, 30)
surface.text((480, 550), str(today.day), font=font, fill=(0, 0, 255), anchor="lm")
surface.text((600, 550), today.strftime("%B"), font=font, fill=(0, 0, 255), anchor="lm")
surface.text((600, 620), str(today.year), font=font, fill=(0, 0, 255), anchor="lm")

img.show()
img.save("./certificate.png")