import discord 
import os

def main():

    client = discord.Client()
    

    @client.event 
    async def on_message(message):
        text_channel = client.get_channel(int(os.environ.get('TEXT_CHANNEL')))
        if message.attachments and message.channel == text_channel:
            await text_channel.create_thread(name = f'{message.author.name} RMT', message= message, auto_archive_duration = 60 )

    client.run(os.environ.get("TOKEN"))

main()
