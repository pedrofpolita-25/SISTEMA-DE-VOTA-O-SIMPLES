import os
import json
from datetime import datetime

def garantir_arquivos():
    # Garante que a pasta dados exista
    if not os.path.exists("dados"):
        os.makedirs("dados")

    # Garante que o arquivo votos exista
    if not os.path.exists("dados/votos.json"):
        with open("dados/votos.json", "w", encoding="utf-8") as f:
            json.dump([], f)

    # Garante que o arquivo de log exista
    if not os.path.exists("dados/log.txt"):
        open("dados/log.txt", "a", encoding="utf-8").close()

def registrar_log(acao):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("dados/log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{data_hora}] {acao}\n")
