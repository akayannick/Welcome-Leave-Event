import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Dein_Status_Hier_Rein"))

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    embed = discord.Embed(title="A Member Joined the Server!", description="{0.mention} joined the Server.\n".format(member), color=0x6f3636, url="https://discord.gg/ndnUpU3CQf", timestamp=datetime.utcnow())
    embed.set_author(name=member.display_name, icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    if channel is not None:
        await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    embed = discord.Embed(title="A Member left the Server!", description="{0.mention} left the Server.\n Member joined at: {0.joined_at}".format(member), color=0xe74c3c, url="https://discord.gg/ndnUpU3CQf", timestamp=datetime.utcnow())
    embed.set_author(name=member.display_name, icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    if channel is not None:
        await channel.send(embed=embed)
        
        
client.run("Dein_Token_Hier_Rein")
