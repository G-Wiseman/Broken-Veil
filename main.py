#!/usr/bin/env python3
import discord
import os
import botlogic
import json
import datetime


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-"):
        command = message.content[1:]
        output = botlogic.commands(command)
        if output != None:
            await message.channel.send(output)

    if "<:Chihuaxander:951361274774716486>" in message.content:
        await message.delete()

key = botlogic.get_key()
client.run(key)
