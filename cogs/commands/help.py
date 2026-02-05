import discord
from discord.ext import commands



class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="help",
        description="ヘルプメニューを表示します"
    )
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(
            title="ヘルプメニュー",
            description="利用可能なコマンドの一覧です。",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="/ping",
            value="Botの応答速度を測定します。",
            inline=False
        )
        embed.add_field(
            name="/help",
            value="このヘルプメニューを表示します。",
            inline=False
        )

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))