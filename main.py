import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print("ログイン完了")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/set_skin':
        channel = message.channel
        await message.channel.send('set skin!')

        def check(m):
            return m.content == "hello" and m.channel == channel:

        msg = await client.wait_for('message', check=check)
        await channel.send(f"Hello {msg.author}")
        #await message.channel.send(f"{os.listdir(path='.')}")


client.run(os.getenv('DISCORD_BOT_TOKEN'))