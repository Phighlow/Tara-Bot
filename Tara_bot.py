# -----------------------------------------------
# Author: Justin Nieto
# Created - Fall 2023
# Description: This is a end result of an inside joke between friends. When this bot is hosted on a server it will read the messages within the channels and respond with a "xyz, I hard know her" to any word
#   that ends in -er. 
# for example: "I need to take a shower" reponse: "Shower, I hardly know her!"
#
# thats it...I have used my education wisely 
# ---------------------------------------------

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('TARA_BOT ONLINE')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = message.content.split()
    last_word = words[-1].lower() if words else ""

    if last_word.endswith("er") or last_word.endswith("or"):  # Allow "er" or "or"
        response = f"{last_word} I hard know her"
        await message.channel.send(response)

    # Continue processing other commands
    await client.process_commands(message)

# Move this line outside of the event handler
client.run('Token')
