# jagaitech by potatoblaster

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import math

bot = commands.Bot(command_prefix='.')

def toTime(time):
    time = math.floor(time)
    seconds = time % 60
    seconds = str(seconds).zfill(2)
    minutes = math.floor((time % 3600)/60)
    minutes = str(minutes).zfill(2)
    hours = math.floor(time/3600)
    hours = str(hours).zfill(2)
    return(hours+":"+minutes+":"+seconds)

@bot.event
async def on_ready():
    print (bot.user.name)
    print (bot.user.id)
    global arp
    global rrp
    global arpstarted
    global arptimestarted
    global rrpstarted
    global rrptimestarted
    global arphost
    global rrphost
    global arpdoc
    global rrpdoc
    arp = None
    rrp = None
    arpstarted = False
    arptimestarted = None
    rrpstarted = False
    rrptimestarted = None
    arphost = None
    rrphost = None
    arpdoc = None
    rrpdoc = None

@bot.command(pass_context=True,aliases=["rpset"])
@commands.has_any_role("Staff","Voice")
async def setrp(ctx,*,roleplay):
    global arp
    global rrp
    if ctx.message.channel.name == "amphy_rp":
        arp = roleplay
        embed = discord.Embed(title="The RP was set to "+str(arp)+". Use .start to start the RP.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        rrp = roleplay
        embed = discord.Embed(title="The RP was set to "+str(rrp)+". Use .start to start the RP.")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["startrp","rpstart"])
@commands.has_any_role("Staff","Voice")
async def start(ctx):
    global arp
    global rrp
    global arpstarted
    global rrpstarted
    global arptimestarted
    global rrptimestarted
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="No RP has been set.")
            await bot.say(embed=embed)
            return
        if arpstarted:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        arpstarted = True
        arptimestarted = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="No RP has been set.")
            await bot.say(embed=embed)
            return
        if rrpstarted:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        rrpstarted = True
        rrptimestarted = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)


@bot.command(pass_context=True,aliases=["rp","arpee","host","doc"])
async def roleplay(ctx):
    global arp
    global rrp
    global arpstarted
    global rrpstarted
    global arptimestarted
    global rrptimestarted
    global arphost
    global rrphost
    global arpdoc
    global rrpdoc
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if not arpstarted:
            embed = discord.Embed(title="The RP is "+str(arp)+". Use .start to start the RP.")
            if not arphost == None:
                embed.add_field(name="Host:",value=arphost)
            if not arpdoc == None:
                embed.add_field(name="Doc:",value=arpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is "+str(arp)+".",description="In progress for: "+toTime(time.time()-arptimestarted))
            if not arphost == None:
                embed.add_field(name="Host:",value=arphost)
            if not arpdoc == None:
                embed.add_field(name="Doc:",value=arpdoc,inline=False)
            await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if not rrpstarted:
            embed = discord.Embed(title="The RP is "+str(rrp)+". Use .start to start the RP.")
            if not rrphost == None:
                embed.add_field(name="Host:",value=rrphost)
            if not rrpdoc == None:
                embed.add_field(name="Doc:",value=rrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is "+str(rrp)+".",description="In progress for: "+toTime(time.time()-rrptimestarted))
            if not rrphost == None:
                embed.add_field(name="Host:",value=rrphost)
            if not rrpdoc == None:
                embed.add_field(name="Doc:",value=rrpdoc,inline=False)
            await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rpend"])
@commands.has_any_role("Staff","Voice")
async def endrp(ctx):
    global arp
    global rrp
    global arpstarted
    global rrpstarted
    global arptimestarted
    global rrptimestarted
    global arphost
    global rrphost
    global arpdoc
    global rrpdoc
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if not arpstarted:
            arptimestarted = time.time()
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-arptimestarted))
        arp = None
        arpstarted = False
        arptimestarted = None
        arphost = None
        arpdoc = None
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if not rrpstarted:
            rrptimestarted = time.time()
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-rrptimestarted))
        rrp = None
        rrpstarted = False
        rrptimestarted = None
        rrphost = None
        rrpdoc = None
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sh"])
@commands.has_any_role("Staff","Voice")
async def sethost(ctx,user:discord.Member):
    global arp
    global rrp
    global arphost
    global rrphost
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        arphost = user.display_name
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        rrphost = user.display_name
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rmh,rmhost"])
@commands.has_any_role("Staff","Voice")
async def removehost(ctx):
    global arp
    global rrp
    global arphost
    global rrphost
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if arphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        arphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if rrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        rrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sd"])
@commands.has_any_role("Staff","Voice")
async def setdoc(ctx, doc):
    global arp
    global rrp
    global arpdoc
    global rrpdoc
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        doc = str(doc)
        arpdoc = doc
        embed = discord.Embed(title="The doc has been set to "+arpdoc)
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        doc = str(doc)
        rrpdoc = doc
        embed = discord.Embed(title="The doc has been set to "+rrpdoc)
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rmd,rmdoc"])
@commands.has_any_role("Staff","Voice")
async def removedoc(ctx):
    global arp
    global rrp
    global arpdoc
    global rrpdoc
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if arpdoc == None:
            embed = discord.Embed(title="There is no doc.")
            await bot.say(embed=embed)
            return
        arpdoc = None
        embed = discord.Embed(title="The doc has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if rrpdoc == None:
            embed = discord.Embed(title="There is no doc.")
            await bot.say(embed=embed)
            return
        rrpdoc = None
        embed = discord.Embed(title="The doc has been removed.")
        await bot.say(embed=embed)

bot.run("insert token")