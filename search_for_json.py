import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
from pprint import pprint

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("This program will give you a possibility to search something in json")
print('')
acct = input('Enter Twitter Account: ')
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': '5'})
# print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)

def search_json(json):
    nick_pair = []
    nicknames = []
    j = 0
    for i in json['users']:
        nick_pair.append((i['screen_name'], j))
        nicknames.append(i['screen_name'])
        j += 1

    while True:
        print("Plese choose a person from friends of this account: ")
        pprint(nicknames)
        print("")
        nick = input("Give one name or press Enter: ")
        if len(nick) < 1: break

        for n in nick_pair:
            if n[0] == nick:
                 i = n[1]
                 break
            else:
                print("Give name from list")
                continue

        values = []
        print("This is all key that you can see")
        for k in json["users"][i]:
            values.append(k)
        pprint(values)

        while True:
            print("Press Enter to quit or give a key")
            key = input("Give a key, that value you want to see: ")
            if len(key) < 1: break
            print('')
            if key not in values:
                print("There is no such key\n")
            else:
                if isinstance(json["users"][0][key], list):
                    print("Value is a list. Do you want to see all elements or by idex?\n")
                    answ = input("Print 'All' or 'Index'\n")
                    if answ == "All":
                        pprint(json["users"][0][key])
                    elif answ == "Index":
                        ln = len(json["users"][0][key])
                        print("What index do you want? There is ", ln, " items")
                        ind = input("Index starts from 0: ")
                        try:
                            pprint(json["users"][0][key][ind])
                            print('')
                        except:
                            print("There is no such index")
                    else:
                        print("You need input only 'All' or 'Index'\n")

                elif isinstance(json["users"][0][key], dict):
                    print("Value is a dictionary. Do you want to see all elements or by key?\n")
                    answ = input("Print 'All' or 'Key'\n")
                    if answ == "All":
                        pprint(json["users"][0][key])
                    elif answ == "Key":
                        val = []
                        print("This is all key that you can see:")
                        for m in json["users"][0][key]:
                            val.append(m)
                        pprint(val)
                        k = input("Please, give key from list: ")
                        try:
                            pprint(json["users"][0][key][k])
                            print('')
                        except:
                            print("This key does not exist\n")
                    else:
                        print("You need input only 'All' or 'Key'\n")
                else:
                    if json["users"][0][key]:
                        print(json["users"][0][key])
                        print('')
                    else:
                        print("Nothing")
                        print('')
search_json(js)


# print(json.dumps(js, indent=2))
