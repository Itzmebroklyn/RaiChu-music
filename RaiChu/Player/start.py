
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**I ᴀᴍ Aʟɪᴇɴ Mᴜsɪᴄ Dᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [亗 ❥︎×͜×『Mʏsᴛᴇʀɪᴏᴜs』❥︎࿐亗](https://t.me/itzmemysty)
        ✨Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Gʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ Aᴅᴍɪᴍ Wɪᴛʜ Mᴀɴᴀɢᴇ Vᴏɪᴄᴇ ᴄʜᴀᴛs Tᴏ Eɴᴊᴏʏ ᴛʜᴇ Fᴇᴀᴛᴜʀᴇs ᴏғ ᴀʟɪᴇɴ
        ✨Fᴏʀ Aɴʏ Qᴜᴇʀʏ ᴄᴏɴᴛᴀᴄᴛ Mʏ Sᴜᴘʀᴇᴍᴇ✨ [亗 ❥︎×͜×『Mʏsᴛᴇʀɪᴏᴜs』❥︎࿐亗](https://t.me/itzmemysty)
        ✨Tᴏ Sᴇᴇ Mʏ Aʟʟ Fᴇᴀᴛᴜʀᴇs Cʟɪᴄᴋ Hᴇʟᴘ 
        ✨Pᴏᴡᴇʀᴇᴅ Bʏ [💘💞✰★𝙆𝙖𝙣𝙣𝙞 𝙍𝙖𝙖𝙨𝙞 𝙆𝙖𝙖𝙧𝙖𝙣 𝘿𝙖★✰💞💘](https://t.me/itzmekanniraasi)
        ✨Tʜᴀɴᴋs Tᴏ Aᴅᴅ Mᴇ🖤 **
        
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ",url="https://t.me/itzmemysty"
                    ),
                    InlineKeyboardButton(
                        "Nᴇᴛᴡᴏʀᴋ", url="https://t.me/itzmealienNetwork"
                    ),
                    InlineKeyboardButton(
                        "Cᴏᴍᴍᴀɴᴅ Lɪsᴛ", url="https://telegra.ph/file/1fd037fa3bcc8b5406a7b.jpg"
                    )
                  ],[
                    InlineKeyboardButton(
                       "Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url="https://t.me/itzmealiensupportgroup"
                    ),
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇs", url="https://t.me/itzmealienUpdates"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",
                        url=f"https://t.me/{itzmealienbot}?startgroup=true",
                    )
                   ]
                ]
            ]
        ),
     disable_web_page_preview=True
    )
