import asyncio
import logging
from pathlib import Path

import dis_snek
from dis_snek import Snake, Intents, listen, slash_command, InteractionContext

logging.basicConfig()
cls_log = logging.getLogger(dis_snek.const.logger_name)
cls_log.setLevel(logging.DEBUG)


class Bot(Snake):
    def __init__(self):
        super().__init__(
            intents=Intents.DEFAULT | Intents.GUILD_MEMBERS,
            sync_interactions=True,
            delete_unused_application_cmds=True,
            asyncio_debug=True,
            activity="with sneks",
            debug_scope=870046872864165888,
            fetch_members=True,
        )

    @listen()
    async def on_ready(self):
        print(f"{bot.user} logged in")

    @slash_command(
        name="news_ping",
        description="Get mentioned whenever news is posted",
        scopes=[701347683591389185],
    )
    async def news_ping(self, ctx: InteractionContext):
        await ctx.defer(ephemeral=True)
        ping_id = 923682774915883028
        if ctx.author.has_role(ping_id):
            await ctx.author.remove_role(ping_id, "User requested to remove role")
            return await ctx.send("The news ping role has been removed", ephemeral=True)
        else:
            await ctx.author.add_role(ping_id, "User requested to add role")
            return await ctx.send("The news ping role has been added", ephemeral=True)

    @slash_command(
        name="poll_ping",
        description="Get mentioned whenever polls are posted",
        scopes=[701347683591389185],
    )
    async def poll_ping(self, ctx: InteractionContext):
        await ctx.defer(ephemeral=True)
        ping_id = 929787105134133269
        if ctx.author.has_role(ping_id):
            await ctx.author.remove_role(ping_id, "User requested to remove role")
            return await ctx.send("The poll ping role has been removed", ephemeral=True)
        else:
            await ctx.author.add_role(ping_id, "User requested to add role")
            return await ctx.send("The poll ping role has been added", ephemeral=True)


bot = Bot()
bot.g_id = 701347683591389185


bot.grow_scale("scales.support")
bot.grow_scale("scales.githubMessages")
bot.grow_scale("scales.tictactoe")
bot.grow_scale("scales.admin")
bot.grow_scale("dis_snek.ext.debug_scale")
bot.grow_scale("scales.tags")
bot.grow_scale("scales.publish")
bot.grow_scale("scales.logging")
bot.grow_scale("scales.fun")
bot.grow_scale("scales.radio")

asyncio.run(bot.astart((Path(__file__).parent / "token.txt").read_text().strip()))
