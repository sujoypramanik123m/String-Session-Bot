from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import *
from .db import db
from .fsub import get_fsub
from pyrogram.errors import RPCError


@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot: Client, msg: Message):
    if not await db.is_user_exist(msg.from_user.id):
        await db.add_user(msg.from_user.id, msg.from_user.first_name)
        await bot.send_message(
            chat_id=LOG_CHANNEL, 
            text=f"**#NewUser\n\n👤 {msg.from_user.mention}**\n\nID - `{msg.from_user.id}`"
        )
    if IS_FSUB and not await get_fsub(bot, msg):return

    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""{msg.from_user.mention},\n\nɪ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ\n\nᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ sᴇssɪᴏɴ\n\n<blockquote><b>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/CallOwnerBot'>ʀᴀʜᴜʟ</a></b></blockquote>""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
        ])
    )
