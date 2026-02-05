import discord
from discord.ext import commands

class Stats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="stats",
        description="Botの統計情報を表示します"
    )
    async def stats(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Botの統計情報",
            description="現在のBotの統計情報を表示します。",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="稼働Bot数",
            value=f"{len(self.bot.cogs)} 台",
            inline=False
        )
        embed.add_field(
            name="サーバーping値",
            value=f"{round(self.bot.latency * 1000)} ms",
            inline=False
        )
        embed.add_field(
            name="サーバーPC稼働時間",
            value="{uptime}",
            inline=False
        )
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Stats(bot))