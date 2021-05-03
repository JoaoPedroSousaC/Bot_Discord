from urllib import request
from urllib.request import urlopen

import PIL
from PIL import Image, ImageFont, ImageDraw
import requests


fundo = Image.open("fundo.png")
mascara = Image.open("mascara.png").resize((130,130))
avatar = Image.open(requests.get("https://store-images.s-microsoft.com/image/apps.40057.13982743944721264.aba8e5da-4441-4232-a0e1-21747a781f2b.0c0baeb1-555e-4ef5-af93-ca8b1bd633d7", stream=True).raw)

avatar = avatar.resize(mascara.size)

mascara.paste(avatar,mask=mascara)
mascara.save("mascateteste.png")
font = ImageFont.truetype("font2.ttf",25)
draw = ImageDraw.Draw(fundo)
draw.text((160,208),'tesllklklkl lklte',(2000,2000,2000),font=font)


fundo.paste(mascara,(40,91),mask=mascara)
fundo.save("teste.png")