import discord
from discord.ext import commands

class Manage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as")
        print(self.bot.user.name)
        print("----------")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        c_general_joined = self.bot.get_channel(555073650902958104)
        join_embed = discord.Embed(title=f"Welcome {member}", description="We hope you'll have an amazing stay! 😊", colour=discord.Color.green())
        await c_general_joined.send(embed=join_embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        c_general_left = self.bot.get_channel(555073650902958104)
        leave_embed = discord.Embed(title=f"We're sad you left, {member}", description="We're sorry to see you go 😭", colour=discord.Color.red())
        await c_general_left.send(embed=leave_embed)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return
        if (reaction.emoji == '✅'):
            await reaction.message.mentions[0].kick(reason=None)
        if (reaction.emoji == '❌'):
            await reaction.message.mentions[0].ban(reason=None)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
    
    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount * 1)
        embed = discord.Embed(title="Silence Peasents", description="I did some hacking, so Silence!", colour=discord.Color.dark_blue())
        embed.add_field(name="Messages deleted.", value=f"{amount} messages deleted.")
        await ctx.send(embed=embed)

    @clear.error
    async def clear_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to delete.')

    @commands.command()
    async def punish(self, ctx, member : discord.Member, *, reason=None):
        msg = await ctx.send(f'Are you sure you want to punish {member.mention}? React with ✅ to kick, and with ❌ to ban.')
        reactions = ['✅', '❌']
        for emoji in reactions:
            await msg.add_reaction(emoji)                  
def setup(bot):
    bot.add_cog(Manage(bot))