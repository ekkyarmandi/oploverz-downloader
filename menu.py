from zippyshare import ZippyBot
from tqdm import tqdm
import re

class menu(ZippyBot):

    def __init__(self):
        super().__init__()
        
        self.input_url()
        self.get_all()

        self.browser_status = "inactive"

    def input_url(self):

        def get_anime_name(url):
            name = url.split("/")[4]
            name = name.replace("-"," ")
            name = name.title()
            return name

        print("1 One Piece    : https://www.oploverz.in/series/one-piece-sub-indo/")
        print("2 SNK S4   : https://www.oploverz.in/series/shingeki-no-kyojin-season-4/")
        print("3 Re:Zero S2   : https://www.oploverz.in/series/re-zero-kara-hajimeru-isekai-seikatsu-season-2/")
        print("4 Dr. Stone S2 : https://www.oploverz.in/series/dr-stone-season-2/")
        print()

        req = input("choose your anime by typing number or paste the link below:\n")
        
        try:
            req = int(req)
            if req == 1:
                self.url = "https://www.oploverz.in/series/one-piece-sub-indo/"
            elif req == 2:
                self.url = "https://www.oploverz.in/series/shingeki-no-kyojin-season-4/"
            elif req == 3:
                self.url = "https://www.oploverz.in/series/re-zero-kara-hajimeru-isekai-seikatsu-season-2/"
            elif req == 4:
                self.url = "https://www.oploverz.in/series/dr-stone-season-2/"
        except:
            self.url = req

        self.anime_name = get_anime_name(self.url)
        print("your anime is:", self.anime_name)
        print("loading your anime information..")

    def get_all(self):

        soups = self.page_renderer(self.url)        
        listinfo = soups.find("div", {"class":"listinfo"}).find("ul")
        list_episodes = soups.find("div", {"class":"episodelist"}).find("ul")
        files = []

        for info in listinfo:
            if "status" in info.text.lower():
                self.status = info.text.strip()
                break
        
        for episode in tqdm(list_episodes):
            episode_no = episode.find("span", {"class":"leftoff"}).text.strip().replace("  "," ")
            title = episode.find("span", {"class":"lefttitle"}).text.strip().replace("  "," ")
            link = episode.find("span", {"class":"leftoff"}).find("a")["href"]
            date = episode.find("span", {"class":"rightoff"}).text.strip()

            episode_dict = {'no':episode_no, 'title':title, 'date':date, 'link':link}
            files.append(episode_dict)
        
        files.reverse()        
        self.episodes = files
        print()

    def download_episodes(self):

        n = len(self.episodes)

        request = input(f'$ please input episode below. if more than one, put comma "," as sparator. (max. {n})\n: ')
        request = re.findall(r"\d+",request)
        request = [int(n) for n in request]
        print("loading your request..")

        return request

    def show(self, episode):

        print(f"{episode['no']} {episode['title']} [upload date: {episode['date']}]")
        print("download link:", episode['link'])
        print()

    def activate_browser(self):

        from selenium import webdriver
        driver = "./driver/chromedriver.exe"        
        self.browser = webdriver.Chrome(driver)
        self.browser_status = "active"

    def download(self, download_link):
        
        self.browser.get(download_link)
