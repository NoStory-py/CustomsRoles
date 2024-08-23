import discord
from discord import app_commands
import os

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True 
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {bot.user}')

@tree.command(name="customs_assign", description="Assign team roles")
async def customs_assign(interaction: discord.Interaction):

    await interaction.response.defer()

    check_red = None
    team_magma = discord.utils.get(interaction.guild.roles, name='Team Magma')
    check_blue = None
    team_aqua = discord.utils.get(interaction.guild.roles, name='Team Aqua')
    magma_added = []
    aqua_added = []

    for x in interaction.guild.roles:
        if "Red: " in x.name:
            check_red = x
        elif "Blue: " in x.name:
            check_blue = x
    
    if check_blue is None and check_red is None:
        return await interaction.followup.send("Failed Coudnt find the Role Red: and Blue: , Lobby isnt created yet.")

    if check_red is not None:
        for member in check_red.members:  
            await member.add_roles(team_magma) 
            magma_added.append(member.nick if member.nick else member.name)

    if check_blue is not None:   
        for member in check_blue.members:  
            await member.add_roles(team_aqua)
            aqua_added.append(member.nick if member.nick else member.name)

    # main magma_chat = bot.get_channel(1175476709999526048)
    # main aqua_chat = bot.get_channel(1175476817440804974)
    magma_chat = bot.get_channel(1273275120391164007)
    aqua_chat = bot.get_channel(1273275140620156950)
    '''
    if magma_chat is not None:
        await magma_chat.send(f"{team_magma.mention} Private team chat!")
    if aqua_chat is not None:
        await aqua_chat.send(f"{team_aqua.mention} Private team chat!")
    '''
    return await interaction.followup.send(f"Assigned Magma to: {", ".join(magma_added)}\nAssigned Aqua to: {", ".join(aqua_added)}")

@tree.command(name="customs_remove", description="Remove team roles")
async def customs_remove(interaction: discord.Interaction):

    await interaction.response.defer()

    team_magma = discord.utils.get(interaction.guild.roles, name='Team Magma')
    team_aqua = discord.utils.get(interaction.guild.roles, name='Team Aqua')
    magma_removed = []
    aqua_removed = []

    for member in team_magma.members:  
        await member.remove_roles(team_magma) 
        magma_removed.append(member.nick if member.nick else member.name)
    for member in team_aqua.members:  
        await member.remove_roles(team_aqua) 
        aqua_removed.append(member.nick if member.nick else member.name)
            
    return await interaction.followup.send(f"Removed Magma from: {", ".join(magma_removed)}\nRemoved Aqua from: {", ".join(aqua_removed)}")

bot.run(TOKEN)
