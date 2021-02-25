import re, os
from pathlib import Path

def input_url():

    url = input("Type/paste your anime link:\n")

    return url

def print_status(object):

    print()
    print("Your anime downloads directory:",object.save_dir)
    print("Anime Name:",object.anime_name)
    print("Status:",object.status)
    print()

def print_latest(object):

    print()
    print(object.episode,"[{}]".format(object.upload_date))
    print(object.episode_link)
    print()

def request_purify(string):

    req_list = re.findall(r"\d+", string)
    req_list = [int(chr) for chr in req_list]

    return req_list

def string_machine(int_list):

    str_list = [str(chr) for chr in int_list]
    string = ", ".join(str_list[-1]) + ", & " + str_list[-1]

    return string

def open_folder(object):

    os.startfile(Path(object.save_dir,object.anime_name))