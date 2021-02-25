def input_url():

    url = input("Type/paste your anime link:\n")

    return url

def print_status(object):

    print()
    print("Your anime downloads directory:",object.save_dir)
    print("Anime Name:",object.anime_name)
    print("Status:",object.status)

def print_latest(object):

    print()
    print(object.episode,"[{}]".format(object.upload_date))
    print(object.episode_link)