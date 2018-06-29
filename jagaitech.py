# jagaitech by potatoblaster

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import math
import random

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
    global cqrphost
    global cqrpstarted
    global cqrptimestarted
    global cqrpdoc
    global tnrrphost
    global tnrrpstarted
    global tnrrptimestarted
    global tnrrpdoc
    global dndrphost
    global dndrpstarted
    global dndrptimestarted
    global dndrpdoc
    global kdmrphost
    global kdmrpstarted
    global kdmrptimestarted
    global kdmrpdoc
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
    cqrphost = None
    cqrpstarted = False
    cqrptimestarted = None
    cqrpdoc = None
    tnrrphost = None
    tnrrpstarted = False
    tnrrptimestarted = None
    tnrrpdoc = None
    dndrphost = None
    dndrpstarted = False
    dndrptimestarted = None
    dndrpdoc = None
    kdmrphost = None
    kdmrpstarted = False
    kdmrptimestarted = None
    kdmrpdoc = None

@bot.command(pass_context=True)
async def say(ctx, *, arg):
    if str(ctx.message.author.id) == "154552600073601024":
        await bot.say(arg)
    else:
        embed = discord.Embed(title="User is too much of a skrub to use this command.")
        await bot.say(embed=embed)

@bot.command(aliases=["dice"])
async def roll(num):
    num = int(num)
    if num < 1 or num > 10000:
        embed = discord.Embed(title="Please enter a number between 1 and 10000.")
        await bot.say(embed=embed)
        return
    embed = discord.Embed(title=random.randint(1,num))
    await bot.say(embed=embed)

@bot.command(aliases=["choose"])
async def pick(*, arg):
    args = arg.split(",")
    if len(args) == 1:
        embed = discord.Embed(title="Please provide more than one choice.")
        await bot.say(embed=embed)
        return
    if len(args) > 10:
        embed = discord.Embed(title="Please provide less than ten options.")
        await bot.say(embed=embed)
        return
    embed = discord.Embed(title=random.choice(args))
    await bot.say(embed=embed)

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
    global cqrphost
    global cqrpstarted
    global cqrptimestarted
    global tnrrphost
    global tnrrpstarted
    global tnrrptimestarted
    global dndrphost
    global dndrpstarted
    global dndrptimestarted
    global kdmrphost
    global kdmrpstarted
    global kdmrptimestarted
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
    if ctx.message.channel.name == "conquest":
        if cqrphost == None:
            embed = discord.Embed(title="Please set a host first.")
            await bot.say(embed=embed)
            return
        if cqrpstarted:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        cqrpstarted = True
        cqrptimestarted = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if tnrrphost == None:
            embed = discord.Embed(title="Please set a host first.")
            await bot.say(embed=embed)
            return
        if tnrrpstarted:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        tnrrpstarted = True
        tnrrptimestarted = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if dndrphost == None:
            embed = discord.Embed(title="Please set a host first.")
            await bot.say(embed=embed)
            return
        if dndrpstarted:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        dndrpstarted = True
        dndrptimestarted = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if kdmrphost == None:
            embed = discord.Embed(title="Please set a host first.")
            await bot.say(embed=embed)
            return
        if kdmrpstarted:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        kdmrpstarted = True
        kdmrptimestarted = time.time()
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
    global cqrphost
    global cqrpstarted
    global cqrptimestarted
    global cqrpdoc
    global tnrrphost
    global tnrrpstarted
    global tnrrptimestarted
    global tnrrpdoc
    global dndrphost
    global dndrpstarted
    global dndrptimestarted
    global dndrpdoc
    global kdmrphost
    global kdmrpstarted
    global kdmrptimestarted
    global kdmrpdoc
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
    if ctx.message.channel.name == "conquest":
        if cqrphost == None:
            embed = discord.Embed(title="There is no Conquest running.")
            await bot.say(embed=embed)
            return
        if not cqrpstarted:
            embed = discord.Embed(title="The RP is Conquest. Use .start to start the RP.")
            embed.add_field(name="Host: ",value=cqrphost)
            if not cqrpdoc == None:
                embed.add_field(name="Doc: ",value=cqrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Conquest.",description="In progress for: "+toTime(time.time()-cqrptimestarted))
            embed.add_field(name="Host: ",value=cqrphost)
            if not cqrpdoc == None:
                embed.add_field(name="Doc: ",value=cqrpdoc,inline=False)
            await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if tnrrphost == None:
            embed = discord.Embed(title="There is no Trainer running.")
            await bot.say(embed=embed)
            return
        if not tnrrpstarted:
            embed = discord.Embed(title="The RP is Trainer. Use .start to start the RP.")
            embed.add_field(name="Host: ",value=tnrrphost)
            if not tnrrpdoc == None:
                embed.add_field(name="Doc: ",value=tnrrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Trainer.",description="In progress for: "+toTime(time.time()-tnrrptimestarted))
            embed.add_field(name="Host: ",value=tnrrphost)
            if not tnrrpdoc == None:
                embed.add_field(name="Doc: ",value=tnrrpdoc,inline=False)
            await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if dndrphost == None:
            embed = discord.Embed(title="There is no Dungeons \'n Dragonites running.")
            await bot.say(embed=embed)
            return
        if not dndrpstarted:
            embed = discord.Embed(title="The RP is Dungeons \'n Dragonites. Use .start to start the RP.")
            embed.add_field(name="Host: ",value=dndrphost)
            if not dndrpdoc == None:
                embed.add_field(name="Doc: ",value=dndrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Dungeons \'n Dragonites.",description="In progress for: "+toTime(time.time()-dndrptimestarted))
            embed.add_field(name="Host: ",value=dndrphost)
            if not dndrpdoc == None:
                embed.add_field(name="Doc: ",value=dndrpdoc,inline=False)
            await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if kdmrphost == None:
            embed = discord.Embed(title="There is no Kingdom running.")
            await bot.say(embed=embed)
            return
        if not kdmrpstarted:
            embed = discord.Embed(title="The RP is Kingdom. Use .start to start the RP.")
            embed.add_field(name="Host: ",value=kdmrphost)
            if not kdmrpdoc == None:
                embed.add_field(name="Doc: ",value=kdmrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Kingdom.",description="In progress for: "+toTime(time.time()-kdmrptimestarted))
            embed.add_field(name="Host: ",value=kdmrphost)
            if not kdmrpdoc == None:
                embed.add_field(name="Doc: ",value=kdmrpdoc,inline=False)
            await bot.say(embed=embed)


@bot.command(pass_context=True,aliases=["rpend"])
@commands.has_any_role("Staff")
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
    global cqrphost
    global cqrpstarted
    global cqrptimestarted
    global cqrpdoc
    global tnrrphost
    global tnrrpstarted
    global tnrrptimestarted
    global tnrrpdoc
    global dndrphost
    global dndrpstarted
    global dndrptimestarted
    global dndrpdoc
    global kdmrphost
    global kdmrpstarted
    global kdmrptimestarted
    global kdmrpdoc
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
    if ctx.message.channel.name == "conquest":
        if cqrphost == None:
            embed = discord.Embed(title="There is no Conquest running.")
            await bot.say(embed=embed)
            return
        if not cqrpstarted:
            cqrptimestarted = time.time()
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-cqrptimestarted))
        cqrphost = None
        cqrpstarted = False
        cqrptimestarted = None
        cqrpdoc = None
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if tnrrphost == None:
            embed = discord.Embed(title="There is no Trainer running.")
            await bot.say(embed=embed)
            return
        if not tnrrpstarted:
            tnrrptimestarted = time.time()
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-tnrrptimestarted))
        tnrrphost = None
        tnrrpstarted = False
        tnrrptimestarted = None
        tnrrpdoc = None
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if dndrphost == None:
            embed = discord.Embed(title="There is no Dungeons \'n Dragonites running.")
            await bot.say(embed=embed)
            return
        if not dndrpstarted:
            dndrptimestarted = time.time()
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-dndrptimestarted))
        dndrphost = None
        dndrpstarted = False
        dndrptimestarted = None
        dndrpdoc = None
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if kdmrphost == None:
            embed = discord.Embed(title="There is no Kingdom running.")
            await bot.say(embed=embed)
            return
        if not kdmrpstarted:
            kdmrptimestarted = time.time()
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-kdmrptimestarted))
        kdmrphost = None
        kdmrpstarted = False
        kdmrptimestarted = None
        kdmrpdoc = None
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sh"])
@commands.has_any_role("Staff","Voice")
async def sethost(ctx,user:discord.Member):
    global arp
    global rrp
    global arphost
    global rrphost
    global cqrphost
    global tnrrphost
    global dndrphost
    global kdmrphost
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
    if ctx.message.channel.name == "conquest":
        cqrphost = user.display_name
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        tnrrphost = user.display_name
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        dndrphost = user.display_name
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        kdmrphost = user.display_name
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rmh,rmhost"])
@commands.has_any_role("Staff","Voice")
async def removehost(ctx):
    global arp
    global rrp
    global arphost
    global rrphost
    global cqrphost
    global tnrrphost
    global dndrphost
    global kdmrphost
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
    if ctx.message.channel.name == "conquest":
        if cqrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        cqrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if tnrrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        tnrrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if dndrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        dndrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if kdmrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        kdmrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sd"])
@commands.has_any_role("Staff","Voice")
async def setdoc(ctx, doc):
    global arp
    global rrp
    global arpdoc
    global rrpdoc
    global cqrpdoc
    global tnrrpdoc
    global dndrpdoc
    global kdmrpdoc
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
    if ctx.message.channel.name == "conquest":
        if cqrphost == None:
            embed = discord.Embed(title="There is no RP running. Please set a host first.")
            await bot.say(embed=embed)
            return
        doc = str(doc)
        cqrpdoc = doc
        embed = discord.Embed(title="The doc has been set to "+cqrpdoc)
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if tnrrphost == None:
            embed = discord.Embed(title="There is no RP running. Please set a host first.")
            await bot.say(embed=embed)
            return
        doc = str(doc)
        tnrrpdoc = doc
        embed = discord.Embed(title="The doc has been set to "+tnrrpdoc)
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if dndrphost == None:
            embed = discord.Embed(title="There is no RP running. Please set a host first.")
            await bot.say(embed=embed)
            return
        doc = str(doc)
        dndrpdoc = doc
        embed = discord.Embed(title="The doc has been set to "+dndrpdoc)
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if kdmrphost == None:
            embed = discord.Embed(title="There is no RP running. Please set a host first.")
            await bot.say(embed=embed)
            return
        doc = str(doc)
        kdmrpdoc = doc
        embed = discord.Embed(title="The doc has been set to "+kdmrpdoc)
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

bot.run("insert token here")