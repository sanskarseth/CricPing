import datetime
import time
from bs4 import BeautifulSoup
import requests
from plyer import notification


html_text = requests.get('https://www.cricbuzz.com/').text

soup = BeautifulSoup(html_text, 'lxml')

matches = soup.find_all(
    'li', class_='cb-col cb-col-25 cb-mtch-blk cb-vid-sml-card-api videos-carousal-item cb-carousal-item-large cb-view-all-ga')

for match in matches:
    match_name = match.find('a')
    result = match_name.find('div', class_='cb-ovr-flo cb-text-complete')
    # toss = match_name.find('div', class_='cb-ovr-flo cb-text-preview')

    # try:
    #     if toss.text:
    #         print(f"Match: {match_name['title']}")
    #         print(f"Toss: {toss}")
    #         print('')
    # except:
    #     continue

    if result:
        name = match_name['title']
        resu = result.text

        notification.notify(
            # title of the notification,
            title="Match on {}".format(datetime.date.today()),
            # the body of the notification
            message=name + '\n' + resu,

            app_icon="cricket.ico",
            # the notification stays for 50sec
            timeout=10
        )

    # while(True):

    #     #sleep for 4 hrs => 60*60*4 sec
    #     #notification repeats after every 4hrs
    #     time.sleep(60*60*4)
