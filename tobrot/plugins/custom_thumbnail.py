"""ThumbNail utilities, © @AnyDLBot"""


import os

from tobrot import DOWNLOAD_LOCATION

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image


async def save_thumb_nail(client, message):
    thumbnail_location = os.path.join(
        DOWNLOAD_LOCATION,
        "thumbnails"
    )
    thumb_image_path = os.path.join(
        thumbnail_location,
        str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("Okay Wait,\nI'm Processing....")
    if message.reply_to_message is not None:
        if not os.path.isdir(thumbnail_location):
            os.makedirs(thumbnail_location)
        download_location = thumbnail_location + "/"
        downloaded_file_name = await client.download_media(
            message=message.reply_to_message,
            file_name=download_location
        )
        # https://stackoverflow.com/a/21669827/4723940
        Image.open(downloaded_file_name).convert("RGB").save(downloaded_file_name)
        metadata = extractMetadata(createParser(downloaded_file_name))
        height = 0
        if metadata.has("height"):
            height = metadata.get("height")
        # resize image
        # ref: https://t.me/PyrogramChat/44663
        img = Image.open(downloaded_file_name)
        # https://stackoverflow.com/a/37631799/4723940
        # img.thumbnail((320, 320))
        img.resize((320, height))
        img.save(thumb_image_path, "JPEG")
        # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
        os.remove(downloaded_file_name)
        await ismgs.edit(
            "Your Image is Successfully Saved as Thumbnail For Videos & Files." + \
            "This Image Will Be Used as Thumbnail to Further Uploads.\nYou Can Change This By /delete"
        )
    else:
        await message.edit("Reply To a Image To Set Custom Thumbnail")


async def clear_thumb_nail(client, message):
    thumbnail_location = os.path.join(
        DOWNLOAD_LOCATION,
        "thumbnails"
    )
    thumb_image_path = os.path.join(
        thumbnail_location,
        str(message.from_user.id) + ".jpg"
    )
    ismgs = await message.reply_text("Okay Wait,\nI'm Processing....")
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
    await ismgs.edit("Custom Thumbnail Deleted Succesfully.")
