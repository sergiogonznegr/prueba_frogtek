# Solución prueba técnica
Propuesta de solución a la prueba técnica solicitada por Frogtek

## Table of Contents
1. [¿En qué consiste?](#en_que_consiste)
2. [Estructura del proyecto](#technologies)
3. [Tecnologías usadas](#tecnologías)
4. [Instalación](#instalacion)
5. [Ejecución](#ejecucion)


## ¿En qué consiste?
La prueba consiste en realizar 3 ejercicios:
#### Ejercicio 1:
Escribe un script que sume todos los números de una cadena de texto pasada por
parámetros.
*  Ejemplos:
   *  "Frogtek se fundó en 2010 y ahora tiene 40 empleados", devolvería "2050"
   *  "Frogtek desarrolla un software para la gestión de tiendas de barrio", devolvería "0"
 
#### Ejercicio 2:
Escribe un script que borre los ceros por la izquierda de una dirección IP pasada por
parámetros.
*  Ejemplo:
   *  "210.010.090.180", devolvería "210.10.90.180" 

#### Ejercicio 3:
Escribe un script en Python que tome como entrada un fichero con una lista con las
siguientes ciudades españolas (Huesca, Frogtek, Jaca, Guadalajara), una por línea. Por
cada una de las ciudades, el script hará dos queries a la API de OpenWeather
(https://openweathermap.org) y guardará en el fichero original los datos que pedimos,
separados por una coma (,):

*   Usando el nombre de la ciudad, consulta y guarda la temperatura, la velocidad del
viento y sus coordenadas geográficas (longitud y latitud).
*   Usando las coordenadas del punto anterior, consulta y guarda la hora del
amanecer y anochecer y valida que el nombre de la ciudad devuelto por la petición
usando coordenadas devuelve el mismo nombre de la ciudad del listado.

Si en el punto 1), hay algún tipo de error, se rellenarán los valores con 0 y no se hará la
petición 2).

Por ejemplo, si el listado inicial fuera de dos ciudades de nombre EXISTE y NOEXISTE, el
fichero final quedaría así:

    EXISTE,23.21,2.54,-0.7499,40.560,06:45:12,21:45:12
    NOEXISTE,0,0,0,0

## Estructura del proyecto

En la raíz del proyecto se encuentran los archivos más orientados a la configuración:

1) requirements
2) Dockerfile  
3) docker-compose.yml
4) pyproject.toml
5) también los ocultos de git, o el de flake8

Aquí también se encuentra la carpeta de `src` dónde están todos los archivos de `python` que hacen funcionar el proyecto


## Tecnologías usadas:

### Para el funcionamiento
Docker. Se utilizar para encapsular todo el proyecto dentro del mismo entorno y que pueda ser portable, cuenta con la creación de una imange propia mediante el `Dockerfile` y en base a la imagen `python:3.12.5-bullseye`

Con docker-compose vamos a poder ejecutar cada uno de los scripts, e incluso los tests. Luego lo vemos

### Para el formato de código
Para modelar los estilos de código: saltos de linea, errores con el PEP, imports, formateo de las líneas, etc. Vamos a usar las herramientas de:

*   isort
*   black
*   flake8

Isort y Black nos va a ayudar con los errores de estilizado el código, haciendo los saltos donde se debe, dejando 1 o 2 líneas de separación entre clases o funciones, optimizando los imports, etc. Todo de manera automática y formateando ellos mismos el código

Por otro lado, flake8 nos va a ayudar e cumplir con las reglas de <a href="https://peps.python.org/pep-0008/">PEP8</a>. Aunque solo va a dar el aviso, o va a modificar nada.

### Control de versiones
GIT. Se ha usado para tener un contro sobre los cambios del código así como mediante las GitHub Actions se realiza el 'linteo' del código (como aviso, no impide hacer nada) y la ejecución de los tests (lo mismo, como aviso)

## Instalación

Hay que tener git en tu pc para poder realizar la instalación.

Para instalar el proyecto:

    git clone https://github.com/sergiogonznegr/prueba_frogtek.git

## Ejecución

Para poder ejecutar el proyecto, hay que tener Docker instalado y funcionando, ya que todo funciona mediante esta tecnología.

Después de clonar el proyecto, hay que entrar en la carpeta raíz del proyecto, donde se encuentra el `Dockerfile` y el `docker-compose.yml`.

#### Ejercicio 1
Estando aquí podemos lanzar el comando:

    docker compose up ejercicio1

Esto hará que se lance el servicio: ejercicio1, lo que ejecutará:

      ejercicio1:
        build:
            context: .
            dockerfile: Dockerfile  
        image: prueba_frogtek:0.0.1  
        container_name: prueba_frogtek_ejercicio1  
        command: python3 /opt/src/ejercicios/ejercicio1/ejercicio1_launcher.py --text_string "En el año 2010 España ganó el 1er mundial de fútbol de su historia"

*La primera vez puede tardar un poco, tiene que construir la imagen*

Lo que deberá mostrar el siguiente resultado:

     ✔ Container prueba_frogtek_ejercicio1  Created                                  1.9s 
    Attaching to prueba_frogtek_ejercicio1
    
    - prueba_frogtek_ejercicio1  | 2024-10-02 21:34:16 [INFO] La string que se ha pasado es: 'En el año 2010 España ganó el 1er mundial de fútbol de su historia'

    - prueba_frogtek_ejercicio1  | 2024-10-02 21:34:16 [INFO] La suma resultante de los números extraídos es: 2011

    - prueba_frogtek_ejercicio1 exited with code 0

Esto quiere decir que el ejercicio1 se ha ejecutado correctamente. En caso de querer enviar otro argumento, habría que cambiar el argumento `--text_string` y poner lo que queramos como valor, siempre entrecomillado


#### Ejercico 2

Lo mismo, estando en la ruta del docker-compose.yml y Dockerfile, podemos lanzar el comando:

    docker compose up ejercicio2

Esto lanzará:

    ejercicio2:
        build:
            context: .
            dockerfile: Dockerfile  
        image: prueba_frogtek:0.0.1  
        container_name: prueba_frogtek_ejercicio2
        command: python3 /opt/src/ejercicios/ejercicio2/ejercicio2_launcher.py --ip "127.0.012.123"


Si antes hemos lanzado el ejercicio 1, no tiene que reconstruir la imagen, por lo que irá más rápido. El resultado esperado sería este:

     ✔ Container prueba_frogtek_ejercicio2  Created                              1.0s

    Attaching to prueba_frogtek_ejercicio2

    prueba_frogtek_ejercicio2  | 2024-10-02 21:40:48 [INFO] La ip que se ha pasado es: '127.0.012.123'

    prueba_frogtek_ejercicio2  | 2024-10-02 21:40:48 [INFO] Se han encontrado ceros a la izquierda de algún subgrupo. Se van a eliminar

    prueba_frogtek_ejercicio2  | 2024-10-02 21:40:48 [INFO] La nueva IP formada es: '127.0.12.123'

Al igual que en el ejercicio 1, aquí también se puede modificar el valor del argumento, en este caso se llama `--ip` y como antes, tiene que ir entrecomillado


#### Tests

Para poder ejecutar los tests, hay otro servicio que lo hace, podemos lanzar el comando:

    docker compose up tests

Esto lanzará:

    tests:
        build:
            context: .
            dockerfile: Dockerfile  
        image: prueba_frogtek:0.0.1  
        container_name: prueba_frogtek_tests
        command: pytest -v

Y el resultado de los tests debería ser:

    prueba_frogtek_tests  | ============================= test session starts ==============================
    prueba_frogtek_tests  | platform linux -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0 -- /usr/local/bin/python
    prueba_frogtek_tests  | cachedir: .pytest_cache
    prueba_frogtek_tests  | rootdir: /opt/src
    prueba_frogtek_tests  | plugins: vcr-1.0.2, cov-5.0.0
    prueba_frogtek_tests  | collecting ... collected 33 items
    prueba_frogtek_tests  | 
    prueba_frogtek_tests  | test/ejercicio1/test_get_numbers.py::test_get_numbers[Frogtek se fund\xf3 en 2010 y ahora tiene 40 empleados-expected0] PASSED [  3%]
    prueba_frogtek_tests  | test/ejercicio1/test_get_numbers.py::test_get_numbers[Frogtek desarrolla un software para la gesti\xf3n de tiendas de barrio-expected1] PASSED [  6%]
    prueba_frogtek_tests  | test/ejercicio1/test_set_numbers.py::test_sum_numbers_works_properly PASSED [  9%]
    prueba_frogtek_tests  | test/ejercicio1/test_set_numbers.py::test_sum_numbers_raise_exception PASSED [ 12%]
    prueba_frogtek_tests  | test/ejercicio2/test_delete_zeros.py::test_delete_zeros PASSED           [ 15%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_left_zeros[01.100.12.23-True] PASSED [ 18%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_left_zeros[10.000000100.012.023-True] PASSED [ 21%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_left_zeros[1.100.00012.023-True] PASSED [ 24%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_left_zeros[01.0100.012.023-True] PASSED [ 27%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_not_left_zeros[1.100.12.23-False] PASSED [ 30%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_not_left_zeros[127.0.0.1-False] PASSED [ 33%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_not_left_zeros[190.123.34.6-False] PASSED [ 36%]
    prueba_frogtek_tests  | test/ejercicio2/test_ip_has_left_zeros.py::test_ip_has_not_left_zeros[10129393.24534.24534.346-False] PASSED [ 39%]
    prueba_frogtek_tests  | test/ejercicio2/test_make_new_ip.py::test_make_new_ip PASSED             [ 42%]
    prueba_frogtek_tests  | test/ejercicio2/test_split_ip.py::test_split_ip PASSED                   [ 45%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_authenticator.py::test_authenticator PASSED [ 48%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_city_name PASSED [ 51%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_city_name_set_authenticator PASSED [ 54%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_city_name_create_url PASSED [ 57%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_city_name_request_data PASSED [ 60%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_geolocation_data PASSED [ 63%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_geolocation_data_set_authenticator PASSED [ 66%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_geolocation_data_create_url PASSED [ 69%]
    prueba_frogtek_tests  | test/ejercicio3/api_connector/test_open_weather_client.py::test_open_weather_by_geolocation_data_request_data PASSED [ 72%]
    prueba_frogtek_tests  | test/ejercicio3/model_data/test_modeling_cities_data.py::test_data_city_modeling_response PASSED [ 75%]
    prueba_frogtek_tests  | test/ejercicio3/model_data/test_modeling_cities_data.py::test_sun_data_modeling_response PASSED [ 78%]
    prueba_frogtek_tests  | test/ejercicio3/test_convert_path_to_full_path.py::test_partial_path_to_full_path PASSED [ 81%]
    prueba_frogtek_tests  | test/ejercicio3/test_get_content_file.py::test_get_content_file PASSED   [ 84%]
    prueba_frogtek_tests  | test/ejercicio3/test_get_weather_data_by_city_name.py::test_get_weather_data_by_city_name_200 PASSED [ 87%]
    prueba_frogtek_tests  | test/ejercicio3/test_get_weather_data_by_city_name.py::test_get_weather_data_by_city_name_404 PASSED [ 90%]
    prueba_frogtek_tests  | test/ejercicio3/test_get_weather_data_by_geolocation_data.py::test_get_weather_data_by_geolocation_data PASSED [ 93%]
    prueba_frogtek_tests  | test/ejercicio3/test_get_weather_data_by_geolocation_data.py::test_get_weather_data_by_geolocation_data_not_match_city_name PASSED [ 96%]
    prueba_frogtek_tests  | test/ejercicio3/test_write_data_in_file.py::test_write_data_in_file PASSED [100%]
    prueba_frogtek_tests  | 
    prueba_frogtek_tests  | ============================== 33 passed in 0.18s ==============================
    prueba_frogtek_tests exited with code 0


#### Ejercicio 3

Para ejecutar el ejercicio 3 hay varias formas

La primera sería igual que el resto:

    docker compose up ejercicio3

Que ejecutará:

    ejercicio3:
        build:
            context: .
            dockerfile: Dockerfile  
        image: prueba_frogtek:0.0.1  
        volumes:
            - ./src/ejercicios/ejercicio3:/opt/src/ejercicios/ejercicio3
        container_name: prueba_frogtek_ejercicio3
        command: python3 /opt/src/ejercicios/ejercicio3/ejercicio3_launcher.py


Que nos mostrará lo siguiente:

     ✔ Container prueba_frogtek_ejercicio3  Created                                                                                          1.1s 
    Attaching to prueba_frogtek_ejercicio3
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:11 [INFO] Se van a recoger los datos del archivo: /opt/src/ejercicios/ejercicio3/ciudades_openweather.txt
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:11 [INFO] El contenido sin transformar del archivo es: Huesca,
    prueba_frogtek_ejercicio3  | Frogtek,
    prueba_frogtek_ejercicio3  | Jaca,
    prueba_frogtek_ejercicio3  | Guadalajara
    prueba_frogtek_ejercicio3  | 
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:11 [INFO] Contenido del archivo: ['Huesca', 'Frogtek', 'Jaca', 'Guadalajara']
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:11 [INFO] Datos de la ciudad: DataCity(coord=Coord(lon='-0.4087', lat='42.1362'), main=Temp(temp='16.14'), wind=Wind(speed='4.12'), name='Huesca', sun=None)
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:11 [INFO] Datos de la ciudad: DataCity(coord=Coord(lon='0', lat='0'), main=Temp(temp='0'), wind=Wind(speed='0'), name='Frogtek', sun=None)
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:11 [WARNING] La ciudad Frogtek no existe o no tiene registros en la API
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:12 [INFO] Datos de la ciudad: DataCity(coord=Coord(lon='-0.5499', lat='42.569'), main=Temp(temp='13.88'), wind=Wind(speed='3.31'), name='Jaca', sun=None)
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:12 [INFO] Datos de la ciudad: DataCity(coord=Coord(lon='-103.3333', lat='20.6667'), main=Temp(temp='26.19'), wind=Wind(speed='2.71'), name='Guadalajara', sun=None)
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:12 [INFO] Los datos fueron escritos en el archivo correctamente
    prueba_frogtek_ejercicio3  | 2024-10-02 21:52:12 [INFO] El contenido final del archivo es:
    prueba_frogtek_ejercicio3  | 
    prueba_frogtek_ejercicio3  | Huesca,16.14,4.12,42.1362,-0.4087,05:59:51,17:41:43
    prueba_frogtek_ejercicio3  | Frogtek,0,0,0,0
    prueba_frogtek_ejercicio3  | Jaca,13.88,3.31,42.569,-0.5499,06:00:36,17:42:06
    prueba_frogtek_ejercicio3  | Guadalajara,26.19,2.71,20.6667,-103.3333,12:44:39,00:40:08
    prueba_frogtek_ejercicio3  | 
    prueba_frogtek_ejercicio3 exited with code 0


También está la posibilidad de usar el archivo que se quiera, siempre y cuando tenga el formato correcto:

    CIUDAD1,
    CIUDAD2,
    CIUDAD3

Este archivo, a diferencia del que hay por defecto, es de un solo uso (de manera automática).

Para ejecutar un archivo externo, hay que crearlo en la carpeta `ext_files`, que está dentro de src, y luego añadir el argumento `--file_path` y añadir la ruta completa al archivo (ruta del contenedor):

    ejercicio3_custom_file:
        build:
        context: .
            dockerfile: Dockerfile  
            image: prueba_frogtek:0.0.1  
        volumes:
        - ./src/ext_files:/opt/src/ext_files
        container_name: prueba_frogtek_ejercicio3_custom_file
        command: python3 /opt/src/ejercicios/ejercicio3/ejercicio3_launcher.py --file_path "/opt/src/ext_files/prueba_ciudades.txt"

Para lanzar esto, hay que lanzar el mismo comando, pero añadiendo el argumento --build

    docker compose up --build ejercicio3_custom_file

Este argumento `--build` lo que hará será reconstruir la imagen de nuevo, y así añadir el archivo dentro del contenedor de ejecución:

     ✔ Container prueba_frogtek_ejercicio3_custom_file  Recreated                                                                            1.6s 
    Attaching to prueba_frogtek_ejercicio3_custom_file
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:17 [INFO] Se van a recoger los datos del archivo: /opt/src/ext_files/prueba_ciudades.txt
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:17 [INFO] El contenido sin transformar del archivo es: Toledo,
    prueba_frogtek_ejercicio3_custom_file  | Soria
    prueba_frogtek_ejercicio3_custom_file  | 
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:17 [INFO] Contenido del archivo: ['Toledo', 'Soria']
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:17 [INFO] Datos de la ciudad: DataCity(coord=Coord(lon='-4', lat='39.8333'), main=Temp(temp='18.36'), wind=Wind(speed='10.32'), name='Toledo', sun=None)
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:18 [INFO] Datos de la ciudad: DataCity(coord=Coord(lon='-2.6667', lat='41.6667'), main=Temp(temp='12.29'), wind=Wind(speed='2'), name='Soria', sun=None)
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:18 [INFO] Los datos fueron escritos en el archivo correctamente
    prueba_frogtek_ejercicio3_custom_file  | 2024-10-02 22:53:18 [INFO] El contenido final del archivo es:
    prueba_frogtek_ejercicio3_custom_file  | 
    prueba_frogtek_ejercicio3_custom_file  | Toledo,18.36,10.32,39.8333,-4,06:14:18,17:55:21
    prueba_frogtek_ejercicio3_custom_file  | Soria,12.29,2,41.6667,-2.6667,06:09:46,17:49:13
    prueba_frogtek_ejercicio3_custom_file  | 
    prueba_frogtek_ejercicio3_custom_file exited with code 0

