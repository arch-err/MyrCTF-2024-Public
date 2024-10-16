Denna utmaning faller under WEB

Tanken är att det är en simpel hemsida. Den sårbara faktorn är 
kakan, som är custom för applikationen.

För att upptäcka kakan måste dock anställningsnumret kluras ut, då ett konto behövs för att få en kaka.

Kakan är enligt följande
KAKA_<RandomBokstäver20><användarnamnet i base64><4 Slumpmässiga Siffror>

Det som verifieras är användarnamnet i base64, inget annat.


Starta test-servern med: php -S 127.0.0.1:80
