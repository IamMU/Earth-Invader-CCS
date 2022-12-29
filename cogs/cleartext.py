# Cleartext
# Made by: IamMU

import nextcord
from nextcord.ext import commands

# match file name with classname
class cleartext(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cleartext - Loaded")

    @nextcord.slash_command(description="Cleartext Encode / Decode" #guild_ids=[guild_id]
    )
    async def cleartext(self, interaction: nextcord.Interaction, action, text):

        # If not enc/dec this stays blank and throws error
        message = ""
        # "encode" or "e" entered
        if action == "encode" or action == 'e':
            output = text 

            message = f"**Encoded:**\n{output}"

        # "decode" or "d" entered
        if action == "decode" or action == 'd':
            output = text

            message = f"**Decoded:**\n{output}"

        await interaction.response.send_message(message)

    # Handle Errors
    @cleartext.error
    async def on_command_error(self, interaction: nextcord.Interaction, error):

        # Help Menu
        message = """
**Syntax**
> Usage - `/cleartext`  `<encode/decode>`  `<text>`

**Examples:**
> Shorthand: `/cleartext`  `e`  `some text to encode`
> Longhand: `/cleartext`  `decode`  `some text to decode`
"""
        embed = nextcord.Embed(title="SYNTAX ERROR",
                               color=0xFE060A, description=message)
        await interaction.channel.send(embed=embed)


def setup(client) -> None:
    client.add_cog(cleartext(client))
