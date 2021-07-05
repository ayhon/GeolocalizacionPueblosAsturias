import requests
from bs4 import BeautifulSoup

URL_LIST="https://www.todopueblos.com/"

def get_list_towns(comunidad = "asturias"):
    s = BeautifulSoup(requests.get(URL_LIST+comunidad).text, "lxml")
    table = s.findAll("div")[1]

    return [x.text for x in table.findAll("b")]

if(__name__ == "__main__"):
    print(get_list_towns())
