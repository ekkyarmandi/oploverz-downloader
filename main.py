import oploverz
from menu import *

print(
"""
oploverz.in Series Anime Downloader

COMMAND WINDOW
- insert link
- update save dir
- download all
- download episode <int>
- download latest
- status
- exit
"""
)

bot = oploverz.OPBot()
url = ""

while True:

    cmd = input("Command: ")

    if cmd == "insert link":
        url = input_url()
        bot.get_info(url)
        print()
    
    if cmd == "update save dir":
        sd = input("Type/paste your new save directory:\n")
        bot.update_save_dir(sd)
        print(f"Your save directory updated! to:\n{sd}")
    
    if cmd == "download latest":
        if url == "":
            url = input_url()
            bot.get_info(url)

        bot.latest_update(url)
        print_latest(bot)

        bot.download()
    
    if cmd == "download all":
        pass
    
    if cmd == "download episode":
        pass
    
    if cmd == "status":
        if url == "":
            url = input_url()
            bot.get_info(url)

        print_status(bot)

    if cmd == "exit":
        break

# https://www.oploverz.in/series/re-zero-kara-hajimeru-isekai-seikatsu-season-2/