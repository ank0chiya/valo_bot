import discord
import os
import json


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
            return m.author == message.author

        await message.channel.send("今日の武器は？？？？")
        await message.channel.send("記入形式は｛武器種:武器名｝にしてください")
        wapon_list = []
        for _ in range(4):
            wapon_list.append(await client.wait_for('message', check=check, timeout=10))
        
        print(wapon_list)

        await message.channel.send(f"Message {wapon_list[1].content}")
        #await message.channel.send(f"{os.listdir(path='.')}")

    if message.content == '/get_skin':
        json_open = open('db/db.json', 'r')
        json_load = json.load(json_open)

        await message.channel.send(f"日付を入力してください ex)2020/1/1")
        date_msg = await client.wait_for('message')

        for date in json_load.values():
            if date_msg.content == date["date"]:
                await message.channel.send(date["wapon"])
            else:
                await message.channel.send("日付を確認してください")



client.run(os.getenv('DISCORD_BOT_TOKEN'))