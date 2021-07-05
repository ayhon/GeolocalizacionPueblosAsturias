import sys
import time
import json
from urllib.parse import quote as encode

import requests
import bs4
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim # Data form Open Street Map
                                      # Lim: 1 req/s

# debug = lambda *text : print(*text, file=sys.stderr)
debug = lambda *text : 1 # Do nothing

debug(__name__)

URL_SEARCH="https://www.pueblosdeasturias.es/buscador?q="
URL="https://www.pueblosdeasturias.es/"
GEOLOCATER = Nominatim(user_agent="Prueba")

def url2html(url,extra):
    """Return html as a string given a webpage's url"""
    return requests.get(url + encode(extra)).text

def get_more_data(address):
    """ Get more data from pueblosdeasturias.es """

    debug("Pueblo:,",address)
    soup = BeautifulSoup(url2html(URL_SEARCH, address), "lxml")
    search_results = soup.find("ul", "resultados")
    info_link = search_results.find("a")["href"] # Only interested in firts result
    debug("Link con la información:",info_link)

    results = {}
    scrape_soup = BeautifulSoup(url2html(URL, info_link), "lxml")
    tables = scrape_soup.find("section","widget").findAll("table","datos_pueblo")
    for table in tables:
        data = table.findAll("tr")
        for row in data:
            debug("Item:",row,"\nTipo:", type(row))
            if isinstance(row, bs4.NavigableString):
                continue # Parece que siempre son el primer y último elemento
            debug("Children:",[ x.text for x in row.children if not isinstance(x,bs4.NavigableString)])
            key, value = [ x.text for x in row.children if not isinstance(x,bs4.NavigableString)]
            results[key] = value

    return results
    
def get_coords(address):
    """ Get a place's latitude and longitude"""
    # time.sleep(1)
    data = GEOLOCATER.geocode(address).raw
    return {
            "Latitud": data["lat"],
            "Longitud": data["lon"]
    }


def get_info(address):
    """Simple program to get data from an address"""
    res = get_more_data(address)
    res.update(get_coords(address))
    return res

def main(address):
    """Simple program to print data from an address"""
    if not address or address == "":
        raise TypeError("Proporciona una dirección como argumento, recibido \"" + address + "\"")
    print(json.dumps(get_info(address),indent=4))

if __name__ == "__main__":
    main(" ".join(sys.argv[1:])) # Avoid script name
