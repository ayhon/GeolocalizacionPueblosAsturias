import sys

import pandas as pd

from geoloc import get_info
from get_list import get_list_towns

debug = lambda *text : print(*text, file=sys.stderr)
# debug = lambda *text : 1 # Do nothing

def add_to_list(dict, key, value):
    if not key in dict.keys():
        dict[key] = [value]
    else:
        dict[key] += [value]

def main():
    comunidad = "asturias"
    if len(sys.argv) > 2:
        comunidad = sys.argv[1]

    towns = get_list_towns(comunidad)
    result = {}
    for town in towns:
        debug(f"Debugging town: {town}")
        try:
            town_info = get_info(town)

            for key in town_info.keys():
                add_to_list(result, key, town_info[key])

            add_to_list(result, "Nombre", town)
        except :
            debug(f"Error with {town}")
            continue

    df = pd.DataFrame(result)
    print(df)
    df.to_csv(f'pueblos_{comunidad}.csv', sep=";")



if (__name__ == "__main__"):
    main()
