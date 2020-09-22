import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from dotenv import load_dotenv
from defiis import getUrl
#Scrappear github y extraer memes 

baseUrl='https://github.com/ironhack-datalabs/datamad0820/pull/'
url = f'{baseUrl}{endpoint}'
res = requests.get(url, params=query_params, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
data=res.json()
print(f"Request")

at_Meme=soup.select('https://user-images.githubusercontent.com/57899051/93204470-70352280-f756-11ea-8895-95d1d3972560.jpg')


getUrl()
#escrapear nombre usuario para hacer registros de user diferenciados
#formar diccionario con meme, nombre usuario, url, llenar mongo d esos users