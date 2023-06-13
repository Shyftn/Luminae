import sqlite3
from collections import Counter
from discord.ext import commands

## The `calculate_popular_channels` function is intended to analyze server activity data 
## and determine which channels are the most active. The function works by analyzing the 
## channel IDs of messages and voice channel activities, and counting the occurrences 
## of each channel ID to determine the channels with the most activity.

class PopularChannels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='popular_channels')
    async def calculate_popular_channels(self, ctx, channel_type):
        ## Establish a connection to the SQLite database that stores server activity data
        conn = sqlite3.connect('server_activity.db')

        if channel_type.lower() in ["text", "both"]:
            ## Define a SQL query to fetch all text channel IDs from the activity data
            text_query = 'SELECT text_channel_id FROM activity'
            text_channel_ids = self.fetch_channel_ids(conn, text_query)

        if channel_type.lower() in ["voice", "both"]:
            ## Define a SQL query to fetch all voice channel IDs from the activity data
            voice_query = 'SELECT voice_channel_id FROM activity'
            voice_channel_ids = self.fetch_channel_ids(conn, voice_query)

        if channel_type.lower() == "text":
            popular_channel = self.get_most_common_channel(text_channel_ids)
            await ctx.send(f"The most popular text channel is: {popular_channel}")

        elif channel_type.lower() == "voice":
            popular_channel = self.get_most_common_channel(voice_channel_ids)
            await ctx.send(f"The most popular voice channel is: {popular_channel}")

        elif channel_type.lower() == "both":
            popular_text_channel = self.get_most_common_channel(text_channel_ids)
            popular_voice_channel = self.get_most_common_channel(voice_channel_ids)
            await ctx.send(f"The most popular text channel is: {popular_text_channel}\n"
                           f"The most popular voice channel is: {popular_voice_channel}")

        else:
            await ctx.send("Invalid channel type! Please enter 'text', 'voice', or 'both'.")

    def fetch_channel_ids(self, conn, query):
        ## Execute the SQL query
        cur = conn.cursor()
        cur.execute(query)
        ## Fetch all channel IDs
        channel_ids = [row[0] for row in cur.fetchall()]
        return channel_ids

    def get_most_common_channel(self, channel_ids):
        ## Count the occurrences of each channel ID
        count = Counter(channel_ids)
        ## The channel ID with the most occurrences is the most popular channel
        popular_channel = count.most_common(1)[0][0]
        return popular_channel

def setup(bot):
    bot.add_cog(PopularChannels(bot))
