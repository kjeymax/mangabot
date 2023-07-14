import asyncio as aio
import os
import uvloop

uvloop.install()

from pathlib import Path
from bot import bot, manga_updater
from models import DB 
from extras import load_plugin

load_plugin(Path("extras.py"))

async def async_main():
    db = DB()
    await db.connect()
    
if __name__ == '__main__':
    loop = aio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(async_main())
    loop.create_task(manga_updater())
    bot.run()
