import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PRODIA_API_KEY = os.getenv('PRODIA_API_KEY')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!generate'):
        prompt = message.content[len('!generate '):]
        await message.channel.send('Generating image...')
        image_url = generate_image(prompt)
        if image_url:
            await message.channel.send(image_url)
        else:
            await message.channel.send('Failed to generate image.')

def generate_image(prompt):
    url = "https://api.prodia.com/v1/generate"
    headers = {
        "Authorization": f"Bearer {PRODIA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "num_images": 1
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['images'][0]['url']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

client.run(DISCORD_TOKEN)
