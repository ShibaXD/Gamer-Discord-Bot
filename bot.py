import discord
from discord.ext.commands import Bot
import secrets
nick_trinnaman = Bot(command_prefix = "!")

@nick_trinnaman.event
async def on_read():
    print("Clinet logged in")

@nick_trinnaman.command()
async def hello(*args):
    return await nick_trinnaman.say("Hello World!")

nick_trinnaman.run("Mjk5NTAyNTYwOTQxOTY1MzIy.C8rrsw.dgHZ99aYLTICkbNXeYqXPGsYoac")
