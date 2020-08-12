import subprocess
import os
import asyncio

from tobrot import (
    EDIT_SLEEP_TIME_OUT,
    DESTINATION_FOLDER,
    RCLONE_CONFIG
)
from pyrogram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)


async def check_size_g(client, message):
    #await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    del_it = await message.reply_text("Wait, I'm Processing...")
    subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
    with open('rclone.conf', 'a', newline="\n") as fole:
        fole.write("[DRIVE]\n")
        fole.write(f"{RCLONE_CONFIG}")
    destination = f'{DESTINATION_FOLDER}'
    gau_tam = subprocess.Popen(['rclone', 'size', '--config=rclone.conf', 'DRIVE:'f'{destination}'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    gau, tam = gau_tam.communicate()
    print(gau)
    print(tam)
    print(tam.decode("utf-8"))
    gautam = gau.decode("utf-8")
    print(gautam)
    await asyncio.sleep(5)
    await message.reply_text(f"Cloud Storage Used :\n\n{gautam}")
    await del_it.delete()

#gautamajay52
async def g_clearme(client, message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton("Yes", callback_data=("fuckingdo").encode("UTF-8")))
    ikeyboard.append(InlineKeyboardButton("No", callback_data=("fuckoff").encode("UTF-8")))
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text("Are You Sure ?\nThis Will Delete All Your Downloads Locally", reply_markup=reply_markup, quote=True)