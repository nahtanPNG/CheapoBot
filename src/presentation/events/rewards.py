import discord
from discord.ext import commands

from src.infrastructure.db.balance import add_reward_every_ten_message


async def reward_every_ten_message(message: discord.Message, bot: commands.Bot):
    await bot.process_commands(message)

    if not message.author.bot:
        user_id = message.author.id
        add_reward_every_ten_message(user_id)