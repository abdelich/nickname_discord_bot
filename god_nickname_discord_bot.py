import discord
from discord.ext import commands

token = "MTAyMzc1MjM1NTUwMzY4MTU4OA.G1UQB2.U72P-cgFpfX8UmFXaFuHjfaaPFvhpN-9jGKsnA"
prefix = "/"

intents = discord.Intents.all()
bot = commands.Bot(prefix, intents=intents)


@bot.event
async def on_member_update(before, after):
    # role = discord.utils.get(after.ctx.guild.roles, name="казах")

    if before.nick != after.nick and after.nick != "saguroff":
        channel = discord.utils.get(before.guild.text_channels, name='bi')
        await after.edit(nick="я ПИДОР")




bot.run(token)
