import discord
from discord.ext import commands
import random
import os
import requests


intents = discord.Intents.default()
intents.message_content = True


QUOTES = [
    "ur ip:126.61.155.147",
    "ur ip: 212.93.69.206",
    "ur ip:159.209.159.172",
    "ur ip: 174.163.124.208",
    "ur ip: 208.113.190.162",
    "ur ip: 192.168.1.7",
    "ur ip: 192.168.1.96",
    "ur ip: 192.168.1.41",
    "ur ip: 192.168.1.234"
]


image_chances = {
    'cat1.jpeg': 0.4,
    'cat2.jpeg': 0.7,
    'cat3.jpeg': 1.0,
    'cat4.jpeg': 0.6,
    'cat5.jpeg': 0.9,
    'cat6.jpeg': 0.000001,
    'cat7.jpeg': 0.5,
    'cat8.jpeg': 0.8,
    'cat9.jpeg': 0.6,
    'cat10.jpeg': 0.8,
    'ds-wdsa.jpeg': 0.01,
    'cat12.jpeg': 0.04
}


bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def about(ctx):
    await ctx.send('Cates Vr Adminsitration Horor is cool geim thar was created in november 25 2022.')


@bot.command()
async def secretcommandomg(ctx):
    await ctx.send('U think u smart?')


@bot.command()
async def secretcommandfr(ctx):
    await ctx.send('Wow u find secret command omg. no')


@bot.command()
async def prank(ctx):
    quote = random.choice(QUOTES)
    await ctx.send(quote)


@bot.command()
async def cat(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)  # Выбираем случайное имя изображения из списка images
    with open(f'images/{img_name}', 'rb') as f:  # Используем img_name для открытия соответствующего файла изображения
        picture = discord.File(f)

    await ctx.send(file=picture)


@bot.command()
async def fanart(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)  # Выбираем случайное имя изображения из списка images
    with open(f'images/{img_name}', 'rb') as f:  # Используем img_name для открытия соответствующего файла изображения
        picture = discord.File(f)

    await ctx.send(file=picture)


bot.run('token')
