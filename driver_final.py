import requests
import random
import pandas as pd
import bs4 as scrape
from discord_webhook import DiscordWebhook, DiscordEmbed
import threading
import timeit
from queue import Queue

start = timeit.default_timer()
webhook = DiscordWebhook(url = 'Enter Webhook Here',rate_limit_retry=True)

def post_request(i):
    df = pd.read_csv("Bible.csv", header=None, encoding='unicode_escape')
    # Proxy
    proxy_string = df.iloc[i][0]

    ip = proxy_string.split(':')[0]
    port = proxy_string.split(':')[1]
    user = proxy_string.split(':')[2]
    pass_ = proxy_string.split(':')[3]

    proxy_input = F"http://{user}:{pass_}@{ip}:{port}"

    proxies = {'https': proxy_input,
               'http': proxy_input}

    # Telephone
    tel_number = int(df.iloc[i][5])
    tel_number = F"0{tel_number}"

    # Email
    email = df.iloc[i][1]

    # FirstName
    firstname = df.iloc[i][2]

    # LastName
    lastname = df.iloc[i][3]

    data_val = {"firstName": f"{firstname}",
                "lastName": f"{lastname}",
                "email": f"{email}",
                "emailConfirm": f"{email}",
                "telephoneNumber": F"{tel_number}",
                "county": '{"ID":55,"text":"Aberdeenshire"}',
                "county_search": None,
                "store": "Tesco",
                "above18": "Y",
                "terms": "Y",
                "marketing": None}

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "249",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "SSID=2983732_8fb422136",
        "Host": "7upmoments.promonow.io",
        "Origin": "https://7upmoments.promonow.io",
        "Referer": "https://7upmoments.promonow.io/",
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102" ',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        "X-Requested-With": "XMLHttpRequest"

    }

    # print("sending request")
    entry_response = requests.post(url='https://7upmoments.promonow.io/gateways/enter.php', headers=headers,
                                   data=data_val,
                                   proxies=proxies)
    print(entry_response.status_code)
    embedsuccess = DiscordEmbed(title='Successful Entry',
                                description="Site: ||7upMoments||\nEmail: ||" + F'{email}' + "||",
                                color='03b2f8')
    embedsuccess.set_image(url='https://upload.wikimedia.org/wikipedia/commons/f/fb/7-up_Logo.svg')
    embedsuccess.set_footer(text='LLBot LLC')
    embedsuccess.set_author(
        name="LLBot",
        icon_url="https://www.israelhayom.com/wp-content/uploads/2022/06/shapiro.jpg")
    embedsuccess.set_timestamp()

    if entry_response.status_code != 200:
        print("Entry Failed " + f'{email}')  # retry
    else:
        print("Entry Successful " + f'{email}')  # sendwebhook
        webhook.add_embed(embedsuccess)
        webhook.execute()


queue = Queue()
for i in range(2):
    worker = threading.Thread(target=post_request, args=(i,))

    worker.start()

queue.join()

stop = timeit.default_timer()
print('Time: ', stop - start)



