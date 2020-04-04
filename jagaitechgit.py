# jagaitech by potatoblaster

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from operator import itemgetter
import asyncio
import time
import math
import random
import ast
import pickle
import collections

bot = Bot(command_prefix='.')

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
    rplist = ['official-rp','rusty-rp','custom-rp']
    if arg in rplist:
        return rplist.index(arg)
#check channel

def clearcq():
    global cq
    global cqrequests
    global alliances
    global allyrequests
    global knightrequests
    cq = {
        "fire": [None, None, None, None],
        "water": [None, None, None, None],
        "grass": [None, None, None, None],
        "rock": [None, None, None, None],
        "steel": [None, None, None, None],
        "ground": [None, None, None, None],
        "flying": [None, None, None, None],
        "fairy": [None, None, None, None],
        "dragon": [None, None, None, None],
        "bug": [None, None, None, None],
        "poison": [None, None, None, None],
        "fighting": [None, None, None, None],
        "psychic": [None, None, None, None],
        "ghost": [None, None, None, None],
        "dark": [None, None, None, None],
        "normal": [None, None, None, None],
        "ice": [None, None, None, None],
        "electric": [None, None, None, None]
    }
    cqrequests = {
        "fire": None,
        "water": None,
        "grass": None,
        "rock": None,
        "steel": None,
        "ground": None,
        "flying": None,
        "fairy": None,
        "dragon": None,
        "bug": None,
        "poison": None,
        "fighting": None,
        "psychic": None,
        "ghost": None,
        "dark": None,
        "normal": None,
        "ice": None,
        "electric": None
    }
    alliances = {
        "fire": {None},
        "water": {None},
        "grass": {None},
        "rock": {None},
        "steel": {None},
        "ground": {None},
        "flying": {None},
        "fairy": {None},
        "dragon": {None},
        "bug": {None},
        "poison": {None},
        "fighting": {None},
        "psychic": {None},
        "ghost": {None},
        "dark": {None},
        "normal": {None},
        "ice": {None},
        "electric": {None}
    }
    allyrequests = {
        "fire": None,
        "water": None,
        "grass": None,
        "rock": None,
        "steel": None,
        "ground": None,
        "flying": None,
        "fairy": None,
        "dragon": None,
        "bug": None,
        "poison": None,
        "fighting": None,
        "psychic": None,
        "ghost": None,
        "dark": None,
        "normal": None,
        "ice": None,
        "electric": None
    }
    knightrequests = {
        "fire": None,
        "water": None,
        "grass": None,
        "rock": None,
        "steel": None,
        "ground": None,
        "flying": None,
        "fairy": None,
        "dragon": None,
        "bug": None,
        "poison": None,
        "fighting": None,
        "psychic": None,
        "ghost": None,
        "dark": None,
        "normal": None,
        "ice": None,
        "electric": None
    }

#def createrpdict():
#    f = open("rp","rb")
#    rpdict = pickle.load(f)
#    f.close
#    return rpdict
#creates dictionary from pickled file

#def updaterpdict(arg1,arg2):
#    rpdict = createrpdict()
#    rpdict[arg1] = arg2
#    f = open("rp","wb")
#    pickle.dump(rpdict,f)
#    f.close()

#async def updatetriviarole(arg,guild):
#    global triviascore
#    role1 = discord.utils.get(guild.roles, name="Trivia")
#    role2 = discord.utils.get(guild.roles, name="Trivia Knight")
#    role3 = discord.utils.get(guild.roles, name="Trivia Lord")
#    role4 = discord.utils.get(guild.roles, name="Trivia Nobleman")
#    role5 = discord.utils.get(guild.roles, name="Trivia King")
#    if triviascore[arg.id] == 1:
#        rolelist = [role1,role2,role3,role4,role5]
#        intersection = [value for value in arg.roles if value in rolelist]
#        if intersection == []:
#            await arg.add_roles(arg,role1)
#            return
#    if triviascore["streak"] == 3:
#        rolelist = [role2,role3,role4,role5]
#        intersection = [value for value in arg.roles if value in rolelist]
#        if intersection == []:
#            await arg.remove_roles(arg,role1)
#            await arg.add_roles(arg,role2)
#            embed = discord.Embed(title=arg.name+" has reached "+role2.name+"!")
#            await ctx.send(embed=embed)
#            return
#    if triviascore["streak"] == 5:
#        rolelist = [role3,role4,role5]
#        intersection = [value for value in arg.roles if value in rolelist]
#        if intersection == []:
#            await arg.remove_roles(arg,role2)
#            await arg.add_roles(arg,role3)
#            embed = discord.Embed(title=arg.name+" has reached "+role3.name+"!")
#            await ctx.send(embed=embed)
#            return
#    if triviascore["streak"] == 8:
#        rolelist = [role4,role5]
#        intersection = [value for value in arg.roles if value in rolelist]
#        if intersection == []:
#            await arg.remove_roles(role3.id)
#            await arg.add_roles(role4.id)
#            embed = discord.Embed(title=arg.name+" has reached "+role4.name+"!")
#            await ctx.send(embed=embed)
#            return
#    if triviascore["streak"] == 10:
#        if not role5 in arg.roles:
#            await arg.remove_roles(role4.id)
#            await arg.add_roles(role5.id)
#            embed = discord.Embed(title=arg.name+" has reached "+role5.name+"!")
#            await ctx.send(embed=embed)
#            return
#    return

@bot.event
async def on_ready():
    print (bot.user.name)
    print (bot.user.id)
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpr
    global rprmember
    global rpvoid
    global trivia
    global triviascore
    global cq
    global cqrequests
    global alliances
    global allyrequests
    global knightrequests
    clearcq()
    #f = open("rp","rb")
    #rpdict = pickle.load(f)
    #f.close
    #rp = rpdict["rp"]
    #rpstarted = rpdict["rpstarted"]
    #rptimestarted = rpdict["rptimestarted"]
    #rphost = rpdict["rphost"]
    #rpdoc = rpdict["rpdoc"]
    #rpvoid = rpdict["rpvoid"]
    #trivia = rpdict["trivia"]
    #triviascore = rpdict["triviascore"]
    rp = [None, None, None]
    rpstarted = [False, False, False]
    rptimestarted = [None, None, None]
    rphost = [None, None, None]
    rpdoc = [None, None, None]
    rpvoid = [None, None, None, None]
    trivia = None
    triviascore = None
    rpr = False
    rprmember = None

#@bot.command()
#async def rpdict(ctx):
#    if ctx.author.id == "154552600073601024":
#        rpdict = createrpdict()
#        await ctx.send(rpdict)
#returns pickled file

#@bot.command()
#async def syncrpdict(ctx):
#    global rp
#    global rpstarted
#    global rptimestarted
#    global rphost
#    global rpdoc
#    global rpvoid
#    global trivia
#    global triviascore
#    if ctx.author.id == "154552600073601024":
#        rpdict = {"rp": rp, "rpstarted": rpstarted, "rptimestarted": rptimestarted, "rphost": rphost, "rpdoc": rpdoc, "rpvoid": rpvoid, "trivia": trivia, "triviascore": triviascore}
#        f = open("rp","wb")
#        pickle.dump(rpdict,f)
#        f.close()
#updates pickled file

@bot.command()
async def whatis(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.author.id == "154552600073601024":
        arg = arg.split(',')
        if len(arg) == 2:
            index = channelindex(arg[1])
            await ctx.send(globals()[arg[0]][index])
#returns specific value

#@bot.command()
#async def owf(ctx, *, arg):
#    if ctx.author.id == "154552600073601024":
#        owf = ctx.channel.overwrites_for(arg)
#        await ctx.send(owf)
#checks overrides

@bot.command()
async def replace(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.author.id == "154552600073601024":
        arg = arg.split(',')
        if arg[0] == "trivia" or arg[0] == "triviascore":
            if len(arg) == 2:
                arg[1] = ast.literal_eval(arg[1])
                globals()[arg[0]] = arg[1]
                await ctx.send("Replace successful.")
                return
        if len(arg) == 3:
            index = channelindex(arg[1])
            arg[2] = ast.literal_eval(arg[2])
            if arg[0] == "rphost":
                arg[2] = idToString(arg[2])
            if not arg[0] == "rpvoid":
                globals()[arg[0]][index] = arg[2]
        else:
            await ctx.send("Please use .listreplace instead.")
            return
        await ctx.send("Replace successful.")
#replaces specific value

@bot.command()
async def arr(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.author.id == 154552600073601024:
        await ctx.send(rp)
        await ctx.send(rpstarted)
        await ctx.send(rptimestarted)
        await ctx.send(rphost)
        await ctx.send(rpdoc)
        await ctx.send(rpvoid)
        await ctx.send(trivia)
        await ctx.send(triviascore)
#returns values for listreplace

@bot.command()
async def listreplace(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.author.id == "154552600073601024":
        arg = arg.split(',',1)
        if len(arg) == 2 or arg[0] == "rpvoid":
            await ctx.send(arg[0])
            await ctx.send(arg[1])
            replacelist = ast.literal_eval(arg[1])
            if arg[0] == "rphost":
                replacelist = list(map(idToString,replacelist))
            globals()[arg[0]] = replacelist
            await ctx.send("Replace successful.")
#replaces list values for rp/rpstarted/rptimestarted/rphost/rpdoc

@bot.command(aliases=["dice"])
async def roll(ctx,num):
    if len(num.split("d")) == 2:
        d = num.split("d")
        rolls = 0
        maxrolls = d[0]
        maxrolls = int(maxrolls)
        if maxrolls > 20:
            maxrolls = 20
        num = d[1]
        num = int(num)
        text = "number"
        while rolls < maxrolls:
            if rolls == 0:
                text = str(random.randint(1,num))
            else:
                text = text + ", " + str(random.randint(1,num))
            rolls = rolls + 1
    else:
        if isinstance(int(num), int):
            text = random.randint(1,int(num))
        else:
            return
    embed = discord.Embed(title=text)
    await ctx.send(embed=embed)

@bot.command(aliases=["choose"])
async def pick(ctx, *, arg):
    args = arg.split(",")
    if len(args) == 1:
        embed = discord.Embed(title="Please provide more than one choice.")
        await ctx.send(embed=embed)
        return
    if len(args) > 10:
        embed = discord.Embed(title="Please provide less than ten options.")
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title=random.choice(args))
    await ctx.send(embed=embed)

@bot.command(aliases=["rpset"])
@commands.has_any_role("Staff","Trusted","Host")
async def setrp(ctx,*,roleplay):
    global rp
    global rpstarted
    index = channelindex(ctx.channel.name)
    if "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:    
        if not rphost[index] == ctx.author.id:
            return
    rp[index] = roleplay
#    updaterpdict("rp",rp)
    embed = discord.Embed(title="The RP was set to "+str(roleplay)+". Use .start to start the RP.")
    if rpstarted[index]:
        embed = discord.Embed(title="The RP was set to "+str(roleplay)+".")
    role = discord.utils.get(ctx.guild.roles, name="Regular")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages=None
    await ctx.channel.set_permissions(role,overwrite=overwrite)
    await ctx.send(embed=embed)
#    await ctx.send("?unlock <#"+ctx.channel.id+"> reason")

@bot.command(aliases=["startrp","rpstart"])
@commands.has_any_role("Staff","Trusted","Host")
async def start(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    index = channelindex(ctx.channel.name)
    if "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:    
        if not rphost[index] == ctx.author.id:
            return
    if rp[index] == None:
        embed = discord.Embed(title="No RP has been set.")
        await ctx.send(embed=embed)
        return
    if rpstarted[index]:
        embed = discord.Embed(title="The RP has already started.")
        await ctx.send(embed=embed)
        return
    rpstarted[index] = True
#    updaterpdict("rpstarted",rpstarted)
    rptimestarted[index] = time.time()
#    updaterpdict("rptimestarted",rptimestarted)
    if index == 0:
        rprolename = "Official RP"
    else:
        if index == 1:
            rprolename = "Rusty RP"
        else:
            rprolename = "Custom RP"
    embed = discord.Embed(title="The RP has started.",description="Remember to check the pinned messages to get the \"In the "+rprolename+"\" role!")
    await ctx.send(embed=embed)

@bot.command(aliases=["rp","arpee","host","doc"])
async def roleplay(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    index = channelindex(ctx.channel.name)
    if ctx.channel.name == "freeroam":
        embed = discord.Embed(title="The RP is Freeroam.")
        await ctx.send(embed=embed)
        return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await ctx.send(embed=embed)
        return
    if not rpstarted[index]:
        embed = discord.Embed(title="The RP is "+str(rp[index])+". Use .start to start the RP.")
    else:
        embed = discord.Embed(title="The RP is "+str(rp[index])+".",description="In progress for: "+toTime(time.time()-rptimestarted[index]))
    if not rphost[index] == None:
        embed.add_field(name="Host:",value=ctx.guild.get_member(rphost[index]).name)
    if not rpdoc[index] == None:
        embed.add_field(name="Doc:",value=rpdoc[index],inline=False)
    await ctx.send(embed=embed)

#@bot.command()
#async def void(ctx):
#    global rpstarted
#    global rpvoid
#    index = channelindex(ctx.channel.name)
#    if not rpstarted[index]:
#        if not rpvoid[2*index+1] == None:
#            if not rpvoid[2*index] == None:
#                embed = discord.Embed(title="Void: "+rpvoid[2*index+1]+", "+rpvoid[2*index])
#            else:
#                embed = discord.Embed(title="Void: "+rpvoid[2*index+1])
#        else:
#            embed = discord.Embed(title="No RPs are void.")
#        await ctx.send(embed=embed)

#@bot.command(aliases=["vr"])
#@commands.has_any_role("Staff","Trusted")
#async def voidreset(ctx):
#    global rpstarted
#    global rpvoid
#    index = channelindex(ctx.channel.name)
#    if not rpstarted[index]:
#        rpvoid[2*index+1] = None
#        rpvoid[2*index] = None
#        embed = discord.Embed(title="Void reset successful.")
#        await ctx.send(embed=embed)

#@bot.command(aliases=["sv"])
#@commands.has_any_role("Staff","Trusted")
#async def setvoid(ctx,*,arg):
#    global rpstarted
#    global rpvoid
#    index = channelindex(ctx.channel.name)
#    if not rpstarted[index]:
#        arg = arg.split(",")
#        if not len(arg) == 2:
#            embed = discord.Embed(title="Invalid number of arguments.")
#            await ctx.send(embed=embed)
#        rpvoid[2*index] = arg[0]
#        rpvoid[2*index+1] = arg[1]
#        embed = discord.Embed(title="The void has been set to "+rpvoid[2*index]+" and "+rpvoid[2*index+1]+".")
#        await ctx.send(embed=embed)

@bot.command(aliases=["rpend"])
@commands.has_any_role("Staff","Trusted","Host")
async def endrp(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    index = channelindex(ctx.channel.name)
    if "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:    
        if not rphost[index] == ctx.author.id:
            return
    role = discord.utils.get(ctx.guild.roles, name="Host")
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await ctx.send(embed=embed)
        return
    if not rpstarted[index]:
        embed = discord.Embed(title="The RP has ended.")
    else:
        embed = discord.Embed(title="The RP has ended.",description="After "+toTime(time.time()-rptimestarted[index]))
#    if rpstarted[index]:
#        if time.time()-rptimestarted[index] >= 900:
#            rpvoid[2*index] = rpvoid[2*index+1]
#            rpvoid[2*index+1] = rp[index]
#    if not rpvoid[2*index+1] == None:
#        if not rpvoid[2*index] == None:
#            embed.add_field(name="Void:",value=rpvoid[2*index+1]+", "+rpvoid[2*index])
#        else:
#            embed.add_field(name="Void:",value=rpvoid[2*index+1])
    rp[index] = None
#    updaterpdict("rp",rp)
    rpstarted[index] = False
#    updaterpdict("rpstarted",rpstarted)
    rptimestarted[index] = None
#    updaterpdict("rptimestarted",rptimestarted)
    if not rphost[index] == None:
        host = ctx.guild.get_member(rphost[index])
        if "Host" in [y.name for y in host.roles]:
            await host.remove_roles(role)
    rphost[index] = None
#    updaterpdict("rphost",rphost)
    rpdoc[index] = None
#    updaterpdict("rpdoc",rpdoc)
    role = discord.utils.get(ctx.guild.roles, name="Regular")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await ctx.channel.set_permissions(role,overwrite=overwrite)
    await ctx.send(embed=embed)
#    await ctx.send("?lock <#"+ctx.channel.id+">")

@bot.command(aliases=["sh"])
@commands.has_any_role("Staff","Trusted","Host")
async def sethost(ctx,user:discord.Member):
    global rp
    global rphost
    index = channelindex(ctx.channel.name)
    role = discord.utils.get(ctx.guild.roles, name="Host")
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await ctx.send(embed=embed)
        return
    if not rphost[index] == None:
        host = ctx.guild.get_member(rphost[index])
        if role.id in [y.id for y in host.roles]:
            await host.remove_roles(role)
    rphost[index] = user.id
#    updaterpdict("rphost",rphost)
    await user.add_roles(role)
    embed = discord.Embed(title="The host has been set to "+user.display_name+".")
    await ctx.send(embed=embed)

@bot.command(aliases=["sd"])
@commands.has_any_role("Staff","Trusted","Host")
async def setdoc(ctx, *, doc):
    global rp
    global rphost
    global rpdoc
    index = channelindex(ctx.channel.name)
    if "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:    
        if not rphost[index] == ctx.author.id:
            return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await ctx.send(embed=embed)
        return
    doc = str(doc)
    rpdoc[index] = doc
#    updaterpdict("rpdoc",rpdoc)
    embed = discord.Embed(title="The doc has been set to "+doc+".")
    await ctx.send(embed=embed)

@bot.command(aliases=["rmd","rmdoc"])
@commands.has_any_role("Staff","Trusted","Host")
async def removedoc(ctx):
    global rp
    global rpdoc
    global rphost
    index = channelindex(ctx.channel.name)
    if "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:    
        if not rphost[index] == ctx.author.id:
            return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await ctx.send(embed=embed)
        return
    if rpdoc[index] == None:
        embed = discord.Embed(title="There is no doc.")
        await ctx.send(embed=embed)
        return
    rpdoc[index] = None
#    updaterpdict("rpdoc",rpdoc)
    embed = discord.Embed(title="The doc has been removed.")
    await ctx.send(embed=embed)

#@bot.command(aliases=["starttrivia","ts","st"])
#@commands.has_any_role("Staff","Trusted")
#async def triviastart(ctx):
#    global trivia
#    global triviascore
#    if ctx.channel.name != "game-corner":
#       embed = discord.Embed(title="This command only works in the Trivia room.")
#        await ctx.send(embed=embed)
#        return
#    if trivia == True:
#        embed = discord.Embed(title="Trivia has already started.")
#        await ctx.send(embed=embed)
#        return
#    trivia = True
#    triviascore = {
#        "lastuser":None,
#        "streak":0
#    }
#    overwrite = discord.PermissionOverwrite()
#    overwrite.send_messages = None
#    role = discord.utils.get(ctx.guild.roles, name="Regular")
#    await bot.edit_channel_permissions(ctx.channel,role,overwrite)
#    embed = discord.Embed(title="Trivia has started.")
#    updaterpdict("trivia",trivia)
#    updaterpdict("triviascore",triviascore)
#    await ctx.send(embed=embed)

#@bot.command(aliases=["answertrivia","at","ta"])
#@commands.has_any_role("Staff","Trusted")
#async def triviaanswer(ctx,user:discord.Member):
#    global trivia
#    global triviascore
#    if ctx.channel.name != "game-corner":
#        embed = discord.Embed(title="This command only works in the Trivia room.")
#        await ctx.send(embed=embed)
#        return
#    if trivia == False:
#        embed = discord.Embed(title="Trivia is not running.")
#        await ctx.send(embed=embed)
#        return
#    if user.id in triviascore:
#        triviascore[user.id] += 1
#    else:
#        triviascore[user.id] = 1
#    if triviascore["lastuser"] == user.id:
#        triviascore["streak"] += 1
#    else:
#        triviascore["lastuser"] = user.id
#        triviascore["streak"] = 1
#    embed = discord.Embed(title="The point has been awarded to "+user.name+".")
#    await ctx.send(embed=embed)
#    await updatetriviarole(user,ctx.guild)
#    embed = discord.Embed(title="Scoreboard")
#    for k in sorted(triviascore,key=itemgetter(1)):
#        if k != "lastuser" and k != "streak":
#            name = discord.utils.get(ctx.guild.members,id=k)
#            score = triviascore[k]
#            embed.add_field(name=name,value=score,inline=False)
#    updaterpdict("triviascore",triviascore)
#    await ctx.send(embed=embed)

#@bot.command(aliases=["sb"])
#@commands.has_any_role("Staff","Trusted")
#async def scoreboard(ctx):
#    global trivia
#    global triviascore
#    if ctx.channel.name != "game-corner":
#        embed = discord.Embed(title="This command only works in the Trivia room.")
#        await ctx.send(embed=embed)
#        return
#    if trivia == False:
#        embed = discord.Embed(title="Trivia is not running.")
#        await ctx.send(embed=embed)
#        return
#    tempts = triviascore
#    del tempts["lastuser"]
#    del tempts["streak"]
#    embed = discord.Embed(title="Scoreboard")
#    for k in sorted(triviascore,key=itemgetter(1)):
#        if k != "lastuser" and k != "streak":
#            name = discord.utils.get(ctx.guild.members,id=k)
#            score = triviascore[k]
#            embed.add_field(name=name,value=score,inline=False)
#    await ctx.send(embed=embed)

#@bot.command(aliases=["endtrivia","te","et"])
#@commands.has_any_role("Staff","Trusted")
#async def triviaend(ctx):
#    global trivia
#    global triviascore
#    if ctx.channel.name != "game-corner":
#        embed = discord.Embed(title="This command only works in the Trivia room.")
#        await ctx.send(embed=embed)
#        return
#    if trivia == False:
#        embed = discord.Embed(title="Trivia is not running.")
#        await ctx.send(embed=embed)
#        return
#    embed2 = discord.Embed(title="Scoreboard")
#    for k in sorted(triviascore,key=itemgetter(1)):
#        if k != "lastuser" and k != "streak":
#            name = discord.utils.get(ctx.guild.members,id=k)
#            score = triviascore[k]
#            embed2.add_field(name=name,value=score,inline=False)
#    trivia = False
#    triviascore = {
#        "lastuser":None,
#        "streak":0
#    }
#    overwrite = discord.PermissionOverwrite()
#    overwrite.send_messages = False
#    role = discord.utils.get(ctx.guild.roles, name="Regular")
#    await bot.edit_channel_permissions(ctx.channel,role,overwrite)
#    embed = discord.Embed(title="Trivia has ended.")
#    updaterpdict("trivia",trivia)
#    updaterpdict("triviascore",triviascore)
#    await ctx.send(embed=embed)
#    await ctx.send(embed=embed2)

@bot.command(aliases=["rpr","roleplayreviewer"])
@commands.has_any_role("Host")
async def roleplayreview(ctx):
    global rp
    global rpr
    global rprmember
    global rphost
    index = channelindex(ctx.channel.name)
    if rpr:
        embed = discord.Embed(title="Please wait for RPR to end before using it again.")
        await ctx.send(embed=embed)
        return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await ctx.send(embed=embed)
        return
    if rphost[index] == None:
        embed = discord.Embed(title="There is no host.")
        await ctx.send(embed=embed)
        return
    rprmember = ctx.guild.get_member(rphost[index])
    rpr = True
    embed = discord.Embed(title="Roleplay review is now active. For the next 10 minutes, messages to the bot will be forwarded to the host anonymously.",description="Note that messages sent to the bot during Roleplay Review are subject to the rules of the server and logged for moderation purposes.")
    await ctx.send(embed=embed)
    await asyncio.sleep(600)
    rprmember = None
    rpr = False
    embed = discord.Embed(title="Roleplay Review has ended.")
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    global rpr
    global rprmember
    if rpr:
        channel = bot.get_channel(461290964384874507)
        if message.guild is None and message.author != bot.user:
            embed = discord.Embed(title="RPR: "+message.author.name+"("+str(message.author.id)+")"+" to "+rprmember.name+"("+str(rprmember.id)+")",description=message.content)
            await channel.send(embed=embed)
            await rprmember.send(message.content)
    await bot.process_commands(message)

@bot.command(aliases=["conquestset","setcq","cqset"])
@commands.has_any_role("Staff","Trusted")
async def setconquest(ctx):
    global rp
    global cq
    global cqrequests
    global alliances
    global allyrequests
    global knightrequests
    index = channelindex(ctx.channel.name)
    if "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:    
        if not rphost[index] == ctx.author.id:
            return
    if not rp[index] == None:
        embed = discord.Embed(title="Please end the current roleplay before setting Conquest.")
        await ctx.send(embed=embed)
        return
    if "Conquest" in rp:
        embed = discord.Embed(title="Conquest is running elsewhere. Please end it before setting Conquest.")
        await ctx.send(embed=embed)
        return
    rp[index] = "Conquest"
    clearcq()
    embed = discord.Embed(title="The RP was set to Conquest. Use .start to start the RP, and .claim type to claim a type.",description="See https://pastebin.com/n0ZGwamQ for the full list of commands.")
    await ctx.send(embed=embed)

@bot.command(aliases=["playerlist"])
async def types(ctx):
    global rp
    global cq
    global alliances
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="Conquest Playerlist")
    for x in cq:
        if not cq[x][0] == None:
            if cq[x][3] == None:
                knights = "\u200b"
                if not cq[x][1] == None:
                    if not cq[x][2] == None:
                        knights = x.capitalize()+" Knights: "+ctx.guild.get_member(cq[x][1]).name+", "+ctx.guild.get_member(cq[x][2]).name
                    else:
                        knights = x.capitalize()+" Knight: "+ctx.guild.get_member(cq[x][1]).name
                embed.add_field(name="**"+x.capitalize()+": "+ctx.guild.get_member(cq[x][0]).name+"**",value=knights,inline=True)
            else:
                for y in cq:
                    if cq[y][0] == cq[x][3]:
                        conquerortype = y
                embed.add_field(name="**"+x.capitalize()+": "+ctx.guild.get_member(cq[x][0]).name+" (conquered by "+conquerortype.capitalize()+")**",value="\u200b",inline=True)
# i know the alliances code for .types is particularly bad, but i'm way too lazy to fix it, and it works (or at least it should)
    g = {None}
    alliancelist = "\u200b"
    for z in alliances:
        if z in g:
            continue
        if not alliances[z] == {None}:
            ally1 = None
            ally2 = None
            for h in alliances[z]:
                if h == None:
                    continue
                g.add(h)
                if ally1 == None:
                    ally1 = h
                else:
                    ally2 = h
            if ally2 == None:
                if alliancelist == "\u200b":
                    alliancelist = z.capitalize()+", "+ally1.capitalize()
                else:
                    alliancelist = alliancelist + " | " + z.capitalize()+", "+ally1.capitalize()
            else:
                if alliancelist == "\u200b":
                    alliancelist = z.capitalize()+", "+ally1.capitalize()+", "+ally2.capitalize()
                else:
                    alliancelist = alliancelist + " | " + z.capitalize()+", "+ally1.capitalize()+", "+ally2.capitalize()
    embed.add_field(name="**Alliances:**",value=alliancelist,inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def claim(ctx,type1):
    global rp
    global cq
    index = channelindex(ctx.channel.name)
    type1 = str(type1)
    type1 = type1.lower()
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    for x in cq:
        if cq[x][0] == ctx.author.id:
            embed = discord.Embed(title=ctx.author.name+" already claims a type. Please use .unclaim before claiming another type.")
            await ctx.send(embed=embed)
            return
        if ctx.author.id in cq[x]:
            embed = discord.Embed(title=ctx.author.name+" already has a role.")
            await ctx.send(embed=embed)
            return
    if not cq[type1][0] == None:
        embed = discord.Embed(title=type1.capitalize()+" is already claimed.")
        await ctx.send(embed=embed)
        return
    cq[type1][0] = ctx.author.id
    embed = discord.Embed(title=ctx.author.name+" has claimed "+type1.capitalize()+".")
    await ctx.send(embed=embed)
    return

@bot.command()
async def knight(ctx,type1):
    global rp
    global cq
    global knightrequests
    index = channelindex(ctx.channel.name)
    type1 = str(type1)
    type1 = type1.lower()
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    if cq[type1][0] == None:
        embed = discord.Embed(title=type1.capitalize()+" is not claimed.")
        await ctx.send(embed=embed)
        return
    for x in cq:
        if cq[x][0] == ctx.author.id and cq[x][3] == None:
            embed = discord.Embed(title=ctx.author.name+" already claims a type. Please use .unclaim before knighting.")
            await ctx.send(embed=embed)
            return
        if ctx.author.id in cq[x] and not cq[x][3] == ctx.author.id:
            embed = discord.Embed(title=ctx.author.name+" already has a role. Please use .unclaim before knighting.")
            await ctx.send(embed=embed)
            return
    if not cq[type1][1] == None and not cq[type1][2] == None:
        embed = discord.Embed(title=type1.capitalize()+" has too many Knights.")
        await ctx.send(embed=embed)
        return
    if not knightrequests[type1] == None:
        await ctx.send("A previous knight request ("+ctx.guild.get_member(knightrequests[type1]).name+") has been overwritten.")
    knightrequests[type1] = ctx.author.id
    embed = discord.Embed(title=ctx.author.name+" has requested to knight for "+type1.capitalize()+". Use .confirmknight to confirm.")
    await ctx.send(embed=embed)
    return

@bot.command(aliases=["cknight"])
async def confirmknight(ctx):
    global rp
    global cq
    global knightrequests
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    type1 = None
    for x in cq:
        if cq[x][0] == ctx.author.id:
            type1 = x
    if type1 == None:
        embed = discord.Embed(title="User cannot accept Knights.")
        await ctx.send(embed=embed)
        return
    if not cq[type1][3] == None:
        embed = discord.Embed(title="User is conquered.")
        await ctx.send(embed=embed)
        return
    if knightrequests[type1] == None:
        embed = discord.Embed(title=type1.capitalize()+" has not received any Knight requests.")
        await ctx.send(embed=embed)
        return
    if cq[type1][1] == None:
        cq[type1][1] = knightrequests[type1]
        knightrequests[type1] = None
        embed = discord.Embed(title=ctx.guild.get_member(cq[type1][1]).name+" has become a "+type1.capitalize()+" Knight!")
        await ctx.send(embed=embed)
    else:
        cq[type1][2] = knightrequests[type1]
        knightrequests[type1] = None
        embed = discord.Embed(title=ctx.guild.get_member(cq[type1][2]).name+" has become a "+type1.capitalize()+" Knight!")
        await ctx.send(embed=embed)

@bot.command(aliases=["rmknights","rmknight","removeknight","clearknights"])
async def removeknights(ctx):
    global rp
    global cq
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    type1 = None
    for x in cq:
        if cq[x][0] == ctx.author.id:
            type1 = x
    if type1 == None:
        embed = discord.Embed(title="User cannot remove Knights.")
        await ctx.send(embed=embed)
        return
    if not cq[type1][3] == None:
        embed = discord.Embed(title="User is conquered.")
        await ctx.send(embed=embed)
        return
    if cq[type1][1] == None and cq[type1][2] == None:
        embed = discord.Embed(title="User has no Knights.")
        await ctx.send(embed=embed)
        return
    if not cq[type1][1] == None:
        await ctx.send(ctx.guild.get_member(cq[type1][1]).name+" is no longer a "+type1.capitalize()+" Knight.")
        cq[type1][1] = None
    if not cq[type1][2] == None:
        await ctx.send(ctx.guild.get_member(cq[type1][2]).name+" is no longer a "+type1.capitalize()+" Knight.")
        cq[type1][2] = None
    embed = discord.Embed(title=type1.capitalize()+" Knights cleared successfully.")
    await ctx.send(embed=embed)

@bot.command()
async def unclaim(ctx):
    global rp
    global cq
    global cqrequests
    global alliances
    global allyrequests
    global knightrequests
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    for x in cq:
        if cq[x][0] == ctx.author.id and cq[x][3] == None:
            cq[x] = [None, None, None, None, None]
            embed = discord.Embed(title=ctx.author.name+" is no longer "+x.capitalize()+".")
            for y in cq:
                if cq[y][3] == ctx.author.id:
                    cq[y][3] = None
                    await ctx.send(y.capitalize()+" has been opened.")
                if y in alliances[x]:
                    alliances[x].discard(y)
                    alliances[x].add(None)
                    alliances[y].discard(x)
                    alliances[y].add(None)
                    await ctx.send(y.capitalize()+" is no longer allied with "+x.capitalize()+".")
            cqrequests[x] = None
            allyrequests[x] = None
            knightrequests[x] = None
            for z in cq:
                if cqrequests[z] == x:
                    cqrequests[z] = None
                if allyrequests[z] == x:
                    allyrequests[z] = None
            await ctx.send(embed=embed)
            return
        if cq[x][1] == ctx.author.id or cq[x][2] == ctx.author.id:
            if cq[x][1] == ctx.author.id:
                cq[x][1] = cq[x][2]
                cq[x][2] = None
            else:
                cq[x][2] = None
            embed = discord.Embed(title=ctx.author.name+" is no longer a "+x.capitalize()+" knight.")
            await ctx.send(embed=embed)
            return
        if cq[x][0] == ctx.author.id and not cq[x][3] == None:
            embed = discord.Embed(title="Cannot use .unclaim while conquered.")
            await ctx.send(embed=embed)
            return
    embed = discord.Embed(title="No role to unclaim.")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role("Staff","Trusted")
async def forceclear(ctx,type1):
    global rp
    global cq
    global cqrequests
    global alliances
    global allyrequests
    type1 = str(type1)
    type1 = type1.lower()
    if type1 in cq:
        conqueror = cq[type1][0]
        spoils = None
        for x in cq:
            if cq[x][3] == conqueror:
                cq[x][3] = None
                if spoils == None:
                    spoils = x.capitalize()
                else:
                    spoils = spoils+", "+x.capitalize()
                await ctx.send("Force clear conquests successful for: "+spoils+".")
        allies = None
        for y in cq:
            if type1 in alliances[y]:
                if len(alliances[y]) == 1:
                    alliances[y].add(None)
                alliances[y].remove(type1)
                if allies == None:
                    allies = y.capitalize()
                else:
                    allies = allies+", "+y.capitalize()
        alliances[type1] = {None}
        if not allies == None:
            await ctx.send("Force clear alliances successful for: "+allies+".")
        cq[type1] = [None, None, None, None, None]
        cqrequests[type1] = None
        allyrequests[type1] = None
        for z in cq:
            if cqrequests[z] == type1:
                cqrequests[z] = None
            if allyrequests[z] == type1:
                allyrequests[z] = None
        await ctx.send("Force clear successful.")

@bot.command()
@commands.has_any_role("Staff","Trusted")
async def forceclearconquests(ctx,type1):
    global rp
    global cq
    type1 = str(type1)
    type1 = type1.lower()
    if type1 in cq:
        conqueror = cq[type1][0]
        spoils = None
        for x in cq:
            if cq[x][3] == conqueror:
                cq[x][3] = None
                if spoils == None:
                    spoils = x.capitalize()
                else:
                    spoils = spoils+", "+x.capitalize()
                await ctx.send("Force clear conquests successful for: "+spoils+".")

@bot.command(aliases=["conquer","cq"])
async def conquest(ctx,type1):
    global rp
    global cq
    global cqrequests
    type1 = str(type1)
    type1 = type1.lower()
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    if cq[type1][0] == None:
        embed = discord.Embed(title=type1.capitalize()+" is not claimed.")
        await ctx.send(embed=embed)
        return
    if not cq[type1][3] == None:
        embed = discord.Embed(title=type1.capitalize()+" is already conquered.")
        await ctx.send(embed=embed)
        return
    for x in cq:
        if cq[x][0] == ctx.author.id and cq[x][3] == None:
            if x == type1:
                await ctx.send(x.capitalize()+" cannot conquer itself.")
                return
            if not cqrequests[x] == None:
                await ctx.send("A previous unconfirmed conquest ("+cqrequests[x]+") has been cleared.")
            cqrequests[x] = type1
            embed = discord.Embed(title=x.capitalize()+' has conquered '+type1.capitalize()+'! Use ".confirmcq '+x+'" to confirm.')
            await ctx.send(embed=embed)
            return
        if cq[x][1] == ctx.author.id or cq[x][2] == ctx.author.id:
            if x == type1:
                await ctx.send(x.capitalize()+" cannot conquer itself.")
                return
            if not cqrequests[x] == None:
                await ctx.send("A previous unconfirmed conquest ("+cqrequests[x]+") has been cleared.")
            cqrequests[x] = type1
            embed = discord.Embed(title=x.capitalize()+' has conquered '+type1.capitalize()+'! Use ".confirmcq '+x+'" to confirm.')
            await ctx.send(embed=embed)
            return
#        if cq[x][4] == ctx.author.id:
#            for y in cq:
#                if cq[y][0] == cq[x][3]:
#                    if not cqrequests[y] == None:
#                        await ctx.send("A previous unconfirmed conquest ("+cqrequests[y]+") has been cleared.")
#                    cqrequests[y] = type1
#                    embed = discord.Embed(title=x.capitalize()+' has conquered '+type1.capitalize()+'! Use ".confirmcq '+x+'"to confirm.')
#                    await ctx.send(embed=embed)
#                    return
# scrapped vassal functionality for .confirmconquest
    await ctx.send("User cannot use .conquest.")
    
@bot.command(aliases=["confirmcq"])
async def confirmconquest(ctx,type1):
    global rp
    global cq
    global cqrequests
    type1 = str(type1)
    type1 = type1.lower()
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    type2 = None
    for x in cq:
        if cq[x][0] == ctx.author.id:
            type2 = x
    if type2 == None and "Staff" not in [y.name for y in ctx.author.roles] and "Trusted" not in [y.name for y in ctx.author.roles]:
        embed = discord.Embed(title="User cannot confirm conquest.")
        await ctx.send(embed=embed)
        return
    if "Staff" in [y.name for y in ctx.author.roles] or "Trusted" in [y.name for y in ctx.author.roles]:
        type2 = cqrequests[type1]
    if not cqrequests[type1] == type2:
        embed = discord.Embed(title=type1.capitalize()+' has not used ".conquest '+type2+'".')
        await ctx.send(embed=embed)
        return
    cqrequests[type1] = None
    cq[type2][3] = cq[type1][0]
    if not cq[type2][1] == None and not cq[type2][2] == None:
        await ctx.send(type2.capitalize()+" Knights have been removed.")
        cq[type2][1] = None
        cq[type2][2] = None
    conquesttransfer = False
    for z in cq:
        if cq[z][3] == cq[type2][0]:
            cq[z][3] = cq[type1][0]
            conquesttransfer = True
    if conquesttransfer:
        await ctx.send(type2.capitalize()+"'s conquests have been transferred to "+type1.capitalize()+".")
    embed = discord.Embed(title=type2.capitalize()+" has been conquered by "+type1.capitalize()+"!")
    await ctx.send(embed=embed)

@bot.command(aliases=["ally","requestally","requestalliance"])
async def formalliance(ctx,type1):
    global rp
    global cq
    global alliances
    global allyrequests
    type1 = str(type1)
    type1 = type1.lower()
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    if cq[type1][0] == None:
        embed = discord.Embed(title=type1.capitalize()+" is not claimed.")
        await ctx.send(embed=embed)
        return
    for x in cq:
        if cq[x][0] == ctx.author.id:
            if x == type1:
                await ctx.send(x.capitalize()+" cannot ally with itself.")
                return
            allycount1 = 0
            allycount2 = 0
            for y in alliances:
                if x in alliances[y]:
                    allycount1 += 1
                if type1 in alliances[y]:
                    allycount2 += 1
            if allycount1 == 2:
                await ctx.send(x.capitalize()+" has too many allies.")
                return
            if allycount2 == 2:
                await ctx.send(type1.capitalize()+" has too many allies.")
                return
            if not allyrequests[x] == None:
                await ctx.send("A previous unconfirmed alliance request ("+allyrequests[x]+") has been cleared.")
            allyrequests[x] = type1
            embed = discord.Embed(title=x.capitalize()+' has offered to ally with '+type1.capitalize()+'! Use ".confirmally '+x+'" to confirm.')
            await ctx.send(embed=embed)
            return
    await ctx.send("User cannot use .formalliance.")

@bot.command(aliases=["confirmally"])
async def confirmalliance(ctx,type1):
    global rp
    global cq
    global alliances
    global allyrequests
    type1 = str(type1)
    type1 = type1.lower()
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    type2 = None
    for x in cq:
        if cq[x][0] == ctx.author.id:
            type2 = x
    if type2 == None:
        embed = discord.Embed(title="User cannot confirm alliance.")
        await ctx.send(embed=embed)
        return
    if not allyrequests[type1] == type2:
        embed = discord.Embed(title=type1.capitalize()+' has not used ".formalliance '+type2+'".')
        await ctx.send(embed=embed)
        return
    allycount1 = 0
    allycount2 = 0
    for y in alliances:
        if type1 in alliances[y]:
            allycount1 += 1
        if type2 in alliances[y]:
            allycount2 += 1
    if allycount1 == 2:
        await ctx.send(type1.capitalize()+" has too many allies.")
        return
    if allycount2 == 2:
        await ctx.send(type2.capitalize()+" has too many allies.")
        return
    zally = False
    ztype = None
    for z in alliances:
        if type2 in alliances[z]:
            if None in alliances[z]:
                alliances[z].remove(None)
            alliances[z].add(type1)
            ztype = z
            zally = True
    allyrequests[type1] = None
    if None in alliances[type1]:
        alliances[type1].remove(None)
    alliances[type1].add(type2)
    if None in alliances[type2]:
        alliances[type2].remove(None)
    alliances[type2].add(type1)
    embed = discord.Embed(title=type2.capitalize()+" has allied with "+type1.capitalize()+"!")
    if zally:
        await ctx.send(type1.capitalize()+" has also allied with "+ztype.capitalize()+".")
    await ctx.send(embed=embed)

@bot.command(aliases=["free"])
async def freeally(ctx,type1):
    global rp
    global cq
    global alliances
    global allyrequests
    type1 = str(type1)
    type1 = type1.lower()
    index = channelindex(ctx.channel.name)
    if not rp[index] == "Conquest":
        embed = discord.Embed(title="There is no Conquest running.")
        await ctx.send(embed=embed)
        return
    if type1 not in cq:
        embed = discord.Embed(title=type1.capitalize()+" is not a valid type.")
        await ctx.send(embed=embed)
        return
    type2 = None
    for x in cq:
        if cq[x][0] == ctx.author.id:
            type2 = x
    if type2 == None:
        embed = discord.Embed(title="User cannot free ally.")
        await ctx.send(embed=embed)
        return
    if cq[type1][3] == None:
        embed = discord.Embed(title=type1.capitalize()+" has not been conquered.")
        await ctx.send(embed=embed)
        return
    if type1 not in alliances[type2]:
        embed = discord.Embed(title=type1.capitalize()+" is not allied with "+type2.capitalize()+".")
        await ctx.send(embed=embed)
        return
    if not cq[type2][0] == cq[type1][3]:
        embed = discord.Embed(title=type2.capitalize()+" has not reclaimed "+type1.capitalize()+".")
        await ctx.send(embed=embed)
        return
    cq[type1][3] = None
    for y in cq:
        if cq[y][1] == cq[type1][0]:
            cq[y][1] = cq[y][2]
            cq[y][2] = None
        if cq[y][2] == cq[type1][0]:
            cq[y][2] = None
    embed = discord.Embed(title=type2.capitalize()+" has freed "+type1.capitalize()+"!")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_any_role("Staff","Trusted")
async def forceclearalliances(ctx,type1):
    global rp
    global cq
    global alliances
    type1 = str(type1)
    type1 = type1.lower()
    if type1 in cq:
        allies = None
        for y in cq:
            if type1 in alliances[y]:
                if len(alliances[y]) == 1:
                    alliances[y].add(None)
                alliances[y].remove(type1)
                if allies == None:
                    allies = y.capitalize()
                else:
                    allies = allies+", "+y.capitalize()
        alliances[type1] = {None}
        if not allies == None:
            await ctx.send("Force clear alliances successful for: "+allies+".")

bot.run("insert token here")
#host role id is 461386257822384138