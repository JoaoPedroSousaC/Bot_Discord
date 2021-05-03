import discord
from discord.ext import commands
import requests

import filecmp
from importlib.metadata import files
from urllib import request
from urllib.request import urlopen

import PIL
from PIL import Image, ImageFont, ImageDraw

intents = discord.Intents.default()
intents.members = True
Token = "ODM4NTI3MTY1NjQwNjA1NzA2.YI8ZRw.o3PJnr6LFxboOHp_K2gcS0jJ0F8"
client = commands.Bot(command_prefix= "!", case_insensitive= True, intents=intents)

@client.event
async def on_ready():
    print('Funcinando como {0.user}'.format(client))


@client.command()
async def teste(ctx):
    await ctx.send(f'teste completo {ctx.author.name}')
@client.event
async def on_member_join(member):
    canalGeral = client.get_channel(769447341652180992)

    fundo = Image.open("fundo.png")
    mascara = Image.open("mascara.png").resize((130, 130))
    avatar = Image.open(requests.get(member.avatar_url,stream=True).raw)

    avatar = avatar.resize(mascara.size)

    mascara.paste(avatar, mask=mascara)
    mascara.save("mascateteste.png")
    font = ImageFont.truetype("font2.ttf", 25)
    draw = ImageDraw.Draw(fundo)
    draw.text((160, 208), member.name, (2000, 2000, 2000), font=font)


    fundo.paste(mascara, (40, 91), mask=mascara)
    fundo.save("teste.png")
    await canalGeral.send(file=discord.File('teste.png'))
@client.command()
async def bemvindo(ctx,target: discord.Member = None):
    canalGeral = client.get_channel(769447341652180992)
    if target == None:
        await ctx.send("You didn't mention anyone!")
    else:

        fundo = Image.open("fundo.png")
        mascara = Image.open("mascara.png").resize((130, 130))
        avatar = Image.open(requests.get(target.avatar_url, stream=True).raw)

        avatar = avatar.resize(mascara.size)

        mascara.paste(avatar, mask=mascara)
        mascara.save("mascateteste.png")
        font = ImageFont.truetype("font2.ttf", 25)
        draw = ImageDraw.Draw(fundo)
        draw.text((160, 208), target.name, (2000, 2000, 2000), font=font)

        fundo.paste(mascara, (40, 91), mask=mascara)
        fundo.save("teste.png")
        await canalGeral.send(file=discord.File('teste.png'))


@client.command()
async def something(ctx, target: discord.Member = None):
    if target == None:
        await ctx.send("You didn't mention anyone!")

    else:
        await ctx.send(target.mention)
client.run(Token)




