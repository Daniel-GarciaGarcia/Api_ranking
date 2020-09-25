import requests
from dotenv import load_dotenv
import os
import re
load_dotenv()


def get_github(endpoint, apiKey=os.getenv("GH_APIKEY"), query_params={}):
  

    baseUrl = "https://api.github.com"
    url = f"{baseUrl}{endpoint}"

    headers = {
        "Authorization": f"Bearer {apiKey}"
    }
    res = requests.get(url, params=query_params, headers=headers)

    print(f"Request data to {res.url} status_code:{res.status_code}")
    data = res.json()

    if res.status_code != 200:
        raise ValueError(f'Invalid github api call: {data["message"]}')

    return data



def extraccion_api(data):

    dictionary=[]
    for x in range(0,len(data)):
        try:
            name={'number':data[x]['number'],
            'title':re.match('\[(.*?)\]',data[x]['title'],re.IGNORECASE).group(1).replace('-',' '),
            'users':data[x]['user']['login'],
            'state':data[x]['state'],
            'created_at':data[x]['created_at'],
            'updated_at':data[x]['updated_at'],
            'closed_at':data[x]['closed_at'],
            'html_url':data[x]['html_url'],
            }
            dictionary.append(name)
        except:
            name={'number':data[x]['number'],
            'title':re.match('\[(.*?)\]',data[x-1]['title'],re.IGNORECASE).group(1).replace('-',' '),
            'users':data[x]['user']['login'],
            'state':data[x]['state'],
            'created_at':data[x]['created_at'],
            'updated_at':data[x]['updated_at'],
            'closed_at':data[x]['closed_at'],
            'html_url':data[x]['html_url'],
            }
            dictionary.append(name)
            
    return dictionary


