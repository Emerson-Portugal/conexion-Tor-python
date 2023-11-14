# Creando una red Anonima con Tor

Es este script escrito en `python` utilizamos la red de Tor para hacer consultas `GET` de forma anonima a servicios `HTTP` para poder extraer informacion.

## Comparacion 

|                  | Sin TOR                                      | Con TOR                                      |
|------------------|----------------------------------------------|----------------------------------------------|
| Protocolo        | HTTP/1.0                                      | HTTP/1.1                                      |
| Estado           | 200 OK                                       | 301 Moved Permanently                         |
| Date             | Tue, 14 Nov 2023 13:21:55 GMT                 | -                                            |
| Server           | mw-web.codfw.main-5444c75fd6-sn2jm             | HAProxy                                      |
| Content-Length   | 22745                                        | 0                                            |
| Location         | -                                            | https://es.wikipedia.org/wiki/Wikipedia:Portada |
| X-Cache          | cp2031 hit, cp2041 hit/76                     | cp6009 int                                   |
| X-Cache-Status   | hit-front                                     | int-tls                                      |
| Connection       | -                                            | close                                        |
| Content-Type     | text/html; charset=UTF-8                      | -                                            |
| Content-Encoding | gzip                                         | -                                            |
| Cache-Control    | private, s-maxage=0, max-age=0, must-revalidate| -                                            |
| Accept-Ranges    | bytes                                        | -                                            |
| Content-Language | es                                           | -                                            |
| Set-Cookie       | Multiple                                     | -                                            |
| Server-Timing    | cache;desc="hit-front", host;desc="cp2041"    | -                                            |
| Strict-Transport-Security | max-age=106384710; includeSubDomains; preload | -                                            |
| Report-To        | JSON Object                                  | -                                            |
| NEL              | JSON Object                                  | -                                            |
| X-Client-IP      | 2001:1388:49ea:89a0:d872:965f:e1fd:2e07        | -                                            |
| Accept-CH        | -                                            | -                                            |
| Vary             | Accept-Encoding,Cookie                       | -                                            |
| Last-Modified    | Tue, 14 Nov 2023 13:21:53 GMT                 | -                                            |
| Age              | 946                                          | -                                            |
| GeoIP            | PE:ARE:Arequipa              | -                                            |


## Conclusion 

Como se puede observar, al realizar una solucitud `GET Normal`, se puede extraer mas informacion pero el costo es que revelas informacion como tu `Ubicacion` e `IP`, en cambio si usar la red Tor, podemos extraer menos informacion pero sin revelar nuestra `Ubicacion` o `IP`. 