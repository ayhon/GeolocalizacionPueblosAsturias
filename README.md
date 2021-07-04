# GeolocalizacionPueblosAsturias
Pequeño script de python que usa tanto `OpenStreetMaps` como `puebosdeasturas.es` para sacar información de los pueblos de Asturias

## Método de uso

`geoloc.py` es el script en si. Se puede usar como una librería que importar en python, o como un programa aislado.

Como programa aislado, recibe como primer argumento el nombre del pueblo del que se quiere recibir la información

```
python3 geoloc.py Torio
```

Como librería de python, las dos funciones interesantes son:
 * `get_coords(pueblo)`  
   Devuelve la latitud y longitud del pueblo `pueblo`
 * `get_more_data(pueblo)`
   Devuelve datos extra del pueblo. Por ahora estos son:
   * Altitud
   * Concejo
   * Parroquia
   * Tipo
