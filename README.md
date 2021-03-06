# GeolocalizacionPueblosAsturias

###### Práctica propuesta y supervisada por Beatriz González Pérez, profesora de la Estadística del doble grado Ingeniería Informática y Matemáticas de la Facultad de Ciencias Matemáticas de la Universidad Complutense de Madrid

Pequeño script de python que usa tanto `OpenStreetMaps` como `puebosdeasturas.es` para sacar información de los pueblos de Asturias

## Instalación

Gestiono las dependencias del script usando `pipenv`. Para conseguir el mismo entorno, basta con hacer `pipenv install` en la carpeta del repositorio.

## Método de uso

`geoloc.py` es el script en si. Se puede usar como una librería que importar en python, o como un programa aislado.

Como programa aislado, recibe como primer argumento el nombre del pueblo del que se quiere recibir la información

```
python3 geoloc.py Torio
```

Como librería de python, las funciones interesantes son:
 * `get_info(pueblo)`  
   Es una combinación de las dos funciones siguientes.
 * `get_coords(pueblo)`  
   Devuelve la latitud y longitud del pueblo `pueblo`
 * `get_more_data(pueblo)`
   Devuelve datos extra del pueblo. Por ahora estos son:
   * Altitud
   * Concejo
   * Parroquia
   * Tipo
   * Hombres
   * Mujeres
   * Viviendas
   * Población
