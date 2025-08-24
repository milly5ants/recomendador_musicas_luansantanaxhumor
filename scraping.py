import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor

# Caminho do CSV existente
csv_path = "data/raw/musicas.csv"

# Ler CSV existente se houver
if os.path.exists(csv_path):
    df_existente = pd.read_csv(csv_path)
    titulos_existentes = set(df_existente['titulo'])
else:
    df_existente = pd.DataFrame(columns=['titulo', 'letra'])
    titulos_existentes = set()

# Scraping da página do artista
url_artista = 'https://www.letras.mus.br/luan-santana/'
response = requests.get(url_artista)
soup = BeautifulSoup(response.text, 'html.parser')

# Montar lista apenas com músicas novas
musicas_novas = []
for li_tag in soup.find_all("li", class_="songList-table-row"):
    titulo = li_tag.get("data-name")
    data_url = li_tag.get("data-url")
    if titulo and data_url and titulo not in titulos_existentes:
        url_completa = "https://www.letras.mus.br" + data_url
        musicas_novas.append({"titulo": titulo, "url": url_completa})
    #if len(musicas_novas) >= 5:   # Limite de 5 músicas
    #    break

print(f"{len(musicas_novas)} músicas novas encontradas.")

# Função para extrair letra de uma música
def extrair_letra(musica):
    try:
        response = requests.get(musica["url"])
        soup = BeautifulSoup(response.text, "html.parser")
        div_letra = soup.find("div", class_="lyric-original")
        if div_letra:
            letra = div_letra.get_text(separator=" ").strip()
            return {"titulo": musica["titulo"], "letra": letra}
    except Exception as e:
        print(f"Erro em {musica['titulo']}: {e}")
    return None

# Usar ThreadPoolExecutor para acelerar scraping
with ThreadPoolExecutor(max_workers=5) as executor:
    resultados = list(executor.map(extrair_letra, musicas_novas))

# Filtrar resultados válidos
novas_musicas_extraidas = [r for r in resultados if r]

# Atualizar DataFrame e salvar CSV
df_atualizado = pd.concat([df_existente, pd.DataFrame(novas_musicas_extraidas)], ignore_index=True)
df_atualizado.to_csv(csv_path, index=False)

print("CSV atualizado com músicas novas!")
