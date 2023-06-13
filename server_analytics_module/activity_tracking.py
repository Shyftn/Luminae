import discord
from discord.ext import commands
from .activity_cogs import ActivityTracker, PopularChannels

def setup(bot):
    bot.add_cog(ActivityTracker(bot))
    bot.add_cog(PopularChannels(bot))

class ActivityTracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Insert logic to track message events here
        # You'll likely want to insert the data into a database for later analysis
        pass

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # Insert logic to track reaction events here
        # You'll likely want to insert the data into a database for later analysis
        pass

def setup(bot):
    bot.add_cog(ActivityTracker(bot))
