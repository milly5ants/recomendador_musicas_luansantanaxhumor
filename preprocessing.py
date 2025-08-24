import pandas as pd 
import re  # Importa a biblioteca de expressões regulares

df = pd.read_csv("data/raw/musicas.csv", encoding="utf-8")

def limpar_letra(letra):
    letra = letra.lower()  # Converte para minúsculas
    letra = re.sub(r'\[.*?\]', '', letra)  # Remove seções entre colchetes
    letra = re.sub(r'[^a-záéíóúãõç\s]', '', letra)  # Remove caracteres especiais, mantendo letras e espaços
    letra = re.sub(r'\s+', ' ', letra).strip()  # Remove espaços extras
    return letra

df['letra_limpa'] = df['letra'].apply(limpar_letra)

df.to_csv("data/processed/musicas_limpa.csv", index=False, encoding="utf-8")

print("Pré-processamento concluído e salvo em 'data/processed/musicas_limpa.csv'")