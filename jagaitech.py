# jagaitech by potatoblaster

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
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

def simpleEval(arg):
    if arg == "None":
        arg = None
    if arg == "False":
        arg = False
    if arg == "True":
        arg = True
    return arg

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
    arr = [None,None,False,None,False,None,None,None,None,None,None,False,None,None,None,False,None,None,None,False,None,None,None,False,None,None]
    arp = arr[0]
    rrp = arr[1]
    arpstarted = arr[2]
    arptimestarted = arr[3]
    rrpstarted = arr[4]
    rrptimestarted = arr[5]
    arphost = arr[6]
    rrphost = arr[7]
    arpdoc = arr[8]
    rrpdoc = arr[9]
    cqrphost = arr[10]
    cqrpstarted = arr[11]
    cqrptimestarted = arr[12]
    cqrpdoc = arr[13]
    tnrrphost = arr[14]
    tnrrpstarted = arr[15]
    tnrrptimestarted = arr[16]
    tnrrpdoc = arr[17]
    dndrphost = arr[18]
    dndrpstarted = arr[19]
    dndrptimestarted = arr[20]
    dndrpdoc = arr[21]
    kdmrphost = arr[22]
    kdmrpstarted = arr[23]
    kdmrptimestarted = arr[24]
    kdmrpdoc = arr[25]

@bot.command(pass_context=True)
async def arr(ctx):
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
    if str(ctx.message.author.id) == "154552600073601024":
        await bot.say("["+str(arp)+","+str(rrp)+","+str(arpstarted)+","+str(arptimestarted)+","+str(rrpstarted)+","+str(rrptimestarted)+","+str(arphost)+","+str(rrphost)+","+str(arpdoc)+","+str(rrpdoc)+","+str(cqrphost)+","+str(cqrpstarted)+","+str(cqrptimestarted)+","+str(cqrpdoc)+","+str(tnrrphost)+","+str(tnrrpstarted)+","+str(tnrrptimestarted)+","+str(tnrrpdoc)+","+str(dndrphost)+","+str(dndrpstarted)+","+str(dndrptimestarted)+","+str(dndrpdoc)+","+str(kdmrphost)+","+str(kdmrpstarted)+","+str(kdmrptimestarted)+","+str(kdmrpdoc)+"]")
        return
    else:
        embed = discord.Embed(title="User cannot use this command.")
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def setvar(ctx,*,arr):
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
    if str(ctx.message.author.id) == "154552600073601024":
        arr = str(arr)
        arr = arr[1:-1]
        arr = arr.split(",")
        if not len(arr) == 26:
            await bot.say("There are not enough arguments.")
            return
        arr = list(map(simpleEval, arr))
        arp = arr[0]
        rrp = arr[1]
        arpstarted = arr[2]
        arptimestarted = arr[3]
        rrpstarted = arr[4]
        rrptimestarted = arr[5]
        arphost = arr[6]
        rrphost = arr[7]
        arpdoc = arr[8]
        rrpdoc = arr[9]
        cqrphost = arr[10]
        cqrpstarted = arr[11]
        cqrptimestarted = arr[12]
        cqrpdoc = arr[13]
        tnrrphost = arr[14]
        tnrrpstarted = arr[15]
        tnrrptimestarted = arr[16]
        tnrrpdoc = arr[17]
        dndrphost = arr[18]
        dndrpstarted = arr[19]
        dndrptimestarted = arr[20]
        dndrpdoc = arr[21]
        kdmrphost = arr[22]
        kdmrpstarted = arr[23]
        kdmrptimestarted = arr[24]
        kdmrpdoc = arr[25]
        await bot.say("setvar successful.")
    else:
        embed = discord.Embed(title="User cannot use this command.")
        await bot.say(embed=embed)
        

@bot.command(pass_context=True)
async def say(ctx, *, arg):
    if str(ctx.message.author.id) == "154552600073601024":
        if arg == "test":
            arg = ctx.message.server.get_member("154552600073601024").name
        await bot.say(arg)
    else:
        embed = discord.Embed(title="User cannot use this command.")
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def whatis(ctx, *, arg):
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
    if str(ctx.message.author.id) == "154552600073601024":
        await bot.say(globals()[arg])
    else:
        embed = discord.Embed(title="User cannot use this command.")
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def update(ctx, *, arg):
    global arptimestarted
    global rrptimestarted
    global cqrptimestarted
    global tnrrptimestarted
    global dndrptimestarted
    global kdmrptimestarted
    if str(ctx.message.author.id) == "154552600073601024":
        globals()[arg] = float(globals()[arg])
    else:
        embed = discord.Embed(title="User cannot use this command.")
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
@commands.has_any_role("Staff","Voice","Host")
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
                embed.add_field(name="Host:",value=ctx.message.server.get_member(arphost).name)
            if not arpdoc == None:
                embed.add_field(name="Doc:",value=arpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is "+str(arp)+".",description="In progress for: "+toTime(time.time()-arptimestarted))
            if not arphost == None:
                embed.add_field(name="Host:",value=ctx.message.server.get_member(arphost).name)
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
                embed.add_field(name="Host:",value=ctx.message.server.get_member(rrphost).name)
            if not rrpdoc == None:
                embed.add_field(name="Doc:",value=rrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is "+str(rrp)+".",description="In progress for: "+toTime(time.time()-rrptimestarted))
            if not rrphost == None:
                embed.add_field(name="Host:",value=ctx.message.server.get_member(rrphost).name)
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
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(cqrphost).name)
            if not cqrpdoc == None:
                embed.add_field(name="Doc: ",value=cqrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Conquest.",description="In progress for: "+toTime(time.time()-cqrptimestarted))
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(cqrphost).name)
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
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(tnrrphost).name)
            if not tnrrpdoc == None:
                embed.add_field(name="Doc: ",value=tnrrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Trainer.",description="In progress for: "+toTime(time.time()-tnrrptimestarted))
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(tnrrphost).name)
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
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(dndrphost).name)
            if not dndrpdoc == None:
                embed.add_field(name="Doc: ",value=dndrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Dungeons \'n Dragonites.",description="In progress for: "+toTime(time.time()-dndrptimestarted))
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(dndrphost).name)
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
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(kdmrphost).name)
            if not kdmrpdoc == None:
                embed.add_field(name="Doc: ",value=kdmrpdoc,inline=False)
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(title="The RP is Kingdom.",description="In progress for: "+toTime(time.time()-kdmrptimestarted))
            embed.add_field(name="Host: ",value=ctx.message.server.get_member(kdmrphost).name)
            if not kdmrpdoc == None:
                embed.add_field(name="Doc: ",value=kdmrpdoc,inline=False)
            await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rpend"])
@commands.has_any_role("Staff","Voice","Host")
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
    role = get(ctx.message.server.roles, id="host id")
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
        if not arphost == None:
            host = ctx.message.server.get_member(arphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
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
        if not rrphost == None:
            host = ctx.message.server.get_member(rrphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
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
        host = ctx.message.server.get_member(cqrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
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
        host = ctx.message.server.get_member(tnrrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
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
        host = ctx.message.server.get_member(dndrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
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
        host = ctx.message.server.get_member(kdmrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
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
    role = get(ctx.message.server.roles, id="host id")
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if not arphost == None:
            host = ctx.message.server.get_member(arphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
        arphost = user.id
        await bot.add_roles(user,role)
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "rusty_rp":
        if rrp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if not rrphost == None:
            host = ctx.message.server.get_member(rrphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
        rrphost = user.id
        await bot.add_roles(user,role)
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "conquest":
        if not cqrphost == None:
            host = ctx.message.server.get_member(cqrphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
        cqrphost = user.id
        await bot.add_roles(user,role)
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if not tnrrphost == None:
            host = ctx.message.server.get_member(tnrrphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
        tnrrphost = user.id
        await bot.add_roles(user,role)
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if not dndrphost == None:
            host = ctx.message.server.get_member(dndrphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
        dndrphost = user.id
        await bot.add_roles(user,role)
        embed = discord.Embed(title="The host has been set to "+user.display_name+".")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if not kdmrphost == None:
            host = ctx.message.server.get_member(kdmrphost)
            if "host id" in [y.id for y in host.roles]:
                await bot.remove_roles(host,role)
        kdmrphost = user.id
        await bot.add_roles(user,role)
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
    role = get(ctx.message.server.roles, id="host id")
    if ctx.message.channel.name == "amphy_rp":
        if arp == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
        if arphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        host = ctx.message.server.get_member(arphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
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
        host = ctx.message.server.get_member(rrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
        rrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "conquest":
        if cqrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        host = ctx.message.server.get_member(cqrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
        cqrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "trainer":
        if tnrrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        host = ctx.message.server.get_member(tnrrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
        tnrrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "dungeons_n_dragonites":
        if dndrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        host = ctx.message.server.get_member(dndrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
        dndrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)
    if ctx.message.channel.name == "kingdom":
        if kdmrphost == None:
            embed = discord.Embed(title="There is no host.")
            await bot.say(embed=embed)
            return
        host = ctx.message.server.get_member(kdmrphost)
        if "host id" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
        kdmrphost = None
        embed = discord.Embed(title="The host has been removed.")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sd"])
@commands.has_any_role("Staff","Voice","Host")
async def setdoc(ctx, *, doc):
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
@commands.has_any_role("Staff","Voice","Host")
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