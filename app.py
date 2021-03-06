from aiohttp import web
from gino import Gino
from config import POSTGRES_URI


async def init_database(app):
    print('Server start')
    await db.set_bind(POSTGRES_URI)
    await db.gino.create_all()
    yield
    await db.pop_bind().close()
    print('Server stop')

app = web.Application()
db = Gino()
app.cleanup_ctx.append(init_database)
