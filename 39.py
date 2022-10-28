import auth
import discord
from discord.utils import get as dc_get
from discord import app_commands
import binmoji

print("Initializing...")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="ping")
async def idea_new(interaction: discord.Interaction):
	await interaction.response.send_message("Pong!", ephemeral=True)

@tree.context_menu(name="Binify")
async def idea_context_menu(interaction: discord.Interaction, message: discord.Message):
	emojis = message.content.replace(" ", "")
	print("binify msg:", emojis)
	if len(emojis) != 8:
		await interaction.response.send_message("Binary appears malformed", ephemeral=True)
		return
	out = binmoji.bin_to_emoji(emojis)
	await interaction.response.send_message(out)

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	game = discord.Game("binary counter")
	await client.change_presence(status=discord.Status.online, activity=game)
	await tree.sync()

client.run(auth.TOKEN)
