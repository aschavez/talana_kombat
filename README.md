#  Talana Kombat JRPG
Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

## Pre-requisitos
-   Docker 20.10.17^
-   Docker Compose 2.6.1^

##  Instalación
Simplemente es necesario clonar el repositorio, dependiendo del uso serán necesarios otros comandos.

```sh
git clone https://github.com/aschavez/talana_kombat.git
```

##  Uso
El repositorio actual se encuentra configurado para ejecutar un REST API dockerizado, pero se pueden usar tambien las librerias de controllador a modo CLI.

###  REST API

Será necesario inicializar el contenedor, para esto necesitaremos tener instalado docker y docker-compose.

```sh
docker-compose build #Solo si es la primera vez que se ejecuta
docker-compose up -d
```

Podemos usar CURL o algun gestor de peticiones REST para probar el endpoint.

```sh
curl --request POST 'http://localhost:9000/combat' \
--header 'Content-Type: application/json' \
--data-raw '{
  "player1": {
    "movimientos":["D","DSD","S","DSD","SD"],
    "golpes":["K","P","","K","P"]
  },
  "player2": {
    "movimientos":["SA","SA","SA","ASA","SA"],
    "golpes":["K","","K","P","P"]
  }
}'
```

Obtendremos una respuesta como esta:

```json
{
  "winner":  "Arnaldor Shuatseneguer",
  "turns_desc":  [
    "Tonyn avanza y da una patada",
    "Arnaldor usa un Remuyuken",
    "Tonyn usa un Taladoken",
    "Arnaldor se agacha y avanza",
    "Tonyn se agacha",
    "Arnaldor conecta un Remuyuken",
    "Arnaldor gana la pelea y aún le queda 2 de energía"
  ]
}
```

### CLI

Podemos usar las librerias del proyecto de la siguiente manera:

```python
import sys, os
sys.path.append(os.path.abspath('app/src'))

# Importando librias del proyecto
import config
from models.player import PlayerModel
from controllers.combat import CombatController

# Inicializando jugadores
player_tonyn = PlayerModel(**config.data_players['tonyn_stallone'])
player_arnaldor = PlayerModel(**config.data_players['arnaldor_shuatseneguer'])

# Inicializando el combate
combat = CombatController([player_tonyn, player_arnaldor])

# Setenado los comandos o movimientos
combat.set_commands(
    {"movimientos":["DSD", "S"]  ,"golpes":["P", ""]},
    {"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}
)

# Ejecutando el combate y obteniendo la narracion de turnos
turns_description = combat.play()

# Imprimiendo los resultados
for turn_desc in turns_description:
    print(turn_desc)
```

Obtendriamos la siguiente respuesta:

```sh
Tonyn conecta un Taladoken
Arnaldor da un puñetazo
Tonyn se agacha
Arnaldor avanza, se agacha y avanza
Tonyn no hace nada
Arnaldor retrocede, avanza y da un puñetazo
Tonyn no hace nada
Arnaldor avanza, avanza, avanza y da una patada
Tonyn no hace nada
Arnaldor da una patada
Tonyn no hace nada
Arnaldor lanza un Remuyuken
Arnaldor gana la pelea y aún le queda 3 de energía
```