# jagaitech by potatoblaster

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import time
import math
import random
import ast

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
#turn seconds into hh:mm:ss format

def idToString(arg):
    if str(arg).isdigit():
        return str(arg)
#for listreplace to work properly

def channelindex(arg):
    rplist = ['customs-one','customs-two','conquest','trainer','dungeons-n-dragonites','kingdom','pokéhigh','murder-mystery','good-vs-evil']
    if arg in rplist:
        return rplist.index(arg)
#check channel

@bot.event
async def on_ready():
    print (bot.user.name)
    print (bot.user.id)
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    rp = [None, None, 'Conquest', 'Trainer', 'Dungeons & Dragonites', 'Kingdom', 'Pokéhigh', 'Murder Mystery', 'Good vs Evil']
    rpstarted = [False, False, False, False, False, False, False, False, False]
    rptimestarted = [None, None, None, None, None, None, None, None, None]
    rphost = [None, None, None, None, None, None, None, None, None]
    rpdoc = [None, None, None, None, None, None, None, None, None]

@bot.command(pass_context=True)
async def whatis(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    if ctx.message.author.id == "154552600073601024":
        arg = arg.split(',')
        if len(arg) == 2:
            index = channelindex(arg[1])
            await bot.say(globals()[arg[0]][index])
#returns specific value

@bot.command(pass_context=True)
async def replace(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    if ctx.message.author.id == "154552600073601024":
        arg = arg.split(',')
        if len(arg) == 3:
            index = channelindex(arg[1])
            globals()[arg[0]][index] = arg[2]
            await bot.say("Replace successful.")
#replaces specific value

@bot.command(pass_context=True)
async def arr(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    if ctx.message.author.id == "154552600073601024":
        await bot.say(rp)
        await bot.say(rpstarted)
        await bot.say(rptimestarted)
        await bot.say(rphost)
        await bot.say(rpdoc)
#returns values for listreplace

@bot.command(pass_context=True)
async def listreplace(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    if ctx.message.author.id == "154552600073601024":
        arg = arg.split(',',1)
        if len(arg) == 2:
            await bot.say(arg[0])
            await bot.say(arg[1])
            replacelist = ast.literal_eval(arg[1])
            if arg[0] == "rphost":
                replacelist = list(map(idToString,replacelist))
            globals()[arg[0]] = replacelist
            await bot.say("Replace successful.")
#replaces list values for rp/rpstarted/rptimestarted/rphost/rpdoc

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
    global rp
    global rpstarted
    index = channelindex(ctx.message.channel.name)
    if index == 0 or index == 1:
        rp[index] = roleplay
        embed = discord.Embed(title="The RP was set to "+str(roleplay)+". Use .start to start the RP.")
        if rpstarted[index]:
            embed = discord.Embed(title="The RP was set to "+str(roleplay)+".")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["startrp","rpstart"])
@commands.has_any_role("Staff","Voice","Host")
async def start(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    index = channelindex(ctx.message.channel.name)
    if index == 0 or index == 1:
        if rp[index] == None:
            embed = discord.Embed(title="No RP has been set.")
            await bot.say(embed=embed)
            return
        if rpstarted[index]:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        rpstarted[index] = True
        rptimestarted[index] = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)
    if index > 1:
        if rphost[index] == None:
            embed = discord.Embed(title="Please set a host first.")
            await bot.say(embed=embed)
            return
        if rpstarted[index]:
            embed = discord.Embed(title="The RP has already started.")
            await bot.say(embed=embed)
            return
        rpstarted[index] = True
        rptimestarted[index] = time.time()
        embed = discord.Embed(title="The RP has started.")
        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rp","arpee","host","doc"])
async def roleplay(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    index = channelindex(ctx.message.channel.name)
    if index == 0 or index == 1:
        if rp[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    else:
        if rphost[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    if not rpstarted[index]:
        embed = discord.Embed(title="The RP is "+str(rp[index])+". Use .start to start the RP.")
    else:
        embed = discord.Embed(title="The RP is "+str(rp[index])+".",description="In progress for: "+toTime(time.time()-rptimestarted[index]))
    if not rphost[index] == None:
        embed.add_field(name="Host:",value=ctx.message.server.get_member(rphost[index]).name)
    if not rpdoc[index] == None:
        embed.add_field(name="Doc:",value=rpdoc[index],inline=False)
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rpend"])
@commands.has_any_role("Staff","Voice","Host")
async def endrp(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    index = channelindex(ctx.message.channel.name)
    role = get(ctx.message.server.roles, id="host id here")
    if index == 0 or index == 1:
        if rp[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    else:
        if rphost[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    if not rpstarted[index]:
        embed = discord.Embed(title="The RP has ended.")
    else:
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-rptimestarted[index]))
    if index == 0 or index == 1:
        rp[index] = None
    rpstarted[index] = False
    rptimestarted[index] = None
    if not rphost[index] == None:
        host = ctx.message.server.get_member(rphost[index])
        if "host id here" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
    rphost[index] = None
    rpdoc[index] = None
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sh"])
@commands.has_any_role("Staff","Voice")
async def sethost(ctx,user:discord.Member):
    global rp
    global rphost
    index = channelindex(ctx.message.channel.name)
    role = get(ctx.message.server.roles, id="host id here")
    if index == 0 or index == 1:
        if rp[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    if not rphost[index] == None:
        host = ctx.message.server.get_member(rphost[index])
        if "host id here" in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
    rphost[index] = user.id
    await bot.add_roles(user,role)
    embed = discord.Embed(title="The host has been set to "+user.display_name+".")
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sd"])
@commands.has_any_role("Staff","Voice","Host")
async def setdoc(ctx, *, doc):
    global rp
    global rphost
    global rpdoc
    index = channelindex(ctx.message.channel.name)
    if index == 0 or index == 1:
        if rp[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    else:
        if rphost[index] == None:
            embed = discord.Embed(title="There is no RP. Please set a host first.")
            await bot.say(embed=embed)
            return
    doc = str(doc)
    rpdoc[index] = doc
    embed = discord.Embed(title="The doc has been set to "+doc+".")
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rmd,rmdoc"])
@commands.has_any_role("Staff","Voice","Host")
async def removedoc(ctx):
    global rp
    global rpdoc
    global rphost
    index = channelindex(ctx.message.channel.name)
    if index == 0 or index == 1:
        if rp[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    else:
        if rphost[index] == None:
            embed = discord.Embed(title="There is no RP.")
            await bot.say(embed=embed)
            return
    if rpdoc[index] == None:
        embed = discord.Embed(title="There is no doc.")
        await bot.say(embed=embed)
        return
    rpdoc[index] = None
    embed = discord.Embed(title="The doc has been removed.")
    await bot.say(embed=embed)

bot.run("insert token here")