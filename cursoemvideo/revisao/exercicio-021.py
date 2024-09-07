''' Faça um programa em Python
    que abra e reproduza o
    áudio de um arquivo MP3. '''

'''
    Instale esta biblioteca utilizando:

    pip install playsound

'''
import requests
from playsound import playsound

# URL do arquivo MP3
url = "https://www.fiftysounds.com/music/consistency.mp3"

# Nome do arquivo local
local_file = "consistency.mp3"

# Baixa o arquivo MP3
response = requests.get(url)
with open(local_file, "wb") as file:
    file.write(response.content)

# Toca o arquivo MP3
playsound(local_file)

# Mensagem de conclusão
print("Música finalizada.")
