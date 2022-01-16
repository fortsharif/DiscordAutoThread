import discord 
import os
from discord.ext import commands


# RE-WRITE ALL OF THIS LATER MESSY CODE.

def main():

    global added_message 
    added_message = ''

    required_roles = ['Fantasy Football Helpers', 'Admin', 'Mods']

    client = commands.Bot(command_prefix='!' , intents = discord.Intents.all())
    
    

    @client.event 
    async def on_message(message):
        text_channel = client.get_channel(int(os.environ.get('TEXT_CHANNEL')))
        text_channel_two = client.get_channel(351411099205369868)
        new_thread = None
        global added_message
        guild = client.get_guild(202794531488268289)
        print(message.author.name)
        author_role = guild.get_member(int(message.author.id)).roles
        user_roles = [role.name for role in author_role]
            
        if any(x in required_roles for x in user_roles):
            if message.content.startswith('!add'):
                new_text = message.content.replace('!add','')
                added_message = new_text
                return await text_channel_two.send(content="*Added Message*")
            if message.content.startswith('!remove'):
                added_message = ''
                return await text_channel_two.send(content="*Removed Message*")

            
        if message.attachments and message.channel == text_channel:
            new_thread = await text_channel.create_thread(name = f'{message.author.name} RMT', message=message, auto_archive_duration = 60 )
            if len(added_message) > 0:
                await new_thread.send(content=added_message)
        


    client.run(os.environ.get("TOKEN"))

main()
