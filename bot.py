from pyrogram import Client
import info


class Bot(Client):
    def __init__(self):
        super().__init__(
            api_id=info.api_id,
            api_hash=info.api_hash,
            bot_token=info.bot_token,
            workers=50,
            plugins={'root':'bot'},
        )