from pyrogram import *
from pyrogram.types import *

api_id = 9 # inserisci api_id
api_hash = " " # inserisci api hash
idtoken = " " # inserisci token

idbot = Client('SpoilerIDBot', api_id, api_hash, bot_token=idtoken)

@idbot.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply_text("""
<b><u>๐ Ciao sono IDBot</u></b>

<b><i>๐ด COMANDI ๐ด</i></b>
<i>/getid ยป da il tuo id di telegram
/getgroupid ยป da id del gruppo telegram
/getchannelid ยป da id del canale</i>

<u>๐จ๐ปโ๐ป Developer: @ChillatoDev </u>
""")

@idbot.on_message(filters.group & filters.command("getgroupid"))
async def getgroupid(client, message):
    await message.reply_text(f"CHATID >> `{message.chat.id}`")

@idbot.on_message(filters.command("getid"))
async def getid(client, message):
    await message.reply_text(f"Il tuo id: `{message.from_user.id}`")

@idbot.on_message(filters.channel & filters.command("getchannelid"))
async def getchannelid(client, message):
    await message.reply_text(f"CHANNELID >> `{message.chat.id}`")

idbot.run()
