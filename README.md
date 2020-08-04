[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) ![Profile views](https://gpvc.arturio.dev/Add830830)
[![Badge](https://fdtu25d5f81p.runkit.sh)](https://git.io/gradientbadge)
## Configuration Variables

##### Mandatory

* `TG_BOT_TOKEN`: Create a bot using [BotFather](https://Telegram.me/BotFather), and get the Telegram API token.

* `APP_ID` & `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).

* `AUTH_CHANNEL`: Create a Super Group in Telegram, add [MissRose](https://telegram.me/MissRose_bot) to the group, and send /id in the chat, to get this value.

* `RCLONE_CONFIG`: Create the rclone config using the rclone.org and read the rclone section for the next.

* `DESTINATION_FOLDER`: Name of your folder in ur respective drive where you want to upload the files using the bot.
wh
* `OWNER_ID`: ID of the bot owner, He/she can be able to access bot in bot mode too.
Get Value by Send /info to [MissRose](https://telegram.me/MissRose_bot)

##### Optional

* `DOWNLOAD_LOCATION`

* `MAX_FILE_SIZE`

* `TG_MAX_FILE_SIZE`

* `FREE_USER_MAX_FILE_SIZE`

* `MAX_TG_SPLIT_FILE_SIZE`

* `CHUNK_SIZE`

* `MAX_MESSAGE_LENGTH`

* `PROCESS_MAX_TIMEOUT`

* `ARIA_TWO_STARTED_PORT`

* `EDIT_SLEEP_TIME_OUT`

* `MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START`

* `FINISHED_PROGRESS_STR`

* `UN_FINISHED_PROGRESS_STR`

* `TG_OFFENSIVE_API`

* `CUSTOM_FILE_NAME`

* `LEECH_COMMAND`

* `YTDL_COMMAND`

* `TELEGRAM_LEECH_COMMAND_G`

* `UPLOAD_AS_DOC`: Takes two option True or False. If True file will be uploaded as document. This is for people who wants video files as document instead of streamable.

* `INDEX_LINK`: (Without `/` at last of the link, otherwise u will get error) During creating index, plz fill `Default Root ID` with the id of your `DESTINATION_FOLDER` after creating. Otherwise index will not work properly.


## Available Commands

* `/ytdl`: This command should be used as reply to a [supported link](https://ytdl-org.github.io/youtube-dl/supportedsites.html)

* `/ytdl gdrive`: This will download and upload to your cloud.

* `/leech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]

* `/leech archive`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]

* `/leech unzip`: This will unzip the .zip file and dupload to telegram.

* `/leech unrar`: This will unrar the .rar file and dupload to telegram.

* `/leech untar`: This will untar the .tar file and upload to telegram.

* `/gleech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. And this will download the files from the given link or torrent and will upload to the cloud using rclone.

* `/gleech archive` This command will compress the folder/file and will upload to your cloud.

* `/gleech unzip`: This will unzip the .zip file and upload to cloud.

* `/gleech unrar`: This will unrar the .rar file and upload to cloud.

* `/gleech untar`: This will untar the .tar file and upload to cloud..

* `/tleech`: This will mirror the telegram files to ur respective cloud cloud.

* `/tleech unzip`: This will unzip the .zip telegram file and upload to cloud.

* `/tleech unrar`: This will unrar the .rar telegram file and upload to cloud.

* `/tleech untar`: This will untar the .tar telegram file and upload to cloud.

* `/getsize`: This will give you total size of your destination folder in cloud.

* `/renewme`: This will clear the remains of downloads which are not getting deleted after upload of the file or after /cancel command. 

You Can Add Custom Name to File just Send Link as `www.website.com/xyz.abc | YourName.extension` And Your File will be uploaded as `YourName.extension`.
