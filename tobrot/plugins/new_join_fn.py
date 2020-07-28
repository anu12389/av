# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    await message.reply_text("Check Pinned Message📌\n Also Check Rules Before Using Commands ☑", quote=True)

async def rename_message_f(client, message):
    await message.reply_text("If You Want To Rename, Send Link As\n <code>www.website.com/ABC.xyz | Your Custom Name.extension</code>\n Then Your File Uploaded As <code>Your Custom name.extension</code>\n• Only Works With Direct Download Links. Don't Try With Magnet Link or .torrent Unless You Will Rewarded With <b>Ban</b>", quote=True)

