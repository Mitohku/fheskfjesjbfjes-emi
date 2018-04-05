import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import random
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
from collections                import Counter


command_prefix = "~" 
description = "A super cute bot for the best girl ever"
bot = commands.Bot(command_prefix, description = description)
bot.remove_command('help')
tu = datetime.datetime.now()
bot_owner = 219881141551759360

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_guild_join(ctx):
	member = discord.Member
	member1 = "TEST"
	welcome = bot.get_channel(429820948485767168)
	
	embed = discord.Embed(colour = discord.Colour(0xA522B3))
	embed.description = f"Welcome to the server **{member1}**! It's nowhere near done and still being set up. You have __24 hours__ to say **`Hai`** or **`Bai`** to access to the server.\nAlso, please read pinned messages."
	await ctx.send(welcome, embed = embed)

#########################################

@bot.command(aliases = ['cmds', 'commands'])
async def help(ctx):

	developer = bot.get_user(385419569558323202)

	if developer.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
	else:
		avi = developer.avatar_url

	embed = discord.Embed(colour = discord.Colour(0xA522B3))
	embed.set_thumbnail(url = avi)
	embed.set_author(name = developer, icon_url = avi)
	embed.description = f"Hi everyone!~♡ I'm **{developer.name}**, the creator of **Emilia Walker** \nThis BOT is for now developed in **Python** by my unique owner: {developer}. \nI started making it after showing my girlfriend that I know how to make them \nbecause she wanted me to make a BOT for her."
	embed.add_field(name="Having Issues/Problems?", value=f"If you have any problems with **Emilia Walker**,\nthen you can use the feedback command to DM my owner: `{command_prefix}ctdev [message]` !", inline=False)

	help1 = discord.Embed(colour = discord.Colour(0xA522B3))
	help1.title = f"Emilia Walker  Commands List~♡"
	help1.description = f"**Emilia Walker**'s prefix is **{command_prefix}**.\nNeed more informations about a command? `{command_prefix}help [command]`\n\n"
	help1.add_field(name="Core Commands", value=f"`{command_prefix}help` **|** `{command_prefix}shutdown` **|** `{command_prefix}game`", inline=False)
	help1.add_field(name="Utility Commands", value=f"`{command_prefix}ping` **|** `{command_prefix}profile` **|** `{command_prefix}about` **|** `{command_prefix}stats` **|** `{command_prefix}avatar` **|** `{command_prefix}guildicon`", inline=False)
	help1.add_field(name="Fun Commands", value=f"`{command_prefix}lovecalc` **|** `{command_prefix}vhug`", inline=False)
	help1.add_field(name="Kawaii Commands", value=f"`{command_prefix}cute`", inline=False)
	help1.add_field(name="Extra Commands", value=f"`{command_prefix}ctdev` **|** `{command_prefix}xmas` **|** `{command_prefix}creation` **|** `{command_prefix}couple`", inline=False)
	help1.set_footer(text = "Have fun using Emilia Walker~♡")
	#help1.description = f"**Emilia Walker** <:bot:389862148395761664>'s prefix is **s**. If the Server Owner changed it, \nYou can use `@Emilia Walker prefix` to get the prefixes list! \nNeed more informations about a command? `shelp [command]`\n\n"

	await ctx.send(embed = embed)
	await ctx.send(embed = help1)

#########################################

@bot.command(pass_context = True, aliases = ['feedback', 'fb', 'msgdev'])
async def ctdev(ctx, *, pmessage : str = None):
	invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
	dev = bot.get_user(385419569558323202)

	if pmessage == None:
		embed = discord.Embed(description = ""+ ctx.author.name +", if you really want to send something to my owner, type a feedback!", color = 0xA522B3)
		await ctx.send(embed = embed)
		await ctx.message.delete()
	else:
			msg = "**__User:__** {}\n**__Server:__** {}\n\n**__FeedBack:__** {}\n\n\n**__Server Invite:__** {}".format(ctx.author, ctx.guild, pmessage, invite.url)
			embed = discord.Embed(title = "Invite to {} discord server!".format(ctx.guild), colour = 0xA522B3, url = "{}".format(invite.url), description = "Feedback: {}".format(pmessage), timestamp = datetime.datetime.utcfromtimestamp(1507439238))
			embed.set_thumbnail(url = "{}".format(ctx.author.avatar_url))
			embed.set_author(name = "{} sent:".format(ctx.author), icon_url = "{}".format(ctx.author.avatar_url))
			await dev.send(embed = embed)
			embed = discord.Embed(description = "I have PMed **{}#{}** with your feedback! Thank you for your help!".format(dev.name, dev.discriminator), color = 0xA522B3)
			await ctx.send(embed = embed)
			await ctx.message.delete()

#########################################

@bot.command(aliases=['kill', 'sd'])
async def shutdown(ctx):
	if await ctx.bot.is_owner(ctx.author):

			developer = bot.get_user(385419569558323202)
			shutdown1 = discord.Embed(colour = discord.Colour(0xA522B3))
			shutdown1.description = f"**Emilia Walker** has been **Shutdown For Maintenance** by ***{developer.name}*** !"
			shutdown1.set_footer(text = time.strftime("%d/%m/%Y - %I:%M:%S %p"))

			await ctx.send(embed = shutdown1)
			bot.logout()
			sys.exit(0)
	else:
			developer = bot.get_user(385419569558323202) # commands.get_user(commands.owner_id)
			shutdown2 = discord.Embed(colour = discord.Colour(0xA522B3))
			list17 = [
			":speech_left:⠀**|⠀*Kurumi Tokisaki***\n```You were ready to kill another creature, yet you are scared to be killed. Dont you think that is weird? When you point a gun at another life... This is what happens.```",
			":speech_left:⠀**|⠀*Tohka Yatogami***\n```Just killing and killing and killing. You deserve to die and to die and to die.```",
			]
			choice17 = random.choice(list17)
			shutdown2.description = choice17
			shutdown2.set_footer(text = "You dont have permissions to use this command")
			
			await ctx.send(embed = shutdown2)

#########################################

@bot.command(aliases=['gleave'])
async def guildleave(ctx):
	guild = ctx.guild
	developer = bot.get_user(385419569558323202)

	if await ctx.bot.is_owner(ctx.author):
		embed = discord.Embed(colour = discord.Colour(0xA522B3))
		embed.description = f"**{developer.name}** told me to leave __{guild.name}__! Bye bye!~"
		await ctx.send(embed = embed)
		await asyncio.sleep(1.50)
		await ctx.guild.leave()
	else:
		embed = discord.Embed(colour = discord.Colour(0xA522B3))
		embed.description = f"**{developer.name}** told m-- Wait. Who are you?!"
		embed.set_footer(text = "You dont have permissions to use this command")
		await ctx.send(embed = embed)

#########################################

@bot.command(aliases=["xmas"])
async def christmas(ctx):
	now=datetime.datetime.utcnow()
	xmas=datetime.datetime(now.year, 12, 25)
	if xmas<now:
		xmas=xmas.replace(year=now.year+1)
		embed=discord.Embed(colour = discord.Colour(0xA522B3))
		embed.add_field(name=":gift::christmas_tree::santa: Christmas :gift::christmas_tree::santa:",
			value=f"***Merry Christmas!*** @everyone")
		await ctx.send(embed=embed)
	delta=xmas-now
	weeks, remainder=divmod(int(delta.total_seconds()), 604800)
	days, remainder2=divmod(remainder, 86400)
	hours, remainder3=divmod(remainder2, 3600)
	minutes, seconds=divmod(remainder3, 60)
	embed=discord.Embed(colour = discord.Colour(0xA522B3))
	embed.add_field(name=":gift::christmas_tree::santa: Time left until __Christmas__ :santa::christmas_tree::gift:",
		value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
	await ctx.send(embed=embed)

@bot.command(aliases=["creation"])
async def botcreation(ctx):
	dev = bot.get_user(385419569558323202)
	now=datetime.datetime.utcnow()
	xmas=datetime.datetime(now.year, 4, 2)
	if xmas<now:
		xmas=xmas.replace(year=now.year+1)
		embed=discord.Embed(colour = discord.Colour(0xA522B3))
		embed.add_field(name=":question::question::question: Bot Creation :question::question::question:",
			value=f"{now.year-2018} years ago, **{dev.name}** started making me! @everyone")
		await ctx.send(embed=embed)
	delta=xmas-now
	weeks, remainder=divmod(int(delta.total_seconds()), 604800)
	days, remainder2=divmod(remainder, 86400)
	hours, remainder3=divmod(remainder2, 3600)
	minutes, seconds=divmod(remainder3, 60)
	embed=discord.Embed(colour = discord.Colour(0xA522B3))
	embed.add_field(name=":question::question::question: Time left until __Bot Creation's Birthday__ :question::question::question:",
		value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
	await ctx.send(embed=embed)

@bot.command(aliases=["couple", "presti", "emilia", "emi", "prestixemilia", "prestixemi"])
async def prestiemilia(ctx):
	presti = bot.get_user(385419569558323202)
	emilia = bot.get_user(180849535306694656)
	now=datetime.datetime.utcnow()
	xmas=datetime.datetime(now.year, 3, 31)
	if xmas<now:
		xmas=xmas.replace(year=now.year+1)
		embed=discord.Embed(colour = discord.Colour(0xA522B3))
		embed.add_field(name=":question::question::question: Couple Love :question::question::question:",
			value=f"{now.year-2018} years ago, **{presti.name}** & **{emilia.name}** became a couple! @everyone")
		await ctx.send(embed=embed)
	delta=xmas-now
	weeks, remainder=divmod(int(delta.total_seconds()), 604800)
	days, remainder2=divmod(remainder, 86400)
	hours, remainder3=divmod(remainder2, 3600)
	minutes, seconds=divmod(remainder3, 60)
	embed=discord.Embed(colour = discord.Colour(0xA522B3))
	embed.add_field(name=":question::question::question: Time left until __Couple Birthday__ :question::question::question:",
		value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
	await ctx.send(embed=embed)

#########################################

##      GAME COMMAND (NOT WORKING)     ##

#########################################

@bot.command(aliases = ['pfp'])
async def avatar(ctx, *, member : discord.Member = None):
	author = ctx.author

	if not member:
		member = author

	if member.avatar:
		if member.avatar_url[54:].startswith('a_'):
			avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
			avi_description = f"**{member.name}'s** avatar!\n[Click to open avatar!]({avi})"
		else:
			avi = member.avatar_url_as(static_format = "png", size = 1024)
			avi_description = f"**{member.name}'s** avatar!\n[Click to open avatar!]({avi})"
	else:
		avi_description = f"**{member.name}** has no avatar!\n"
		avi = "https://i.imgur.com/lkeELEJ.png"

	embed = discord.Embed(description = f"{avi_description}", color =  discord.Colour(0xA522B3))
	embed.set_image(url = f"{avi}")
	await ctx.send(embed = embed)

#########################################

@bot.command(aliases = ['gicon'])
async def guildicon(ctx):
	guild = ctx.guild

	if guild.icon_url:
		embed = discord.Embed(description = f"**{guild.name}'s** guild icon!\n[Click to open {guild.name}'s guild icon!]({guild.icon_url})", color =  discord.Colour(0xA522B3))
		embed.set_image(url = f"{guild.icon_url}")
		await ctx.send(embed = embed)
	else:
		embed = discord.Embed(description = f"**{guild.name}** has no icon!\n", color =  discord.Colour(0xA522B3))
		embed.set_image(url = "https://i.imgur.com/lkeELEJ.png")
		await ctx.send(embed = embed)

#########################################

@bot.command(aliases = ['virtualhug'])
async def vhug(ctx, *, member : discord.Member = None):

	author = ctx.author
	if not member:
		await ctx.send("Please mention a user to send a hug to")
	else:
		member = member.mention

		message = await ctx.send(f"[⠀▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(2)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug...")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug....")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug...")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug....")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug...")
		await asyncio.sleep(2)
		await message.edit(content = f"Successfully sent ***__virtual-hug.exe__***  to **{member}**")

#########################################

@bot.group(invoke_without_command = True)
async def cute(ctx):

	await ctx.send(f"**{ctx.author.name}**, please use one of the following options: `cats`, `dogs` or `neko`")

@cute.command(name = 'cats')
async def cute_cats(ctx):

	async with aiohttp.ClientSession() as session:
		async with session.get("https://random.cat/meow") as r:
			if r.status == 200:
				response = await r.json()
				embed = discord.Embed(description = "Here is your random cute Cat.", color =  discord.Colour(0xA522B3))
				embed.set_image(url = response['file'])
				await ctx.send(embed = embed)	
			else:
				await ctx.send(f'**{ctx.author.name}**, could not access the random.cat API!')

@cute.command(name = 'dogs')
async def cute_dogs(ctx):

	async with aiohttp.ClientSession() as session:
		async with session.get("https://api.thedogapi.co.uk/v2/dog.php") as r:
			if r.status == 200:
				response = await r.json()
				embed = discord.Embed(description = "Here is your random cute Dog.", color =  discord.Colour(0xA522B3))
				embed.set_image(url = response['data'][0]["url"])
				await ctx.send(embed = embed)
			else:
				await ctx.send(f'**{ctx.author.name}**, could not access the random.dog API!')

@cute.command(name = 'neko')
async def cute_neko(ctx):

	async with aiohttp.ClientSession() as session:
		async with session.get("https://nekos.life/api/neko") as r:
			if r.status == 200:
				nekos = await r.json()
				embed = discord.Embed(description = "Here is your random cute Neko Girl.", color =  discord.Colour(0xA522B3))
				embed.set_image(url = nekos['neko'])
				await ctx.send(embed = embed)
			else:
				await ctx.send(f'**{ctx.author.name}**, could not access the Nekos.life API!')

#########################################

@bot.command(aliases = ['lovecalc', 'lcal', 'lovecalculator'])
async def ship(ctx, *, member : discord.Member = None):
	
	if not member:
		await ctx.send("Please mention a user to calculate love percentage")
	else:
		member = member.mention

		love_percentage = random.randint(1, 100)
		if love_percentage < 30:
			love_result = "I think no relationship could happen, you should try to find someone else.."
			embed = discord.Embed(description = f"__Result:__ **{love_percentage}%**\n¤ {love_result}", color =  discord.Colour(0xA522B3))
			embed.set_author(name = f"LoveCalculator⠀⠀❤", icon_url = "http://icons.iconarchive.com/icons/paomedia/small-n-flat/64/heart-icon.png")
			await ctx.send(embed = embed)
		if love_percentage < 50:
			if love_percentage >= 30:
				love_result = "A relationship would be hard, but dont give up!" 
				embed = discord.Embed(description = f"__Result:__ **{love_percentage}%**\n¤ {love_result}", color =  discord.Colour(0xA522B3))
				embed.set_author(name = f"LoveCalculator⠀⠀❤", icon_url = "http://icons.iconarchive.com/icons/paomedia/small-n-flat/64/heart-icon.png")
				await ctx.send(embed = embed)
			else:
				return
		if love_percentage < 80:
			if love_percentage >= 50:
				love_result = "A relationship is possible! Try your best!"
				embed = discord.Embed(description = f"__Result:__ **{love_percentage}%**\n¤ {love_result}", color =  discord.Colour(0xA522B3))
				embed.set_author(name = f"LoveCalculator⠀⠀❤", icon_url = "http://icons.iconarchive.com/icons/paomedia/small-n-flat/64/heart-icon.png")
				await ctx.send(embed = embed)
			else:
				return
		if love_percentage == 100:
			if love_percentage >= 80:
				love_result = "What are you waiting for?! Its possible!"
				embed = discord.Embed(description = f"__Result:__ **{love_percentage}%**\n¤ {love_result}", color =  discord.Colour(0xA522B3))
				embed.set_author(name = f"LoveCalculator⠀⠀❤", icon_url = "http://icons.iconarchive.com/icons/paomedia/small-n-flat/64/heart-icon.png")
				await ctx.send(embed = embed)
			else:
				return

#########################################

@bot.command(aliases = ['ping', 'ms'])
async def latency(ctx):
	pingms = "{}".format(int(ctx.bot.latency * 1000))
	pings = "{}".format(int(ctx.bot.latency * 1))
	message = await ctx.send("Ping - Calculating connection.")
	await message.edit(content = f"Ping - Calculating connection..")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection...")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection....")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection.")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection..")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection...")
	await asyncio.sleep(1.50)
	await message.edit(content = f"Pong! - My latency is **{pings}**s | **{pingms}**ms")

#########################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
