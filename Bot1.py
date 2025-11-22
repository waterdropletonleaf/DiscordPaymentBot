import discord
from datetime import date, datetime, time, timedelta
from discord.ext import tasks, commands
import csv
from update import add_user, remove_user, search_user
from tax import payment_time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith('$hello'):
    #     await message.channel.send("Hello")

    if message.content.startswith('$add'):
        #Returns a string of the discord message
        #just need to ignore the $add and send out a message saying
        #added X user to payment list
        new_user = str(message.clean_content)[5:]
        #call a function to update a txt file with the new user string
        add_user(new_user)
        await message.channel.send("added " + new_user + " to payment list")
    
    if message.content.startswith('$search'):
        print("Search User ran")
        find_user = str(message.clean_content)[8:]
        print(find_user)
        v1, v2 = search_user(find_user)
        print(v1)
        row = str(v1)
        if v2 == True: 
            await message.channel.send(find_user + " is at row " + row)
        else:
            await message.channel.send(find_user + " is not in file")

            
        
        # If true, return user is in payment list 
        #if false, return user is not in payment list 
            
    if message.content.startswith('$remove'):
        print("Remove User Ran")

        free_user = str(message.clean_content)[8:]
        print(free_user)
        # #call a function to update a txt file with the new user string
        remove_user(free_user)
        # await message.channel.send("added " + free_user + " to payment list")

@tasks.loop(hours= 24) # send a message every 30 days 
async def auto_send(channel : discord.TextChannel):
    rn = datetime.now()
    if (rn.day == 1):
        victim = str(payment_time())
        await channel.send(victim + " Needs to pay User1 for Various task")

@client.event
async def on_ready():

    if not auto_send.is_running():
        channel = await client.fetch_channel(ChannelID)
        auto_send.start(channel)

    print('Ready')
client.run('DiscordKey')
