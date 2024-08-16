import discord
from discord import app_commands
import os

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True  # Enable member intents
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {bot.user}')

@tree.command(name="customs_assign", description="Assign team roles")
async def customs_assign(interaction: discord.Interaction):

    await interaction.response.defer()

    role_to_check1 = next((x for x in interaction.guild.roles if "Red: " in x.name), None)
    role_to_give1 = discord.utils.get(interaction.guild.roles, name='Team Magma')

    listm = []

    for member in interaction.guild.members:  
        if role_to_check1 in member.roles:
            listm.append(member.name)  
            await member.add_roles(role_to_give1) 

    role_to_check2 = next((x for x in interaction.guild.roles if "Blue: " in x.name), None)
    role_to_give2 = discord.utils.get(interaction.guild.roles, name='Team Aqua')

    lista = []

    for member in interaction.guild.members:  
        if role_to_check2 in member.roles:  
            lista.append(member.name)
            await member.add_roles(role_to_give2)
            
    magma = bot.get_channel(1175476709999526048)
    aqua = bot.get_channel(1175476817440804974)

    if magma is not None:
        await magma.send(f"{role_to_give1.mention} Private team chat!")
    if aqua is not None:
        await aqua.send(f"{role_to_give2.mention} Private team chat!")

    await interaction.followup.send(f"Assigned Magma to: {listm}\nAssigned Aqua to: {lista}")


@tree.command(name="customs_remove", description="Remove team roles")
async def customs_remove(interaction: discord.Interaction):

    await interaction.response.defer()

    role_to_check1 = discord.utils.get(interaction.guild.roles, name='Team Magma')
    
    listm = []

    for member in interaction.guild.members:  
        
        if role_to_check1 in member.roles:  
            listm.append(member.name)
            await member.remove_roles(role_to_check1) 

    role_to_check2 = discord.utils.get(interaction.guild.roles, name='Team Aqua')
    
    lista = []

    for member in interaction.guild.members:  
        
        if role_to_check2 in member.roles:  
            lista.append(member.name)
            await member.remove_roles(role_to_check2)
    
    await interaction.followup.send(f"Removed Magma from: {listm}\nRemoved Aqua from: {lista}")

bot.run(TOKEN)
