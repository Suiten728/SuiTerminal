import discord
from discord.ext import commands

class Setup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="setup",
        description="Botのセットアップを行います"
    )
    async def setup(self, ctx: commands.Context):
        embed = discord.Embed(
            title="セットアップ完了",
            description="Botのセットアップが完了しました。",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Setup(bot))