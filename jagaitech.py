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
    rplist = ['official-rp','rusty-rp','custom-rp']
    if arg in rplist:
        return rplist.index(arg)
#check channel

def createrpdict():
    f = open("rp","rb")
    rpdict = pickle.load(f)
    f.close
    return rpdict
#creates dictionary from pickled file

def updaterpdict(arg1,arg2):
    rpdict = createrpdict()
    rpdict[arg1] = arg2
    f = open("rp","wb")
    pickle.dump(rpdict,f)
    f.close()

async def updatetriviarole(arg,server):
    global triviascore
    role1 = discord.utils.get(server.roles, name="Trivia")
    role2 = discord.utils.get(server.roles, name="Trivia Knight")
    role3 = discord.utils.get(server.roles, name="Trivia Lord")
    role4 = discord.utils.get(server.roles, name="Trivia Nobleman")
    role5 = discord.utils.get(server.roles, name="Trivia King")
    if triviascore[arg.id] == 1:
        rolelist = [role1,role2,role3,role4,role5]
        intersection = [value for value in arg.roles if value in rolelist]
        if intersection == []:
            await bot.add_roles(arg,role1)
            return
    if triviascore["streak"] == 3:
        rolelist = [role2,role3,role4,role5]
        intersection = [value for value in arg.roles if value in rolelist]
        if intersection == []:
            await bot.remove_roles(arg,role1)
            await bot.add_roles(arg,role2)
            embed = discord.Embed(title=arg.name+" has reached "+role2.name+"!")
            await bot.say(embed=embed)
            return
    if triviascore["streak"] == 5:
        rolelist = [role3,role4,role5]
        intersection = [value for value in arg.roles if value in rolelist]
        if intersection == []:
            await bot.remove_roles(arg,role2)
            await bot.add_roles(arg,role3)
            embed = discord.Embed(title=arg.name+" has reached "+role3.name+"!")
            await bot.say(embed=embed)
            return
    if triviascore["streak"] == 8:
        rolelist = [role4,role5]
        intersection = [value for value in arg.roles if value in rolelist]
        if intersection == []:
            await bot.remove_roles(role3.id)
            await bot.add_roles(role4.id)
            embed = discord.Embed(title=arg.name+" has reached "+role4.name+"!")
            await bot.say(embed=embed)
            return
    if triviascore["streak"] == 10:
        if not role5 in arg.roles:
            await bot.remove_roles(role4.id)
            await bot.add_roles(role5.id)
            embed = discord.Embed(title=arg.name+" has reached "+role5.name+"!")
            await bot.say(embed=embed)
            return
    return

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
    f = open("rp","rb")
    rpdict = pickle.load(f)
    f.close
    rp = rpdict["rp"]
    rpstarted = rpdict["rpstarted"]
    rptimestarted = rpdict["rptimestarted"]
    rphost = rpdict["rphost"]
    rpdoc = rpdict["rpdoc"]
    rpvoid = rpdict["rpvoid"]
    trivia = rpdict["trivia"]
    triviascore = rpdict["triviascore"]
    rpr = False
    rprmember = None

@bot.command(pass_context=True)
async def rpdict(ctx):
    if ctx.message.author.id == "154552600073601024":
        rpdict = createrpdict()
        await bot.say(rpdict)
#returns pickled file

@bot.command(pass_context=True)
async def syncrpdict(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.message.author.id == "154552600073601024":
        rpdict = {"rp": rp, "rpstarted": rpstarted, "rptimestarted": rptimestarted, "rphost": rphost, "rpdoc": rpdoc, "rpvoid": rpvoid, "trivia": trivia, "triviascore": triviascore}
        f = open("rp","wb")
        pickle.dump(rpdict,f)
        f.close()
#updates pickled file

@bot.command(pass_context=True)
async def whatis(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.message.author.id == "154552600073601024":
        arg = arg.split(',')
        if len(arg) == 2:
            index = channelindex(arg[1])
            await bot.say(globals()[arg[0]][index])
#returns specific value

#@bot.command(pass_context=True)
#async def owf(ctx, *, arg):
#    if ctx.message.author.id == "154552600073601024":
#        owf = ctx.message.channel.overwrites_for(arg)
#        await bot.say(owf)
#checks overrides

@bot.command(pass_context=True)
async def replace(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.message.author.id == "154552600073601024":
        arg = arg.split(',')
        if arg[0] == "trivia" or arg[0] == "triviascore":
            if len(arg) == 2:
                arg[1] = ast.literal_eval(arg[1])
                globals()[arg[0]] = arg[1]
                await bot.say("Replace successful.")
                return
        if len(arg) == 3:
            index = channelindex(arg[1])
            arg[2] = ast.literal_eval(arg[2])
            if arg[0] == "rphost":
                arg[2] = idToString(arg[2])
            if not arg[0] == "rpvoid":
                globals()[arg[0]][index] = arg[2]
        else:
            await bot.say("Please use .listreplace instead.")
            return
        await bot.say("Replace successful.")
#replaces specific value

@bot.command(pass_context=True)
async def arr(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.message.author.id == "154552600073601024":
        await bot.say(rp)
        await bot.say(rpstarted)
        await bot.say(rptimestarted)
        await bot.say(rphost)
        await bot.say(rpdoc)
        await bot.say(rpvoid)
        await bot.say(trivia)
        await bot.say(triviascore)
#returns values for listreplace

@bot.command(pass_context=True)
async def listreplace(ctx, *, arg):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    global trivia
    global triviascore
    if ctx.message.author.id == "154552600073601024":
        arg = arg.split(',',1)
        if len(arg) == 2 or arg[0] == "rpvoid":
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
@commands.has_any_role("Staff","Trusted","Host")
async def setrp(ctx,*,roleplay):
    global rp
    global rpstarted
    index = channelindex(ctx.message.channel.name)
    if "Staff" not in [y.name for y in ctx.message.author.roles] and "Trusted" not in [y.name for y in ctx.message.author.roles]:    
        if not rphost[index] == ctx.message.author.id:
            return
    rp[index] = roleplay
    updaterpdict("rp",rp)
    embed = discord.Embed(title="The RP was set to "+str(roleplay)+". Use .start to start the RP.")
    if rpstarted[index]:
        embed = discord.Embed(title="The RP was set to "+str(roleplay)+".")
    role = discord.utils.get(ctx.message.server.roles, name="Regular")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages=None
    await bot.edit_channel_permissions(ctx.message.channel,role,overwrite)
    await bot.say(embed=embed)
#    await bot.say("?unlock <#"+ctx.message.channel.id+"> reason")

@bot.command(pass_context=True,aliases=["startrp","rpstart"])
@commands.has_any_role("Staff","Trusted","Host")
async def start(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    index = channelindex(ctx.message.channel.name)
    if "Staff" not in [y.name for y in ctx.message.author.roles] and "Trusted" not in [y.name for y in ctx.message.author.roles]:    
        if not rphost[index] == ctx.message.author.id:
            return
    if rp[index] == None:
        embed = discord.Embed(title="No RP has been set.")
        await bot.say(embed=embed)
        return
    if rpstarted[index]:
        embed = discord.Embed(title="The RP has already started.")
        await bot.say(embed=embed)
        return
    rpstarted[index] = True
    updaterpdict("rpstarted",rpstarted)
    rptimestarted[index] = time.time()
    updaterpdict("rptimestarted",rptimestarted)
    if index == 0:
        rprolename = "Official RP"
    else:
        if index == 1:
            rprolename = "Rusty RP"
        else:
            rprolename = "Custom RP"
    embed = discord.Embed(title="The RP has started.",description="Remember to check the pinned messages to get the \"In the "+rprolename+"\" role!")
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rp","arpee","host","doc"])
async def roleplay(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    index = channelindex(ctx.message.channel.name)
    if ctx.message.channel.name == "freeroam":
        embed = discord.Embed(title="The RP is Freeroam.")
        await bot.say(embed=embed)
        return
    if rp[index] == None:
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

#@bot.command(pass_context=True)
#async def void(ctx):
#    global rpstarted
#    global rpvoid
#    index = channelindex(ctx.message.channel.name)
#    if not rpstarted[index]:
#        if not rpvoid[2*index+1] == None:
#            if not rpvoid[2*index] == None:
#                embed = discord.Embed(title="Void: "+rpvoid[2*index+1]+", "+rpvoid[2*index])
#            else:
#                embed = discord.Embed(title="Void: "+rpvoid[2*index+1])
#        else:
#            embed = discord.Embed(title="No RPs are void.")
#        await bot.say(embed=embed)

#@bot.command(pass_context=True,aliases=["vr"])
#@commands.has_any_role("Staff","Trusted")
#async def voidreset(ctx):
#    global rpstarted
#    global rpvoid
#    index = channelindex(ctx.message.channel.name)
#    if not rpstarted[index]:
#        rpvoid[2*index+1] = None
#        rpvoid[2*index] = None
#        embed = discord.Embed(title="Void reset successful.")
#        await bot.say(embed=embed)

#@bot.command(pass_context=True,aliases=["sv"])
#@commands.has_any_role("Staff","Trusted")
#async def setvoid(ctx,*,arg):
#    global rpstarted
#    global rpvoid
#    index = channelindex(ctx.message.channel.name)
#    if not rpstarted[index]:
#        arg = arg.split(",")
#        if not len(arg) == 2:
#            embed = discord.Embed(title="Invalid number of arguments.")
#            await bot.say(embed=embed)
#        rpvoid[2*index] = arg[0]
#        rpvoid[2*index+1] = arg[1]
#        embed = discord.Embed(title="The void has been set to "+rpvoid[2*index]+" and "+rpvoid[2*index+1]+".")
#        await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rpend"])
@commands.has_any_role("Staff","Trusted","Host")
async def endrp(ctx):
    global rp
    global rpstarted
    global rptimestarted
    global rphost
    global rpdoc
    global rpvoid
    index = channelindex(ctx.message.channel.name)
    if "Staff" not in [y.name for y in ctx.message.author.roles] and "Trusted" not in [y.name for y in ctx.message.author.roles]:    
        if not rphost[index] == ctx.message.author.id:
            return
    role = get(ctx.message.server.roles, name="Host")
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await bot.say(embed=embed)
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
    updaterpdict("rp",rp)
    rpstarted[index] = False
    updaterpdict("rpstarted",rpstarted)
    rptimestarted[index] = None
    updaterpdict("rptimestarted",rptimestarted)
    if not rphost[index] == None:
        host = ctx.message.server.get_member(rphost[index])
        if "Host" in [y.name for y in host.roles]:
            await bot.remove_roles(host,role)
    rphost[index] = None
    updaterpdict("rphost",rphost)
    rpdoc[index] = None
    updaterpdict("rpdoc",rpdoc)
    role = discord.utils.get(ctx.message.server.roles, name="Regular")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel,role,overwrite)
    await bot.say(embed=embed)
#    await bot.say("?lock <#"+ctx.message.channel.id+">")

@bot.command(pass_context=True,aliases=["sh"])
@commands.has_any_role("Staff","Trusted","Host")
async def sethost(ctx,user:discord.Member):
    global rp
    global rphost
    index = channelindex(ctx.message.channel.name)
    role = get(ctx.message.server.roles, name="Host")
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await bot.say(embed=embed)
        return
    if not rphost[index] == None:
        host = ctx.message.server.get_member(rphost[index])
        if role.id in [y.id for y in host.roles]:
            await bot.remove_roles(host,role)
    rphost[index] = user.id
    updaterpdict("rphost",rphost)
    await bot.add_roles(user,role)
    embed = discord.Embed(title="The host has been set to "+user.display_name+".")
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sd"])
@commands.has_any_role("Staff","Trusted","Host")
async def setdoc(ctx, *, doc):
    global rp
    global rphost
    global rpdoc
    index = channelindex(ctx.message.channel.name)
    if "Staff" not in [y.name for y in ctx.message.author.roles] and "Trusted" not in [y.name for y in ctx.message.author.roles]:    
        if not rphost[index] == ctx.message.author.id:
            return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await bot.say(embed=embed)
        return
    doc = str(doc)
    rpdoc[index] = doc
    updaterpdict("rpdoc",rpdoc)
    embed = discord.Embed(title="The doc has been set to "+doc+".")
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["rmd","rmdoc"])
@commands.has_any_role("Staff","Trusted","Host")
async def removedoc(ctx):
    global rp
    global rpdoc
    global rphost
    index = channelindex(ctx.message.channel.name)
    if "Staff" not in [y.name for y in ctx.message.author.roles] and "Trusted" not in [y.name for y in ctx.message.author.roles]:    
        if not rphost[index] == ctx.message.author.id:
            return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await bot.say(embed=embed)
        return
    if rpdoc[index] == None:
        embed = discord.Embed(title="There is no doc.")
        await bot.say(embed=embed)
        return
    rpdoc[index] = None
    updaterpdict("rpdoc",rpdoc)
    embed = discord.Embed(title="The doc has been removed.")
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["starttrivia","ts","st"])
@commands.has_any_role("Staff","Trusted")
async def triviastart(ctx):
    global trivia
    global triviascore
    if ctx.message.channel.name != "game-corner":
        embed = discord.Embed(title="This command only works in the Trivia room.")
        await bot.say(embed=embed)
        return
    if trivia == True:
        embed = discord.Embed(title="Trivia has already started.")
        await bot.say(embed=embed)
        return
    trivia = True
    triviascore = {
        "lastuser":None,
        "streak":0
    }
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = None
    role = discord.utils.get(ctx.message.server.roles, name="Regular")
    await bot.edit_channel_permissions(ctx.message.channel,role,overwrite)
    embed = discord.Embed(title="Trivia has started.")
    updaterpdict("trivia",trivia)
    updaterpdict("triviascore",triviascore)
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["answertrivia","at","ta"])
@commands.has_any_role("Staff","Trusted")
async def triviaanswer(ctx,user:discord.Member):
    global trivia
    global triviascore
    if ctx.message.channel.name != "game-corner":
        embed = discord.Embed(title="This command only works in the Trivia room.")
        await bot.say(embed=embed)
        return
    if trivia == False:
        embed = discord.Embed(title="Trivia is not running.")
        await bot.say(embed=embed)
        return
    if user.id in triviascore:
        triviascore[user.id] += 1
    else:
        triviascore[user.id] = 1
    if triviascore["lastuser"] == user.id:
        triviascore["streak"] += 1
    else:
        triviascore["lastuser"] = user.id
        triviascore["streak"] = 1
    embed = discord.Embed(title="The point has been awarded to "+user.name+".")
    await bot.say(embed=embed)
    await updatetriviarole(user,ctx.message.server)
    embed = discord.Embed(title="Scoreboard")
    for k in sorted(triviascore,key=itemgetter(1)):
        if k != "lastuser" and k != "streak":
            name = discord.utils.get(ctx.message.server.members,id=k)
            score = triviascore[k]
            embed.add_field(name=name,value=score,inline=False)
    updaterpdict("triviascore",triviascore)
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["sb"])
@commands.has_any_role("Staff","Trusted")
async def scoreboard(ctx):
    global trivia
    global triviascore
    if ctx.message.channel.name != "game-corner":
        embed = discord.Embed(title="This command only works in the Trivia room.")
        await bot.say(embed=embed)
        return
    if trivia == False:
        embed = discord.Embed(title="Trivia is not running.")
        await bot.say(embed=embed)
        return
    tempts = triviascore
    del tempts["lastuser"]
    del tempts["streak"]
    embed = discord.Embed(title="Scoreboard")
    for k in sorted(triviascore,key=itemgetter(1)):
        if k != "lastuser" and k != "streak":
            name = discord.utils.get(ctx.message.server.members,id=k)
            score = triviascore[k]
            embed.add_field(name=name,value=score,inline=False)
    await bot.say(embed=embed)

@bot.command(pass_context=True,aliases=["endtrivia","te","et"])
@commands.has_any_role("Staff","Trusted")
async def triviaend(ctx):
    global trivia
    global triviascore
    if ctx.message.channel.name != "game-corner":
        embed = discord.Embed(title="This command only works in the Trivia room.")
        await bot.say(embed=embed)
        return
    if trivia == False:
        embed = discord.Embed(title="Trivia is not running.")
        await bot.say(embed=embed)
        return
    embed2 = discord.Embed(title="Scoreboard")
    for k in sorted(triviascore,key=itemgetter(1)):
        if k != "lastuser" and k != "streak":
            name = discord.utils.get(ctx.message.server.members,id=k)
            score = triviascore[k]
            embed2.add_field(name=name,value=score,inline=False)
    trivia = False
    triviascore = {
        "lastuser":None,
        "streak":0
    }
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    role = discord.utils.get(ctx.message.server.roles, name="Regular")
    await bot.edit_channel_permissions(ctx.message.channel,role,overwrite)
    embed = discord.Embed(title="Trivia has ended.")
    updaterpdict("trivia",trivia)
    updaterpdict("triviascore",triviascore)
    await bot.say(embed=embed)
    await bot.say(embed=embed2)

@bot.command(pass_context=True,aliases=["rpr","roleplayreviewer"])
@commands.has_any_role("Host")
async def roleplayreview(ctx):
    global rp
    global rpr
    global rprmember
    global rphost
    index = channelindex(ctx.message.channel.name)
    if rpr:
        embed = discord.Embed(title="Please wait for RPR to end before using it again.")
        await bot.say(embed=embed)
        return
    if rp[index] == None:
        embed = discord.Embed(title="There is no RP.")
        await bot.say(embed=embed)
        return
    if rphost[index] == None:
        embed = discord.Embed(title="There is no host.")
        await bot.say(embed=embed)
        return
    rprmember = ctx.message.server.get_member(rphost[index])
    rpr = True
    embed = discord.Embed(title="Roleplay review is now active. For the next 10 minutes, messages to the bot will be forwarded to the host anonymously.",description="Note that messages sent to the bot during Roleplay Review are subject to the rules of the server and logged for moderation purposes.")
    await bot.say(embed=embed)
    await asyncio.sleep(600)
    rprmember = None
    rpr = False
    embed = discord.Embed(title="Roleplay Review has ended.")
    await bot.say(embed=embed)

@bot.event
async def on_message(message):
    global rpr
    global rprmember
    if rpr:
        channel = bot.get_channel("461290964384874507")
        if message.server is None and message.author != bot.user:
            embed = discord.Embed(title="RPR: "+message.author.name+"("+message.author.id+")"+" to "+rprmember.name+"("+rprmember.id+")",description=message.content)
            await bot.send_message(channel,embed=embed)
            await bot.send_message(rprmember,message.content)
    await bot.process_commands(message)

bot.run("insert token here")
#host role id is 461386257822384138