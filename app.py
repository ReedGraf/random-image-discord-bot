import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="thisDoesntNeedAPrefixBecauseYou@TheBotButItWontLetMeRunItWithoutOne", intents=intents)
folder = "images"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('-=-=-=-=-=-=-=-=-=-=-')

@bot.event
async def on_message(message):
    # Don't respond to self
    if message.author == bot.user:
        return

    # Check if the bot was mentioned
    if bot.user.mentioned_in(message):
        try:
            # Creat the list of files
            images = [img for img in os.listdir(folder) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]

            # Empty folder check
            if images:
                # Pick a random image
                random_image = random.choice(images)
                file_path = os.path.join(folder, random_image)
                
                # Send the file
                with open(file_path, 'rb') as file:
                    await message.channel.send(file=discord.File(file)) # Future To-Do: reply to the user or take a message to reply to?
            else:
                await message.channel.send("`The image folder is empty!`")
                
        except FileNotFoundError:
            await message.channel.send("`Error: " + folder + " folder not found.`")

    # This ensures other commands (if you add them) still work
    await bot.process_commands(message)

load_dotenv()
bot.run(os.getenv("TOKEN"))
