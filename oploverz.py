from pathlib import Path
from zippyshare import ZippyBot
import re, wget, os

class OPBot(ZippyBot):

    def __init__(self):

        super().__init__()

        self.save_dir = str(Path.home() / "Downloads")

    def update_save_dir(self, new_save_dir):

        self.save_dir = new_save_dir

    def get_info(self, url):

        soups = self.page_renderer(url)
        listinfo = soups.find('div', {'class':'listinfo'}).find('ul').findAll('li')

        for list in listinfo:
            if "ongoing" in list.text.lower():
                status = list.text
                status = re.search(r"\bongoing\b",status.lower())[0]
                break
        
        self.status = status.title()
        self.anime_name = url.split("/")[4].replace("-"," ").title()

    def create_folder(self):

        if not os.path.exists(Path(self.save_dir,self.anime_name)):
            os.mkdir(Path(self.save_dir,self.anime_name))

    def latest_update(self,url):

        soups = self.page_renderer(url)
        episodes = soups.find("div", {'class':'episodelist'}).find("ul")

        episode = episodes.find("span", {'class':'leftoff'}).text.strip()
        upload_date = episodes.find('span', {'class':'rightoff'}).text.strip()

        episode_link = episodes.find("span", {'class':'leftoff'}).find("a")['href']

        self.episode = episode
        self.upload_date = upload_date

        self.episode_link = episode_link

    def download(self):

        def file_title(filename):
            filename = filename.replace("%20", " ")
            filename = filename.replace("%5d", "]")
            filename = filename.replace("%5b", "[")
            return filename
        
        zippy_link = self.get_zippy_link(self.episode_link)
        dl_link = self.get_zippy_download(zippy_link)

        filename = wget.detect_filename(dl_link)
        filename = file_title(filename)
        print(filename)

        self.create_folder()
        save_dir = Path(self.save_dir,self.anime_name)
        
        wget.download(dl_link,str(Path(save_dir,filename)))