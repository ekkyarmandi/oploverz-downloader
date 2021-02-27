from menu import menu
from tqdm import tqdm
import time

menu = menu()

print(
"""
COMMAND WINDOW
$ ri - reinsert link
$ dl - download latest
$ da - download all
$ de - download episodes
$ se - show episodes
$ s  - status
$ a  - activate the browser
$ exit
"""
)

while True:

    cmd = input("$ ")

    # reinsert the link
    if cmd == "ri":
        menu.input_url()
        menu.get_all()
    
    # download latest episodes
    if cmd == "dl":
        episode = menu.episodes[-1]
        episode['link'] = menu.get_link(episode['link'])
        menu.show(episode)

        if menu.browser_status == "active":
            menu.download(episode['link'])
    
    # download all episodes
    if cmd == "da":
        episodes = []
        for i in tqdm(range(len(menu.episodes))):
            episode = menu.episodes[i]
            episode['link'] = menu.get_link(episode['link'])
            episodes.append(episode)
        
        print()
        if menu.browser_status == "active":
            for episode in episodes:
                menu.download(episode['link'])
                menu.show(episode)
        else:
            for episode in episodes: menu.show(episode)
    
    # download list of episodes
    if cmd == "de":
        req = menu.download_episodes()
        req_ep = []

        for i in tqdm(req):
            episode = menu.episodes[i-1]
            episode['link'] = menu.get_link(episode['link'])
            req_ep.append(episode)
        
        print()
        if menu.browser_status == "active":
            for episode in episodes:
                menu.download(episode['link'])
                menu.show(episode)
        else:
            for episode in episodes: menu.show(episode)

    # show all the episodes
    if cmd == "se":
        for episode in menu.episodes: menu.show(episode)
    
    # show anime status
    if cmd == "s":
        print(menu.status)
        print()
    
    if cmd == "a":
        menu.activate_browser()

    if cmd == "exit":
        break