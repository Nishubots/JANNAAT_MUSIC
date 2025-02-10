from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝐎𝐖𝐍𝐄𝐑 𝐒𝐄 𝐏𝐔𝐂𝐇𝐎 𝐑𝐄𝐏𝐎 𝐊𝐄 𝐋𝐈𝐘𝐄 

✰ || @its_deva_heree  ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ 𝗠ᴇ 𝗕ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("˹𝚵𝗔𝗚𝗟𝗘˼ ˹𝗨𝗣𝗗𝗔𝗧𝚵𝗦˼", url="https://t.me/EAGLE_UPDTAES"),
          InlineKeyboardButton("𝗥𝗔𝗗𝗛𝗘", url="https://t.me/its_deva_heree"),
          ],
               [
                InlineKeyboardButton("𝐂𝐇𝐀𝐓 𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/UNDERGROUND_MAFIA_CLUB"),
],
[
InlineKeyboardButton("𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓", url=f"https://t.me/SUKOONN_MUSIC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/UNo.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
