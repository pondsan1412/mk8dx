#
#
#

from asyncore import loop
from email import message
from unicodedata import name
import discord
from discord.ext import commands
import time
import asyncio
import asyncio
from email import message
import functools
import itertools
import math
import random
from discord import FFmpegAudio
import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
status = 0
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print(f"Logged in as{client.user}")


@client.event
async def on_ready():
    print('The bot is logged in.')
    while True:
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} servers!"))
        await asyncio.sleep(1)
    
@client.event
async def on_message(message):
    if message.content.startswith('.1-1'):#MKS number
        embedVar = discord.Embed(title="Mario Kart Stedium", description="Tracks code: MKS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967821303761473578/MKS.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.MKS'):#MKS text
        embedVar = discord.Embed(title="Mario Kart Stedium", description="Tracks code: MKS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967821303761473578/MKS.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.WP'):#WP text
        embedVar = discord.Embed(title="Water Park", description="Tracks code: WP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863293433770064/WP.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.1-2'):#WP number
        embedVar = discord.Embed(title="Water Park", description="Tracks code: WP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863293433770064/WP.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.SSC'):#SSC text
        embedVar = discord.Embed(title="Sweet Sweet Canyon", description="Tracks code: SSC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863345313095750/SCC.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.1-3'):#SSC n
        embedVar = discord.Embed(title="Sweet Sweet Canyon", description="Tracks code: SSC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863345313095750/SCC.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.1-4'):#TR text
        embedVar = discord.Embed(title="Thwomp Ruins", description="Tracks code: TR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863377651200101/TR.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.TR'):#TR text
        embedVar = discord.Embed(title="Thwomp Ruins", description="Tracks code: TR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863377651200101/TR.png")
        embedVar.add_field(name="Mushroom Cup", value="European code: 1-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.2-1'):#TR text
        embedVar = discord.Embed(title="Mario Circuit", description="Tracks code: MC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863755084005376/MC.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.MC'):#TR text
        embedVar = discord.Embed(title="Mario Circuit", description="Tracks code: MC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863755084005376/MC.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.2-2'):#TR text
        embedVar = discord.Embed(title="Toad Harbor", description="Tracks code: TH", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863786272874636/TH.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.TH'):#TR text
        embedVar = discord.Embed(title="Toad Harbor", description="Tracks code: TH", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863786272874636/TH.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.2-3'):#TR text
        embedVar = discord.Embed(title="Twisted Mansion", description="Tracks code: TM", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863811392561193/TM.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.TM'):#TR text
        embedVar = discord.Embed(title="Twisted Mansion", description="Tracks code: TM", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863811392561193/TM.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.2-4'):#TR text
        embedVar = discord.Embed(title="Shy Guy Falls", description="Tracks code: SGF", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863847392247829/SGF.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.SGF'):#TR text
        embedVar = discord.Embed(title="Shy Guy Falls", description="Tracks code: SGF", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863847392247829/SGF.png")
        embedVar.add_field(name="Flower Cup", value="European code: 2-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.SA'):#TR text
        embedVar = discord.Embed(title="Sunshine Airport", description="Tracks code: SA", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863871853445131/SA.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.3-1'):#TR text
        embedVar = discord.Embed(title="Sunshine Airport", description="Tracks code: SA", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863871853445131/SA.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.DS'):#TR text
        embedVar = discord.Embed(title="Dophine Shoals", description="Tracks code: DS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863916526968922/DS.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.3-2'):#TR text
        embedVar = discord.Embed(title="Dophine Shoals", description="Tracks code: DS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967863916526968922/DS.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.3-3'):#TR text
        embedVar = discord.Embed(title="Electrodrome", description="Tracks code: ED", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864001402916974/Ed.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.ED'):#TR text
        embedVar = discord.Embed(title="Electrodrome", description="Tracks code: ED", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864001402916974/Ed.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.3-4'):#TR text
        embedVar = discord.Embed(title="Mount Wario", description="Tracks code: MW", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864021665579068/MW.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.MW'):#TR text
        embedVar = discord.Embed(title="Mount Wario", description="Tracks code: MW", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864021665579068/MW.png")
        embedVar.add_field(name="Star Cup", value="European code: 3-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.4-1'):#TR text
        embedVar = discord.Embed(title="Cloudtop Cruise", description="Tracks code: CC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864050547556362/CC.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.CC'):#TR text
        embedVar = discord.Embed(title="Cloudtop Cruise", description="Tracks code: CC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864050547556362/CC.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.4-2'):#TR text
        embedVar = discord.Embed(title="Bone-Dry Dunes", description="Tracks code: BDD", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864081413443584/BDD.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.BDD'):#TR text
        embedVar = discord.Embed(title="Bone-Dry Dunes", description="Tracks code: BDD", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864081413443584/BDD.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.4-3'):#TR text
        embedVar = discord.Embed(title="Bowser's Castle", description="Tracks code: BC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864095351111761/BC.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.BC'):#TR text
        embedVar = discord.Embed(title="Bowser's Castle", description="Tracks code: BC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864095351111761/BC.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.4-4'):#TR text
        embedVar = discord.Embed(title="Rainbow Road", description="Tracks code: RR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864120688926790/RR.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.RR'):#TR text
        embedVar = discord.Embed(title="Rainbow Road", description="Tracks code: RR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864120688926790/RR.png")
        embedVar.add_field(name="Special Cup", value="European code: 4-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.5-1'):#TR text
        embedVar = discord.Embed(title="Yoshi Circuit", description="Tracks code: dYC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864179828617216/dYC.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dYC'):#TR text
        embedVar = discord.Embed(title="Yoshi Circuit", description="Tracks code: dYC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864179828617216/dYC.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dEA'):#TR text
        embedVar = discord.Embed(title="Excitebike Arena", description="Tracks code: dEA", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864206789582848/dEA.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.5-2'):#TR text
        embedVar = discord.Embed(title="Excitebike Arena", description="Tracks code: dEA", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864206789582848/dEA.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.5-3'):#TR text
        embedVar = discord.Embed(title="Dragon Driftway", description="Tracks code: dDD", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864225139662868/dDD.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dDD'):#TR text
        embedVar = discord.Embed(title="Dragon Driftway", description="Tracks code: dDD", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864225139662868/dDD.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.5-4'):#TR text
        embedVar = discord.Embed(title="Mute City", description="Tracks code: dMC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864252352319518/dMC.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dMC'):#TR text
        embedVar = discord.Embed(title="Mute City", description="Tracks code: dMC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864252352319518/dMC.png")
        embedVar.add_field(name="Egg Cup", value="European code: 5-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dBP'):#TR text
        embedVar = discord.Embed(title="Baby Park", description="Tracks code: dBP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864281116856421/dBP.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.6-1'):#TR text
        embedVar = discord.Embed(title="Baby Park", description="Tracks code: dBP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864281116856421/dBP.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dCL'):#TR text
        embedVar = discord.Embed(title="Cheese Land", description="Tracks code: dCL", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864292047196240/dCL.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.6-2'):#TR text
        embedVar = discord.Embed(title="Cheese Land", description="Tracks code: dCL", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864292047196240/dCL.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.6-3'):#TR text
        embedVar = discord.Embed(title="Wild Wood", description="Tracks code: dWW", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864311022235709/dWW.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dWW'):#TR text
        embedVar = discord.Embed(title="Wild Wood", description="Tracks code: dWW", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864311022235709/dWW.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-3", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.6-4'):#TR text
        embedVar = discord.Embed(title="Animal Crossing", description="Tracks code: dAC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864323022143579/dAC.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dAC'):#TR text
        embedVar = discord.Embed(title="Animal Crossing", description="Tracks code: dAC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864323022143579/dAC.png")
        embedVar.add_field(name="Crossing Cup", value="European code: 6-4", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.7-1'):#TR text
        embedVar = discord.Embed(title="Moo Moo Meadows", description="Tracks code: rMMM", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864381046128680/rMMM.png")
        embedVar.add_field(name="Shell Cup", value="European code: 7-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rMMM'):#TR text
        embedVar = discord.Embed(title="Moo Moo Meadows", description="Tracks code: rMMM", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864381046128680/rMMM.png")
        embedVar.add_field(name="Shell Cup", value="European code: 7-1", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.7-2'):#TR text
        embedVar = discord.Embed(title="GBA Mario Circuit", description="Tracks code: rMC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864449249706044/rMC.png")
        embedVar.add_field(name="Shell Cup", value="European code: 7-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rMC'):#TR text
        embedVar = discord.Embed(title="GBA Mario Circuit", description="Tracks code: rMC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864449249706044/rMC.png")
        embedVar.add_field(name="Shell Cup", value="European code: 7-2", inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.7-3'):#TR text
        embedVar = discord.Embed(title="Cheep Cheep Beach", description="Tracks code: rCCB", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864459831955507/rCCB.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rCCB'):#TR text
        embedVar = discord.Embed(title="Cheep Cheep Beach", description="Tracks code: rCCB", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864459831955507/rCCB.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.7-4'):#TR text
        embedVar = discord.Embed(title="Toad's Turnpike", description="Tracks code: rTT", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864470972010596/rTT.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.8-1'):#TR text
        embedVar = discord.Embed(title="Dry Dry Desert", description="Tracks code: rDDD", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205682979532882/rDDD.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rDDD'):#TR text
        embedVar = discord.Embed(title="Dry Dry Desert", description="Tracks code: rDDD", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205682979532882/rDDD.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rDP3'):#TR text
        embedVar = discord.Embed(title="Donut Plains 3", description="Tracks code: rDP3", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205784133537792/rDP3.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.8-2'):#TR text
        embedVar = discord.Embed(title="Donut Plains 3", description="Tracks code: rDP3", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205784133537792/rDP3.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.8-3'):#TR text
        embedVar = discord.Embed(title="Royal Raceway", description="Tracks code: rRRy", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205820108099714/rRRY.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rRRy'):#TR text
        embedVar = discord.Embed(title="Royal Raceway", description="Tracks code: rRRy", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205820108099714/rRRY.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rDKJ'):#TR text
        embedVar = discord.Embed(title="3DS DK Jungle", description="Tracks code: rDKJ", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205851036909568/rDKJ.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.8-4'):#TR text
        embedVar = discord.Embed(title="3DS DK Jungle", description="Tracks code: rDKJ", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205851036909568/rDKJ.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.9-1'):#TR text
        embedVar = discord.Embed(title="DS Wario Stedium", description="Tracks code: rWS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205871882580009/rWS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rWS'):#TR text
        embedVar = discord.Embed(title="DS Wario Stedium", description="Tracks code: rWS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205871882580009/rWS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rSL'):#TR text
        embedVar = discord.Embed(title="GCN Sherbet Land", description="Tracks code: rSL", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205882913607730/rSL.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.9-2'):#TR text
        embedVar = discord.Embed(title="GCN Sherbet Land", description="Tracks code: rSL", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968205882913607730/rSL.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rMP'):#TR text
        embedVar = discord.Embed(title="3DS Music Park", description="Tracks code: rMP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209183222665246/rMP.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.9-3'):#TR text
        embedVar = discord.Embed(title="3DS Music Park", description="Tracks code: rMP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209183222665246/rMP.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.9-4'):#TR text
        embedVar = discord.Embed(title="N64 Yoshi Valley", description="Tracks code: rYV", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209267930828800/rYV.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rYV'):#TR text
        embedVar = discord.Embed(title="N64 Yoshi Valley", description="Tracks code: rYV", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209267930828800/rYV.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rTTC'):#TR text
        embedVar = discord.Embed(title="DS Tick-Tock Clock", description="Tracks code: rTTC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209337979924610/rTTC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.10-1'):#TR text
        embedVar = discord.Embed(title="DS Tick-Tock Clock", description="Tracks code: rTTC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209337979924610/rTTC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.10-2'):#TR text
        embedVar = discord.Embed(title="3DS Piranha Plant Slide", description="Tracks code: rPPS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209355906363442/rPPS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rPPS'):#TR text
        embedVar = discord.Embed(title="3DS Piranha Plant Slide", description="Tracks code: rPPS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209355906363442/rPPS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rGV'):#TR text
        embedVar = discord.Embed(title="Wii Grumble Volcano", description="Tracks code: rGV", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209370125045840/rGV.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.10-3'):#TR text
        embedVar = discord.Embed(title="Wii Grumble Volcano", description="Tracks code: rGV", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209370125045840/rGV.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.10-4'):#TR text
        embedVar = discord.Embed(title="N64 Rainbow Road", description="Tracks code: rRRd", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209393248272414/rRRd.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.rRRd'):#TR text
        embedVar = discord.Embed(title="N64 Rainbow Road", description="Tracks code: rRRd", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209393248272414/rRRd.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.11-1'):#TR text
        embedVar = discord.Embed(title="Wii Wario's Gold Mine", description="Tracks code: dWGM", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209425603117056/dWGM.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dWGM'):#TR text
        embedVar = discord.Embed(title="Wii Wario's Gold Mine", description="Tracks code: dWGM", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209425603117056/dWGM.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.11-2'):#TR text
        embedVar = discord.Embed(title="SNES Rainbow Road", description="Tracks code: dRR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209438097940480/dRR.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dRR'):#TR text
        embedVar = discord.Embed(title="SNES Rainbow Road", description="Tracks code: dRR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209438097940480/dRR.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dIIO'):#TR text
        embedVar = discord.Embed(title="Ice Ice Outpost", description="Tracks code: dIIO", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209450567606292/dIIO.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.11-3'):#TR text
        embedVar = discord.Embed(title="Ice Ice Outpost", description="Tracks code: dIIO", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209450567606292/dIIO.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.11-4'):#TR text
        embedVar = discord.Embed(title="Hyrule Circuit", description="Tracks code: dHC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209462257127454/dHC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dHC'):#TR text
        embedVar = discord.Embed(title="Hyrule Circuit", description="Tracks code: dHC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209462257127454/dHC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.12-1'):#TR text
        embedVar = discord.Embed(title="3DS Neo Bowser City", description="Tracks code: dNBC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209471895666738/dNBC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dNBC'):#TR text
        embedVar = discord.Embed(title="3DS Neo Bowser City", description="Tracks code: dNBC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209471895666738/dNBC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dRiR'):#TR text
        embedVar = discord.Embed(title="GBA Ribbon Road", description="Tracks code: dRiR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209498483339384/dRiR.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.12-2'):#TR text
        embedVar = discord.Embed(title="GBA Ribbon Road", description="Tracks code: dRiR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209498483339384/dRiR.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dSBS'):#TR text
        embedVar = discord.Embed(title="Super Bell Subway", description="Tracks code: dSBS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209523040981022/dSBS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.12-3'):#TR text
        embedVar = discord.Embed(title="Super Bell Subway", description="Tracks code: dSBS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209523040981022/dSBS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.12-3'):#TR text
        embedVar = discord.Embed(title="Super Bell Subway", description="Tracks code: dSBS", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209523040981022/dSBS.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.12-4'):#TR text
        embedVar = discord.Embed(title="Big Blue", description="Tracks code: dBB", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209532155232276/dBB.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.dBB'):#TR text
        embedVar = discord.Embed(title="Big Blue", description="Tracks code: dBB", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968209532155232276/dBB.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bPP'):#TR text
        embedVar = discord.Embed(title="Tour Paris Promenade", description="Tracks code: bPP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968218823947853834/bPP.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.13-1'):#TR text
        embedVar = discord.Embed(title="Tour Paris Promenade", description="Tracks code: bPP", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968218823947853834/bPP.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.13-2'):#TR text
        embedVar = discord.Embed(title="3DS Toad Circuit", description="Tracks code: bTC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968220915735351306/bTC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bTC'):#TR text
        embedVar = discord.Embed(title="3DS Toad Circuit", description="Tracks code: bTC", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968220915735351306/bTC.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.13-3'):#TR text
        embedVar = discord.Embed(title="N64 Choco Mountain", description="Tracks code: bCMo", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968220934651674644/bCM64.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bCMo'):#TR text
        embedVar = discord.Embed(title="N64 Choco Mountain", description="Tracks code: bCMo", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968220934651674644/bCM64.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.13-4'):#TR text
        embedVar = discord.Embed(title="Wii Coconut Mall", description="Tracks code: bCMa", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968220944239845436/bCMw.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bCMa'):#TR text
        embedVar = discord.Embed(title="Wii Coconut Mall", description="Tracks code: bCMa", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968220944239845436/bCMw.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.14-1'):#TR text
        embedVar = discord.Embed(title="Tour Tokyo Blue", description="Tracks code: bTB", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222348744478770/bTB.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bTB'):#TR text
        embedVar = discord.Embed(title="Tour Tokyo Blue", description="Tracks code: bTB", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222348744478770/bTB.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bSR'):#TR text
        embedVar = discord.Embed(title="DS Shroom Ridge", description="Tracks code: bSR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222350438977597/bSR.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.14-2'):#TR text
        embedVar = discord.Embed(title="DS Shroom Ridge", description="Tracks code: bSR", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222350438977597/bSR.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.14-3'):#TR text
        embedVar = discord.Embed(title="GBA Sky Garden", description="Tracks code: bSG", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222358055833631/bSG.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bSG'):#TR text
        embedVar = discord.Embed(title="GBA Sky Garden", description="Tracks code: bSG", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222358055833631/bSG.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.14-4'):#TR text
        embedVar = discord.Embed(title="Ninja Hideaway", description="Tracks code: bNH", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222365823672421/bNH.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.bNH'):#TR text
        embedVar = discord.Embed(title="Ninja Hideaway", description="Tracks code: bNH", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/968222365823672421/bNH.png")
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    if message.content.startswith('.help'):
        embedVar = discord.Embed(title=":star: Command for use the bot", description="prefix command using dot (.) infront of anytracks you want. please go with right words don't type only lowercase letter. for example > .dHC .rGV .dRR", color=0x00ff00)
        embedVar.set_thumbnail(url="https://media.tenor.com/images/1625d3706ed4a53aeba484e32fa8ea40/tenor.gif")
        embedVar.set_author(name="Pond サンダー ", url="https://twitter.com/pondsan1412", icon_url="https://cdn-icons-png.flaticon.com/512/124/124021.png")
        embedVar.add_field(name=":bookmark_tabs: Tracks code list",value='[sheet link for tracks code](https://docs.google.com/document/d/1P4CJbTEPskvFAREHMhZrkzSi5EJ3Onqlgyv3NRJyczw/edit?usp=sharing)',inline=False)
        embedVar.add_field(name=":magnet: invite bot to your server", value='[click here to create invite!](https://discord.com/api/oauth2/authorize?client_id=926061900813451264&permissions=517544007744&scope=bot)' , inline=False)
        embedVar.set_footer(text='Developed by pond')
        await message.channel.send(embed=embedVar)
    await client.process_commands(message)#https://cdn.discordapp.com/attachments/967820792131887194/967864470972010596/rTT.png
@client.command()
async def rTT(ctx):
    rTT=discord.Embed(title="Toad's turnpike",color=0xFF5733)
    rTT.set_image(url="https://cdn.discordapp.com/attachments/967820792131887194/967864470972010596/rTT.png")#รูปmks emoji
    rTT.set_footer(text='Developed by pond')
    message = await ctx.send(embed=rTT)
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    
    
   
client.run('put_your_token')