import discord
import asyncio
from datetime import datetime, time, timedelta
intents = discord.Intents.default()
client = discord.Client(intents=intents)

#add questions to your list, one per day
question_list = [
    "What is your favorite color?",
    "If you could travel back in time 🕥 to any moment in history, where and when would you go?",
    "If you could only eat one food for the rest of your life, what would it be?",
    "If you could be any character from a 📖 book, 🎬 movie, or 📺 TV show, who would you be and why?",
    "If you had to choose between only being able to play games from the 90s or 2000s for the rest of your life, which one would you choose?🧓"
    ]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await asyncio.sleep(5)
    await daily_question()

async def daily_question():
    await client.wait_until_ready()
    while True:
        channel = client.get_channel(channel_id) # replace channel_id with the ID of the channel you want the bot to post in
        current_time = datetime.now().time()
        question = question_list[0]
        question_list.pop(0)
        question_list.append(question)
        question_enh = "**" + str(question) + "**"
        embed = discord.Embed(title="Daily Topic",description=question_enh, color=discord.Color.from_rgb(255,165,0)) #
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Question_Mark.svg/1200px-Question_Mark.svg.png') # replace the URL with the URL of the image you want to use - you can use a discord image link that the bot has access to        
        message = await channel.send(embed=embed)
# you can add emojis like this:
        #if question == "What is your favorite color?":
        #    await message.add_reaction("🟥")
        #    await message.add_reaction("🟦")
# or define an emoji list, question type and use an index
        await asyncio.sleep(86400) # run the loop every 86400 seconds (24 hours)
client.run('your_bot_token')
