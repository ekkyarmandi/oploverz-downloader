import oploverz
import menu

bot = oploverz.OPBot()
url = menu.input_url()

print(
"""
oploverz.in Series Anime Downloader

COMMAND WINDOW
- insert link
- status
- download latest
- download episode <int> or <int_list>
- download all
- update save dir
- exit
"""
)

while True:

    cmd = input("Command: ")

    if cmd == "insert link":
        url = menu.input_url()
        bot.get_info(url)
        print()
    
    if cmd == "update save dir":
        sd = input("Type/paste your new save directory:\n")
        bot.update_save_dir(sd)
        print(f"Your save directory updated! to:\n{sd}")
    
    if cmd == "download latest":
        if url == "":
            url = menu.input_url()
            bot.get_info(url)
        else:
            bot.get_info(url)

        episode_link = bot.latest_update(url)
        menu.print_latest(bot)

        bot.download(episode_link)

        print("Latest video downloaded succesfully!")
    
    if cmd == "download all":

        # get the url first
        if url == "":
            url = menu.input_url()
            bot.get_info(url)
        else:
            bot.get_info(url)

        # return all the episodes link in a list
        links = bot.get_all_episodes(url)

        # download all the link in the list sequencingly
        for link in links.values():
            bot.download(episode_link)

        print("All videos downloaded succesfully!")

    if cmd == "download episode":

        # make sure the url inserted
        if url == "":
            url = menu.input_url()
            bot.get_info(url)
        else:
            bot.get_info(url)

        # get the wanted episodes in number or list
            request = input("Which episode you want to download?\n Note: please type the episode in number and if more than one put coma as separator\n")
            request = menu.request_purify(request)

        # download the episodes based on requested number
        links = bot.get_all_episodes(url)

        for i in request:
            bot.download(links[i])

        print("Episode(s):", menu.string_machine(request), "has been downloaded!")
    
    if cmd == "status":
        if url == "":
            url = menu.input_url()
            bot.get_info(url)
        else:
            bot.get_info(url)


        menu.print_status(bot)

    if cmd == "exit":
        break