import sys
from pprint import pprint
from urllib.parse import quote as encode

import requests
import bs4
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim # Data form Open Street Map
                                      # Lim: 1 req/s

debug = lambda *text : print(*text, file=sys.stderr)
# debug = lambda *text : 1 # Do nothing

debug(__name__)

URL_SEARCH="https://www.pueblosdeasturias.es/buscador?q="
URL="https://www.pueblosdeasturias.es/"
GEOLOCATER = Nominatim(user_agent="Prueba")

def url2html(url,extra):
    """Return html as a string given a webpage's url"""
    return requests.get(url + encode(extra)).text

def get_more_data(address):
    """ Get more data from pueblosdeasturias.es """
    debug(address)
    soup = BeautifulSoup(url2html(URL_SEARCH, address), "lxml")
    results = soup.find("ul", "resultados")
    info_link = results.find("a")["href"] # Only interested in firts result
    debug(info_link)

    scrape_soup = BeautifulSoup(url2html(URL, info_link), "lxml")
    debug("scrape data")
    data = scrape_soup.find("table","datos_pueblo").find("tbody")
    debug(data)

    results = {}
    for child in data.children:
        if isinstance(child, bs4.NavigableString):
            continue
        key, value = [ x.text for x in child.children if not isinstance(x,bs4.NavigableString)]
        results[key] = value

    return results


def get_coords(address):
    """ Get a place's latitude and longitude"""
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
    pprint(get_info(address))

if __name__ == "__main__":
    main(" ".join(sys.argv[1:])) # Avoid script name
