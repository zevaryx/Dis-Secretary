import logging
from pathlib import Path

import dis_snek.const
from dis_snek.client import Snake
from dis_snek.models.application_commands import (
    slash_command,
)
from dis_snek.models.context import (
    InteractionContext,
)
from dis_snek.models.discord_objects.embed import Embed
from dis_snek.models.enums import (
    Intents,
)
from dis_snek.models.listener import listen

logging.basicConfig()
cls_log = logging.getLogger(dis_snek.const.logger_name)
cls_log.setLevel(logging.DEBUG)


class Bot(Snake):
    def __init__(self):
        super().__init__(
            intents=Intents.DEFAULT,
            sync_interactions=True,
            delete_unused_application_cmds=True,
            asyncio_debug=True,
            activity="with sneks",
            debug_scope=870046872864165888,
        )

    @listen()
    async def on_ready(self):
        print(f"{bot.user} logged in")

    @slash_command(name="info", description="Information about sneks")
    async def info(self, ctx: InteractionContext):
        emb = Embed(
            description="Dis-snek is an API Wrapper for discord, written in Python. This wrapper is in early development, as such this server acts as a place to contribute and give feedback as the wrapper matures"
        )
        emb.add_field(
            "Links:",
            value="-[GitHub](https://github.com/LordOfPolls/dis_snek)\n-[Trello](https://trello.com/b/LVjnmYKt/dev-board)",
        )
        emb.set_thumbnail(
            url="https://cdn.discordapp.com/icons/870046872864165888/c665942b7f58cc2d2720fd276ae1729e.png?size=1024"
        )
        emb.color = 16426522
        await ctx.send(embeds=emb)


bot = Bot()
bot.g_id = 701347683591389185


bot.grow_scale("scales.support")
bot.grow_scale("scales.githubMessages")
bot.grow_scale("scales.tictactoe")
bot.grow_scale("scales.admin")
bot.grow_scale("scales.debug")
bot.grow_scale("scales.tags")
bot.grow_scale("scales.publish")

bot.start((Path(__file__).parent / "token.txt").read_text().strip())
