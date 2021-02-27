from menu import menu
from tqdm import tqdm

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
    
    # download all episodes
    if cmd == "da":
        episodes = []
        for i in tqdm(range(len(menu.episodes))):
            episode = menu.episodes[i]
            episode['link'] = menu.get_link(episode['link'])
            episodes.append(episode)
        
        print()
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
        for episode in req_ep: menu.show(episode)

    # show all the episodes
    if cmd == "se":
        for episode in menu.episodes: menu.show(episode)
    
    # show anime status
    if cmd == "s":
        print(menu.status)
        print()
    
    if cmd == "exit":
        break