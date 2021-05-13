import datetime
import time
from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier
from datetime import datetime as dt
import os

toast = ToastNotifier()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# toast.show_toast("CricPing", "Software was successfully installed..." + '\n' + "RESTART your PC now",
#                  duration=15, icon_path=resource_path("bell.ico"))


def cric():

    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    # print(current_time)

    cbuzz = requests.get('https://www.cricbuzz.com/').text

    soup = BeautifulSoup(cbuzz, 'lxml')

    matches = soup.find_all(
        'li', class_='cb-col cb-col-25 cb-mtch-blk cb-vid-sml-card-api videos-carousal-item cb-carousal-item-large cb-view-all-ga')

    for match in matches:
        match_name = match.find('a')
        result = match_name.find('div', class_='cb-ovr-flo cb-text-preview')
        # toss = match_name.find('div', class_='cb-ovr-flo cb-text-preview')
        score = match_name.find(
            'div', class_='cb-ovr-flo', style='display:inline-block; width:140px')
        today = dt.now()
        # today = today.strftime("%d/%m/%Y %H:%M:%S")
        # today = today.strftime("%d/%m/%Y")
        name = match_name['title']
        name = name.split("-", 1)
        name = name[0]

        # print(score)

        if result and score is None:

            resu = result.text

            # print(name)
            # print(resu)

            if resu:
                toast.show_toast("Today's match:", name + '\n' +
                                 resu, duration=15, icon_path=resource_path("bell.ico"))


def checkNet(i):
    # if i == 0:
    # toast.show_toast("CricPing", "Checking for internet connection...",
    #                  duration=15, icon_path=resource_path("alert.ico"))
    try:
        response = requests.get("http://www.google.com")
        global j
        if j == False:
            # toast.show_toast("CricPing", "Connected to the Internet.",
            #                  duration=15, icon_path=resource_path("alert.ico"))
            j = True
        return True
    except requests.ConnectionError:
        if i % 7 == 0:
            toast.show_toast("CricPing", "Check Your Internet connection!",
                             duration=15, icon_path=resource_path("alert.ico"))
        return False


i = 0
j = False

# checkNet(i)
# cric()

while(True):

    checkNet(i)
    cric()
    # sleep for 4 hrs => 60*60*4 sec
    time.sleep(60*30)
